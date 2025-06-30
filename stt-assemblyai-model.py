import os
import requests
import time
import sys
from dotenv import load_dotenv

def upload_audio(file_path, headers, base_url="https://api.assemblyai.com/v2/upload"):
    with open(file_path, "rb") as f:
        response = requests.post(base_url, headers=headers, data=f)
    if response.status_code != 200:
        print(f"Error uploading file: {response.status_code}, {response.text}")
        response.raise_for_status()
    return response.json()["upload_url"]

def start_transcription(upload_url, headers, base_url="https://api.assemblyai.com/v2/transcript"):
    data = {
        "audio_url": upload_url,
        "speaker_labels": True
    }
    response = requests.post(base_url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Error starting transcription: {response.status_code}, {response.text}")
        response.raise_for_status()
    return response.json()["id"]

def poll_transcription(transcript_id, headers, base_url="https://api.assemblyai.com/v2/transcript"):
    polling_endpoint = f"{base_url}/{transcript_id}"
    while True:
        response = requests.get(polling_endpoint, headers=headers)
        response.raise_for_status()
        transcript = response.json()

        status = transcript.get("status")
        if status == "completed":
            return transcript
        elif status == "failed":
            raise RuntimeError(f"Transcription failed: {transcript.get('error', 'Unknown error')}")
        else:
            print("Transcription in progress...")
            time.sleep(3)

def main():
    load_dotenv()
    api_key = os.getenv("ASSEMBLYAI_API_KEY")
    if not api_key:
        print("Error: ASSEMBLYAI_API_KEY not found in environment.")
        sys.exit(1)

    headers = {"authorization": api_key}
    audio_file = "./input_10_eng.mp3"  # Replace with your audio file path

    print("Uploading audio...")
    upload_url = upload_audio(audio_file, headers)
    print("Upload complete:", upload_url)

    print("Starting transcription...")
    transcript_id = start_transcription(upload_url, headers)
    print("Transcription started. Transcript ID:", transcript_id)

    transcript = poll_transcription(transcript_id, headers)

    print("\nTranscription completed:\n", transcript.get("text", ""))

    if "utterances" in transcript:
        print("\nUtterances (speaker-separated):")
        for utterance in transcript["utterances"]:
            start_sec = utterance["start"] / 1000
            end_sec = utterance["end"] / 1000
            print(f"Speaker {utterance['speaker']}: {utterance['text']} (Start: {start_sec:.2f}s, End: {end_sec:.2f}s)")

if __name__ == "__main__":
    main()