# Audio fileto SRT converter

## Brief history

I was working on Adobe Premier Pro and I wanted to use the `srt` format to add subtitles to my videos. I looked for online tools to convert my audio files to `srt` format but I didn't find any that I liked. So I decided to create my own tool.

## My Environnement

- WSL Ubuntu-20.04

## Installing

- Install `install.sh`

```bash
chmod +x install.sh
sudo ./install.sh
```

- create `srt` folder and move inside
- Clone `srt` git repo: `git clone https://github.com/romainm13/srt_whisper.git`
- Create `srt_venv` virtual environment

```bash
python3 -m venv srt_venv

# Activate venv
source srt_venv/bin/activate
# or
source ./activate

# Update pip
python3 -m pip install --upgrade pip
```

- Install `requirements.txt`

```bash
pip install -r requirements.txt
```

 - If whisper not installed (all conda packages nvidia, cuda ...) Install git-whisper (but normally ok)

```bash
pip install git+https://github.com/openai/whisper.git
```

## ToDo
