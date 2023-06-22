import openai
import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from OpenAI_integration.secrets import MY_API_KEY

openai.api_key = MY_API_KEY


def gpt_response(user_prompt):
    std_gpt_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_prompt,
        temperature=.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return std_gpt_response["choices"][0]["text"]


def intentExtraction(user_prompt):
    intent = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Read the complete sentence {user_prompt} and then determine the intent or action to be performed in the following sentence '{user_prompt}'\nprint the response as intent=intent",
        temperature=0.3,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return intent["choices"][0]["text"]


def recognizeUseCase(intent):
    nlp = spacy.load('en_core_web_md')
    dance_keywords = ["dance", "dancing", "dancer", "ballet", "choreography", "perform", "rhythm"]
    song_keywords = ["sing", "song", "singing", "singer", "melody", "vocal", "music", "musical", "tune"]
    move_keywords = ["move", "moving", "mover", "motion", "action", "gesture", "step"]

    def get_embedding(word):
        # Used to find similar words from the given dataset
        return nlp.vocab[word].vector.reshape(1, -1)

    def find_similar_words(keyword_list, word):
        word_embedding = get_embedding(word)
        similarities = []  # Empty list to store similarity score

        for keyword in keyword_list:  # Iterating over all the words of the sentence
            keyword_embedding = get_embedding(keyword)
            similarity = cosine_similarity(word_embedding, keyword_embedding)  # Generating the similarity score
            similarities.append(similarity)  # Storing the score

        max_similarity_index = np.argmax(similarities)  # Gives the maximum value index
        max_similarity = similarities[max_similarity_index]  # Getting the maximum value
        similar_word = keyword_list[max_similarity_index]  # Retrieving the most similar word

        return similar_word, max_similarity

    def process_sentence(sentence):
        doc = nlp(sentence.lower())
        similar_words = []  # Will contain most similar words with similarity score
        meanings = []  # Will store the meaning associated with the similar word (song, dance, move)

        for token in doc:  # Iterating on every list if it matches then its belong to that list
            if token.text in dance_keywords:
                similar_words.append(find_similar_words(dance_keywords, token.text))
                meanings.append("dance")
            elif token.text in song_keywords:
                similar_words.append(find_similar_words(song_keywords, token.text))
                meanings.append("song")
            elif token.text in move_keywords:
                similar_words.append(find_similar_words(move_keywords, token.text))
                meanings.append("motion")

        if similar_words:
            similar_words.sort(key=lambda x: x[1],
                               reverse=True)  # Sorting the list in decending order based on similarity score
            selected_meanings = set(meanings)  # Storing unique values
            for meaning in selected_meanings:  # Iterating the set and calling the function
                if meaning == "dance":
                    return dance
                elif meaning == "song":
                    return song
                elif meaning == "motion":
                    return move
                else:
                    return gpt_response
        else:
            return gpt_response

    func = process_sentence(intent)
    return func


def extractSongDetails(song_prompt):
    default_time = 60
    default_song = "gaadi wala aya ghar se kachra nikal"
    song_details = []
    extract_song = f"extract the song name from the given {song_prompt} and print(song_name = song_name) otherwise print {default_song}"
    song_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=extract_song,
        temperature=0.1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    extract_time = f"perform necessary mathematical operation as mentioned in the '{song_prompt}' to extract the time duration from '{song_prompt}' and convert the value to seconds. If successful, print the response as time = time; otherwise, print {default_time}."
    time_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=extract_time,
        temperature=0.1,
        max_tokens=10,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(song_response)
    # print(time_response)

    input_string = song_response["choices"][0]["text"]
    start_index = input_string.find("\"") + 1
    end_index = input_string.rfind("\"")
    nameOfSong = input_string[start_index:end_index]
    song_details.append(nameOfSong)
    input_string = time_response["choices"][0]["text"]
    start_index = input_string.find("=") + 1
    end_index = input_string.find(";")
    value_string = input_string[start_index:end_index].strip()
    t = int(value_string)
    song_details.append(t)
    return song_details


def intent_preprocess(text):
    start_index = text.find("intent=")
    if start_index == -1:
        return None

    start_index += len("intent=")
    end_index = text.find(" ", start_index)

    if end_index == -1:
        intent = text[start_index:]
    else:
        intent = text[start_index:end_index]

    return intent


def song(name, time=30):
    print(f"playing song {name} for {time} seconds")


def dance():
    print("dancing like a pro")

def move():
    print("robot is moving")


if __name__ == '__main__':
    prompts = [
        "Move forward by 10 meters.",
        "Rotate 90 degrees to the left.",
        "Jump three times in a row.",
        "Walk in a zigzag pattern.",
        "Perform a somersault.",
        "Hop on one leg for 30 seconds.",
        "Crawl like a spider on the floor.",
        "Balance on one foot for as long as possible.",
        "Dance to your favorite song.",
        "Run in a circle around the room."
    ]

    for prompt in prompts:
        print(prompt)
        user_prompt = prompt
        intent = intentExtraction(user_prompt)
        intent = intent_preprocess(intent)
        if intent is None:
            print("Response : ", end='')
            print(gpt_response(user_prompt))
        else:
            print("intent =", intent)
            print("Response : ", end='')
            functionToBeCalled = recognizeUseCase(intent)
            if functionToBeCalled == song:
                name, time = extractSongDetails(user_prompt)
                song(name, time)
            if functionToBeCalled == dance:
                dance()
            if functionToBeCalled == move:
                move()
            if functionToBeCalled == gpt_response:
                print(gpt_response(user_prompt))
        print()
