import openai
import os
from openai import OpenAI

openai.my_api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

class AskGpt:

    messages = []
    
    @staticmethod
    def ask_gpt(prompt):
        AskGpt.messages.append({"role" : "user", "content" : prompt})
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = AskGpt.messages
        )
        reply = response.choices[0].message.content
        AskGpt.messages.append({"role" : "assistant", "content" : reply})
        return reply

user_prompt = "What is the weather today like in Anand, Gujarat? Respond with maximum 20 words."
openai_response = AskGpt.ask_gpt(user_prompt)
print(openai_response)