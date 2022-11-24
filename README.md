# rst

## Environnement

- WSL Ubuntu-20.04
- apt update + upgrade
- Clone repo git `rst`

In `rst` local git:

```bash
python3 -m venv rst_venv

# Activate venv
source rst_venv/bin/activate
# ou 
source ./activate
```

- Install `requirements.txt`

```bash
pip install -r requirements.txt
```

 - Install git-whisper

```bash
pip install git+https://github.com/openai/whisper.git
```

- Install `install.sh`


```bash
chmod +x …
sudo ./install.sh
```
