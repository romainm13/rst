#%%
import os
import time
import whisper

FOLDER_WHISPERS = 'whispers'
###################
###################
#%%

# 'base' model
model_type = 'base'

start_load = int(time.time())
model = whisper.load_model(model_type)
end_load = int(time.time())
print('Model loaded in {} seconds'.format(end_load - start_load))

start_transcribe = int(time.time())
result = model.transcribe('/home/romainm13/rst/Flo - The Joke (audio-extractor.net).mp3')
print(result["text"])
end_transcribe = int(time.time())
print(f"Transcribed in {end_transcribe - start_transcribe} seconds")

#store each result in 'result.txt' file
with open(os.path.join(FOLDER_WHISPERS, model_type +".txt", "w")) as f:
    f.write(f"Model {model_type}\nLoaded in {end_load - start_load} seconds\nTranscribed in {end_transcribe - start_transcribe} seconds\n")
    f.write(result["text"])
    f.write("\n\n")


###################
###################
#%%

# 'small' model
model_type = 'small'

start_load = int(time.time())
model = whisper.load_model(model_type)
end_load = int(time.time())
print('Model loaded in {} seconds'.format(end_load - start_load))

start_transcribe = int(time.time())
result = model.transcribe('/home/romainm13/rst/Flo - The Joke (audio-extractor.net).mp3')
print(result["text"])
end_transcribe = int(time.time())
print(f"Transcribed in {end_transcribe - start_transcribe} seconds")

#store each result in 'result.txt' file
with open(os.path.join(FOLDER_WHISPERS, model_type +".txt", "w")) as f:
    f.write(f"Model {model_type}\nLoaded in {end_load - start_load} seconds\nTranscribed in {end_transcribe - start_transcribe} seconds\n")
    f.write(result["text"])
    f.write("\n\n")


###################
###################
#%%
"""
PEUT CRASH

RuntimeError: CUDA error: unknown error
CUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
"""

# 'medium' model
model_type = 'medium'

start_load = int(time.time())
model = whisper.load_model(model_type)
end_load = int(time.time())
print('Model loaded in {} seconds'.format(end_load - start_load))

start_transcribe = int(time.time())
result = model.transcribe('/home/romainm13/rst/Flo - The Joke (audio-extractor.net).mp3')
print(result["text"])
end_transcribe = int(time.time())
print(f"Transcribed in {end_transcribe - start_transcribe} seconds")

#store each result in 'result.txt' file
with open(os.path.join(FOLDER_WHISPERS, model_type +".txt", "w")) as f:
    f.write(f"Model {model_type}\nLoaded in {end_load - start_load} seconds\nTranscribed in {end_transcribe - start_transcribe} seconds\n")
    f.write(result["text"])
    f.write("\n\n")


###################
###################
#%%
"""
CRASH

LOAD TIME ~ 15min

RuntimeError: CUDA error: unknown error
CUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
"""

# 'large' model
model_type = 'large'

start_load = int(time.time())
model = whisper.load_model(model_type)
end_load = int(time.time())
print('Model loaded in {} seconds'.format(end_load - start_load))

start_transcribe = int(time.time())
result = model.transcribe('/home/romainm13/rst/Flo - The Joke (audio-extractor.net).mp3')
print(result["text"])
end_transcribe = int(time.time())
print(f"Transcribed in {end_transcribe - start_transcribe} seconds")

#store each result in 'result.txt' file
with open(os.path.join(FOLDER_WHISPERS, model_type +".txt", "w")) as f:
    f.write(f"Model {model_type}\nLoaded in {end_load - start_load} seconds\nTranscribed in {end_transcribe - start_transcribe} seconds\n")
    f.write(result["text"])
    f.write("\n\n")
    
# %%
# put "\r" after each ".", "!" and "?" to make a new line
model_type = "medium"
with open(model_type + ".txt", "r") as f:
    data = f.read()
data = data.replace(". ", ".\r").replace("! ", "!\r").replace("? ", "?\r")
with open(model_type + "2.txt", "w") as f:
    f.write(data)