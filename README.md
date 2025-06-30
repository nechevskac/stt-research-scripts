# stt-research-scripts

Python scripts and experiments used for my research paper on speech-to-text AI models. This repository includes model evaluations, accuracy benchmarks, and transcript quality comparisons using various open-source and cloud-based STT APIs.

````
> 💡 Tip: Place your audio file in the same directory and update `audio_path` in the scripts.
````


## Setup and run Whisper

Follow these steps to set up and run the Whisper transcription script:


### 1. Use Python 3.10

Make sure you have Python 3.10 installed on your machine.

> ⚠️ Whisper requires Python 3.10 due to dependency compatibility. Using other versions (like 3.11 or 3.12) may cause installation issues or runtime errors.

### 2. Create a virtual environment

```
python3.10 -m venv whisper-venv
```

### 3. Activate the virtual environment

```
source whisper-venv/bin/activate
```

### 4. Install dependencies

```
pip install openai-whisper
```

### 5. Run the transcription script

```
python3 stt-whisper-model.py
```

### 6. Deactivate the virtual environment

```
deactivate
```

## Setup and run Vosk

### 1. Download the English Vosk Model (lightweight)

```
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 vosk-model
```
This downloads and extracts the model to a folder named vosk-model which the script expects.

### 2. Create a virtual environment

```
python3.10 -m venv vosk-venv
```

### 3. Activate the virtual environment

```
source vosk-venv/bin/activate
```

### 4. Install dependencies

```
pip install vosk
```

### 5. Run the transcription script

```
python3 stt-vosk-model.py path/to/your/audio.wav
```
Replace `path/to/your/audio.wav` with the path to your WAV file (mono, 16kHz).

### 6. Output files
After running, two files will be generated in the script directory:

`transcription.json` — full transcription plus word-level timestamps
`transcription.txt` — full transcription as plain text

### 7. Deactivate the virtual environment

```
deactivate
```
## Setup and run AssemblyAI

### 1. Create a virtual environment

```
python3.10 -m venv assemblyai-venv
```

### 3. Activate the virtual environment

```
source assemblyai-venv/bin/activate
```

### 4. Install dependencies

```
pip install requests, dotenv
```

### 5. Run the transcription script

```
python3 stt-assemblyai-model.py
```

### 6. Deactivate the virtual environment

```
deactivate
```
