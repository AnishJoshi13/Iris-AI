import openai
from OpenAI_integration.secrets import MY_API_KEY

openai.api_key = MY_API_KEY

predefined_tone = {
    "conversational",
    "lighthearted",
    "persuasive",
    "spartanformal"
    "formal",
    "firm"
}

def gpt_response_preprocessing(user_prompt):
    gpt_preprocess = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Please analyze the input sentence '{user_prompt}' and determine its tone. Compare it to the list of predefined tones: {predefined_tone}. Return the single best matching tone.",
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return gpt_preprocess["choices"][0]["text"]

def gpt_response(user_prompt,preprocessed_prompt):
    std_gpt_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Give the answer/response of input {user_prompt} in the tone {preprocessed_prompt}",
        temperature=.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return std_gpt_response["choices"][0]["text"]

if __name__ == '__main__':
    if __name__ == '__main__':
        sentence = "By investing in renewable energy sources, we can create a cleaner and more sustainable future for generations to come."
        s = gpt_response_preprocessing(sentence).lower()
        print(s)
        response = gpt_response(sentence, s)
        print(response)
