#%%
import os
import shutil
import glob

# Copy all files from 'whispers' folder to 'text' folder keeping text transcripted
from_folder = 'whispers'
to_folder = 'txt'

for file in glob.glob(os.path.join(from_folder, '*.txt')):
    if "2" in os.path.basename(file):
        shutil.copy(file, to_folder)

for file in glob.glob(os.path.join(to_folder, '*.txt')):
    with open(file, 'r') as f:
        lines = f.readlines()
        if  lines[0].startswith("Model"):
            lines = lines[3:]
            with open(file, 'w') as f:
                f.writelines(lines)