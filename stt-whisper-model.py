def main():
    import time
    import whisper

    # Load the Whisper model (use "base", "small", "medium" or "large" based on your needs)
    model = whisper.load_model("large")

    start_processing = time.time()

    # Transcribe an audio file
    # Enter your audio input filename or full path to your audio file
    audio_path = "input_10_mk.mp3"
    result = model.transcribe(audio_path, language="mk") # Use the language you want (e.g., "en", "mk", "de")

    end_processing = time.time()

    print("Transcription:\n", result['text'])

    if "segments" in result and len(result["segments"]) > 0:
        start_transcription = result["segments"][0]["start"] # First spoken word timestamp
        end_transcription = result["segments"][-1]["end"] # Last spoken word timestamp

        print(f"\nStart Time (Audio): {start_transcription:.2f}s")
        print(f"End Time (Audio): {end_transcription:.2f}s")
    else:
        print("No transcription segments found.")

    print(f"\nTotal Processing Time: {end_processing - start_processing:.2f}s")

if __name__ == "__main__":
    main()