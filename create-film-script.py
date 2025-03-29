import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key='---API KEY DE OPEN AI https://platform.openai.com/---' #You have to Add credit to your Ope AI Account to get the API KEY
)

response = client.responses.create(


    input="Create a script about a powerful princess that gets lost in the forest. The princess has magic powers. Don't use animals in your story.""", #Your Prompt
    model="gpt-4o", #or any valid model for Open AI
    instructions="You are an expert horror screenwriter", #How the robot will behave
)

print(response.output_text)