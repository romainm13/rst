#%%
import os
import time
import whisper

FOLDER_WHISPERS = 'whispers'

###################
###################
# model_type = 'base'
# model_type = 'small'
model_type = 'medium'
"""
PEUT CRASH

RuntimeError: CUDA error: unknown error
CUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
"""
# model_type = 'large'
"""
CRASH

LOAD TIME ~ 15min

RuntimeError: CUDA error: unknown error
CUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
"""


start_load = int(time.time())
model = whisper.load_model(model_type)
end_load = int(time.time())
print('Model loaded in {} seconds'.format(end_load - start_load))

start_transcribe = int(time.time())
result = model.transcribe('/home/romainm13/rst/sounds/Flo - The Joke (audio-extractor.net).mp3')
print(result["text"])
end_transcribe = int(time.time())
print(f"Transcribed in {end_transcribe - start_transcribe} seconds")
#%%
#store each result in 'result.txt' file
with open(os.path.join(FOLDER_WHISPERS, model_type +".txt"), "w") as f:
    f.write(f"Model {model_type}\nLoaded in {end_load - start_load} seconds\nTranscribed in {end_transcribe - start_transcribe} seconds")
    f.write("\n")
    f.write(result["text"].lstrip())

#%%
# put "\r" after each ".", "!" and "?" to make a new line
with open(os.path.join(FOLDER_WHISPERS, model_type +".txt"), "r") as f:
    data = f.read()
data = data.replace(". ", ".\r").replace("! ", "!\r").replace("? ", "?\r")
with open(os.path.join(FOLDER_WHISPERS, model_type +"2.txt"), "w") as f:
    # remove first 3 lines
    for i, line in enumerate(data.splitlines()):
        if i > 2:
            f.write(line + "\r")