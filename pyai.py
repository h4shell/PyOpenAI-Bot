import openai
from creds import *


def ai(message):
    models = openai.Model.list(key)

# print the first model's id
    completion = openai.ChatCompletion.create(key,
                                              model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
    return completion['choices'][-1]['message']['content']