#%%
import os
import time
from datetime import timedelta
import whisper
import glob

####################
####################

FOLDER_WHISPERS = 'whispers_stats'
FOLDER_SRT = 'srt_files'
FOLDER_SOUND = "sounds"

sound_path = glob.glob(os.path.join(FOLDER_SOUND, '*'))[0]

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

####################
####################

start_load = int(time.time())
model = whisper.load_model(model_type)
end_load = int(time.time())
print('Model loaded in {} seconds'.format(end_load - start_load))

start_transcribe = int(time.time())
result = model.transcribe(sound_path)
print(result["text"])
end_transcribe = int(time.time())
print(f"Transcribed in {end_transcribe - start_transcribe} seconds")

# ----- STATS MODEL WHISPER ----- #
#store each result in 'result.txt' file
# with open(os.path.join(FOLDER_WHISPERS, model_type +".txt"), "w") as f:
#     f.write(f"Model {model_type}\nLoaded in {end_load - start_load} seconds\nTranscribed in {end_transcribe - start_transcribe} seconds")
#     f.write("\n")
#     f.write(result["text"].lstrip())

# # put "\r" after each ".", "!" and "?" to make a new line
# with open(os.path.join(FOLDER_WHISPERS, model_type +".txt"), "r") as f:
#     data = f.read()
# data = data.replace(". ", ".\r").replace("! ", "!\r").replace("? ", "?\r")
# with open(os.path.join(FOLDER_WHISPERS, model_type +"2.txt"), "w") as f:
#     # remove first 3 lines
#     for i, line in enumerate(data.splitlines()):
#         if i > 2:
#             f.write(line + "\r")

# ---- SRT FILE ---- #
segments = result['segments']


for segment in segments:
    startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
    endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
    text = segment['text']
    segmentId = segment['id']+1
    segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

    srtFilename = os.path.join(FOLDER_SRT, model_type + "_" + os.path.basename(sound_path) + ".srt")
    with open(srtFilename, 'a', encoding='utf-8') as srtFile:
        srtFile.write(segment)
