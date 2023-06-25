import openai
import re
from OpenAI_integration.secrets import MY_API_KEY
from src.intentExtractWithoutSpacy import intentExtraction

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


# Define the list of predefined functions
predefined_functions = {
    "dance",
    "moveForward",
    "moveBackward",
    "rotate",
    "moveHand1",
    "moveHand2",
    "movementCombo",
    "sing",
    "chat"
}


def extractSongDetails(song_prompt):
    default_time = 60
    default_song = "believer"
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
    if not nameOfSong:
        nameOfSong = default_song
    song_details.append(nameOfSong)

    input_string = time_response["choices"][0]["text"]
    t_match = re.search(r"time = (\d+)", input_string)
    if t_match:
        t = int(t_match.group(1))
    else:
        t = default_time
    song_details.append(t)
    # print(t)

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


def play_song(name, time):
    print(f"Playing song {name} for {time} seconds")


def sing_song(sentence):
    print("Singing a song")
    song_detail = extractSongDetails(sentence)
    if song_detail:
        song_name = song_detail[0]
        song_time = song_detail[1]
        play_song(song_name, song_time)


def dance():
    sing_song(processed_sentence)
    print("dancing like a pro")


def move():
    print("robot is moving")


def moveForward():
    print("Moving forward function")


def moveBackward():
    print("Moving backwards function")


def rotate():
    print("Rotating function")


def moveHand1():
    print("Moving hand one (Left hand) function")


def moveHand2():
    print("Moving hand 2 (right hand) function")


def movementCombo():
    print("Moving in combination function")


if __name__ == '__main__':
    sentences = [

        "play the song fairytale by alexander rybaks for 100 seconds and dance",
        "dance on your favorite song",
        "play song for squae root of 64 seconds",
        "What is arduino UNO"

    ]

# Loop over each sentence and check the response
for processed_sentence in sentences:
    print(processed_sentence)
    sentence = intentExtraction(processed_sentence)
    # Construct the prompt
    prompt = f"from the given input {sentence}. Analyze the intent and action to identify the best matching function from {predefined_functions}. Your response should return the list of (best matching function) otherwise return chat"

    # Generate the response using GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        n=1,
        temperature=0.1
    )

    intent_response = response["choices"][0]["text"]
    intent_list = intent_response.split(",")  # Split the string into a list
    print(intent_list)
    try:
        for extracted_funcList in intent_list:
            extracted_funcList = extracted_funcList.strip().strip("'").lower()
            print(extracted_funcList)
            if extracted_funcList == "dance":
                dance()

            elif extracted_funcList == "song" or extracted_funcList == "sing":
                sing_song(processed_sentence)

            elif extracted_funcList == "moveforward":
                moveForward()

            elif extracted_funcList == "movebackward":
                moveBackward()

            elif extracted_funcList == "rotate":
                rotate()

            elif extracted_funcList == "movehand1":
                moveHand1()

            elif extracted_funcList == "movehand2":
                moveHand2()

            elif extracted_funcList == "movementcombo":
                movementCombo()

            elif extracted_funcList == "chat":
                print(gpt_response(processed_sentence))
            else:
                print(gpt_response(processed_sentence))

    except (ValueError, SyntaxError):
        print("Invalid intent response format.")