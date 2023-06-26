import openai
import re
from OpenAI_integration.secrets import MY_API_KEY
from src.intentExtractWithoutSpacy import intentExtraction
from src.Robo_Functions.Motion_functions import *
from src.Robo_Functions.Groove_Functions import *
from src.Robo_Functions.Iris_Chat import *
from src.Robo_Functions.Face_Detection import *

openai.api_key = MY_API_KEY

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
    "chat",
    "recognise_me"
}

if __name__ == '__main__':
    sentences = [

        "start face detection"

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
                    dance(processed_sentence)

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

                elif extracted_funcList == "recognise_me":
                    recognize_faces()

                elif extracted_funcList == "chat":
                    preprocess_tone = gpt_response_preprocessing(processed_sentence).lower()
                    chat_response = gpt_response(processed_sentence, preprocess_tone)
                    print(chat_response)

                else:
                    preprocess_tone = gpt_response_preprocessing(processed_sentence).lower()
                    chat_response = gpt_response(processed_sentence, preprocess_tone)
                    print(chat_response)

        except (ValueError, SyntaxError):
            print("Invalid intent response format.")