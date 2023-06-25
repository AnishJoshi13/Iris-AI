import openai
from OpenAI_integration.secrets import MY_API_KEY

openai.api_key = MY_API_KEY

def move(prompt):
    print("robot is moving")
    # Generate the response using GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyse the input {prompt} ",
        max_tokens=10,
        n=1,
        temperature=0.1
    )

    intent_response = response["choices"][0]["text"]


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