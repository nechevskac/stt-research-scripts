# stt-research-scripts

Python scripts and experiments used for my research paper on speech-to-text AI models. This repository includes model evaluations, accuracy benchmarks, and transcript quality comparisons using various open-source and cloud-based STT APIs.

## Getting Started with Whisper

Follow these steps to set up and run the Whisper transcription script:

````markdown
> 💡 Tip: Place your audio file in the same directory and update `audio_path` in the script.
````

### 1. Use Python 3.10

Make sure you have Python 3.10 installed on your machine.

> ⚠️ Whisper requires Python 3.10 due to dependency compatibility. Using other versions (like 3.11 or 3.12) may cause installation issues or runtime errors.

### 2. Create a virtual environment

```bash
python3.10 -m venv whisper-venv
```

### 3. Activate the virtual environment

```bash
source whisper-venv/bin/activate
```

### 4. Install Whisper

```bash
pip install openai-whisper
```

### 5. Run the transcription script

```bash
python3 stt-whisper-model.py
```

### 6. Deactivate the virtual environment

```bash
deactivate
```
