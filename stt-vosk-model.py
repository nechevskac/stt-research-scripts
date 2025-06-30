import os
import wave
import json
import argparse
from vosk import Model, KaldiRecognizer

def main():
    # Parse command-line argument for the audio file
    parser = argparse.ArgumentParser(description="Transcribe WAV audio using Vosk.")
    parser.add_argument("audio", help="Path to a WAV audio file (mono, 16kHz)")
    args = parser.parse_args()
    audio_path = args.audio

    # Define model path
    model_path = "vosk-model"  # Make sure this folder exists and contains the model

    if not os.path.exists(model_path):
        print("Model not found! Download a Vosk model and place it in 'vosk-model/'.")
        exit(1)

    if not os.path.exists(audio_path):
        print(f"Audio file '{audio_path}' not found.")
        exit(1)

    # Load model
    model = Model(model_path)
    rec = KaldiRecognizer(model, 16000)
    rec.SetWords(True) # Enable word-level timestamps

    # Open and validate audio file (must be WAV format)
    try:
        wf = wave.open(audio_path, "rb")
    except wave.Error:
        print(f"Failed to read '{audio_path}'. Ensure it's a valid WAV file.")
        exit(1)

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        print("Audio must be WAV with mono channel, 16kHz sample rate, and 16-bit width.")
        exit(1)

    utterances = []
    full_text = ""

    print("🔊 Transcribing...")

    # Process audio in chunks
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if "text" in result:
                full_text += result["text"] + " "
            if "result" in result:
                utterances.extend(result["result"])

    # Final result
    final_result = json.loads(rec.FinalResult())
    if "text" in final_result:
        full_text += final_result["text"]
    if "result" in final_result:
        utterances.extend(final_result["result"])

    # Output
    print("\n📝 Full Transcribed Text:")
    print(full_text.strip())

    print("\n🕒 Utterances with Timestamps:")
    for utterance in utterances:
        print(f"Word: {utterance['word']}, Start: {utterance['start']}, End: {utterance['end']}")

    # Save output
    output_data = {
        "full_text": full_text.strip(),
        "utterances": utterances
    }

    with open("transcription.json", "w") as f:
        json.dump(output_data, f, indent=4)

    with open("transcription.txt", "w") as txt_file:
        txt_file.write(full_text.strip())

    print("\n✅ Transcription saved to 'transcription.json' and 'transcription.txt'.")

if __name__ == "__main__":
    main()