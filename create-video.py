import time, base64
from runwayml import RunwayML

key = "--YOUR RUNWAY ML API KEY--" #You can get one at https://dev.runwayml.com/

client = RunwayML(api_key=key)

# Point this at your own image file
image = './--THE PATH TO YOUR IMAGE--/--THE NAME OF YOUR IMAGE--.png'

# encode image to base64
with open(image, "rb") as f:
    base64_image = base64.b64encode(f.read()).decode("utf-8")

# Create a new image-to-video task using the "gen3a_turbo" model
task = client.image_to_video.create(
  model='gen3a_turbo', #Latest model in march 2025
  prompt_image=f"data:image/png;base64,{base64_image}", #Base Image
  prompt_text='Generate a video with this image where the sun on the background moves to the sunset. Sun light glitters like at the golden hour. Main character turn their faces slowly to the camera.', #Your prompt

)

# Poll the task until it's complete
time.sleep(10)  # Wait for a second before polling
task = client.tasks.retrieve(task.id)
while task.status not in ['SUCCEEDED', 'FAILED']:
  time.sleep(10)  # Wait for ten seconds before polling
  task = client.tasks.retrieve(task.id)

print('Task complete:', task) #Here you'll get the URL of your generated Runway ML video