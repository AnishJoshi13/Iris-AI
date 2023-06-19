import openai
from secrets import MY_API_KEY

openai.api_key = MY_API_KEY

prompt = "Explain the basic functionality and components of Arduino boards"
response = openai.Completion.create(
    engine="text-davinci-003",  # Choose the desired language model, e.g., "davinci" or "curie"
    prompt=prompt,
    max_tokens=100,  # Adjust the desired response length
    n=1,  # Number of responses to generate
    stop=None,  # Optional: Specify a string to stop generation at
)

generated_text = response.choices[0].text.strip()
print(response)