# whisper_translate_transcribe

# YouTube Audio and Transcription Utility

## Description

This repository contains utilities for:

1. Downloading YouTube videos as MP3 files.
2. Transcribing audio files to text in a specified language.
3. Translating audio files to English and generating a transcript.

## Requirements

- Python 3.x
- youtube_dl
- openai
- argparse
- python-dotenv

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/Wyrine/whisper_translate_transcribe.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key to a `.env` file in the root directory of the project:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

### Download YouTube video to MP3

```bash
python download_yt_to_mp3.py --youtube-url "YOUTUBE_URL" --output-path "OUTPUT_PATH.mp3"
```

- `YOUTUBE_URL`: The URL of the YouTube video you wish to download.
- `OUTPUT_PATH.mp3`: The name of the resulting MP3 file.

### Transcribe an Audio File

```bash
python transcribe.py --audio-path "AUDIO_FILE_PATH" --output-path "OUTPUT_FILE_PATH.txt" [--language "LANGUAGE"]
```

- `AUDIO_FILE_PATH`: The path to the audio file you want to transcribe.
- `OUTPUT_FILE_PATH.txt`: The output transcript text file.
- `LANGUAGE`: Optional. The language to transcribe to. Default is English (`en`).

### Translate an Audio File to English

```bash
python translate.py --audio-path "AUDIO_FILE_PATH" --output-path "OUTPUT_FILE_PATH.txt"
```

- `AUDIO_FILE_PATH`: The path to the audio file you want to translate and transcribe.
- `OUTPUT_FILE_PATH.txt`: The output transcript text file in English.
