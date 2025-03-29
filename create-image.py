from openai import OpenAI


client = OpenAI(
    api_key="---OPEN AI API KEY https://platform.openai.com/---"
)

response = client.images.generate(
    model="dall-e-3", #Or dall-e-2
    prompt="A tender husky in a snowy forest", #Your prompt
    size="1024x1024", #Only one of those:  [‘256x256’, ‘512x512’, ‘1024x1024’, ‘1024x1792’, ‘1792x1024’]
    quality="standard", #Only 'standard' or 'hq'
    n=1,
)

print(response.data[0].url)