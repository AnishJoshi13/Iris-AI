import openai

from OpenAI_integration.secrets import MY_API_KEY

openai.api_key = MY_API_KEY

def intentExtraction(user_prompt):
    intent = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Find out what the user wants to achieve from {user_prompt} and then determine a non-specific intent or action to be performed\nprint the response as intent,action",
        temperature=0.1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return intent["choices"][0]["text"]

# Define the list of sentences
sentences = [
    "Move forward by 10 meters.",
    "Play a song for square root of 64 seconds.",
    "Suggest me some tips for a healthy diet",
    "Rotate 90 degrees to the left.",
    "Dance with me",
    "Jump three times in a row.",
    "What is Arduino UNO",
    "Can we sway to the music as dance partners",
    "Walk in a zigzag pattern.",
    "Perform a somersault.",
    "Who are you and what is your purpose",
    "Play believer by Imagine Dragons",
    "Hop on one leg for 30 seconds.",
    "Crawl like a spider on the floor.",
    "Balance on one foot for as long as possible.",
    "Dance to your favorite song.",
    "Run in a circle around the room."
]

# Define the list of predefined functions
predefined_functions = {
    "dance()",
    "moveForward()",
    "moveBackward()",
    "rotate()",
    "moveHand1()",
    "moveHand2()",
    "movementCombo()",
    "sing()",
    "chat()"
}

# Loop over each sentence and check the response
for sentence in sentences:
    print(sentence)
    sentence = intentExtraction(sentence)
    # Construct the prompt
    prompt = f"from the given input {sentence}. Analyze the intent and action to identify the best matching function from {predefined_functions}. Your response should print(best matching function) otherwise print(no function matched) "

    # Generate the response using GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        n=1,
        temperature=0.3
    )

    print(response["choices"][0]["text"])
    print()
