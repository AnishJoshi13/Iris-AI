import openai
import re

from OpenAI_integration.secrets import MY_API_KEY

openai.api_key = MY_API_KEY

def play_song(name, time):
    print(f"Playing song {name} for {time} seconds")


def sing_song(sentence):
    print("Singing a song")
    song_detail = extractSongDetails(sentence)
    if song_detail:
        song_name = song_detail[0]
        song_time = song_detail[1]
        play_song(song_name, song_time)


def dance(processed_sentence):
    sing_song(processed_sentence)
    print("dancing like a pro")

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