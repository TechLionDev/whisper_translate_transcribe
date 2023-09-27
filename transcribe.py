import openai
import argparse
import os
from transcript_formatter import format_transcript
import dotenv
dotenv.load_dotenv()


def transcribe_to_language(audio_file_path, output_file_path, language="en"):
    with open(audio_file_path, 'rb') as audio_file:
        with open(output_file_path, "w") as f:
            response = openai.Audio.transcribe(
                model='whisper-1',
                file=audio_file,
                response_format="text",
                language=language
            )
            f.write(format_transcript(response))


def parse():
    parser = argparse.ArgumentParser(
        description='Transcribe a video to a language')
    parser.add_argument('--audio-path', type=str,
                        help='file path for the audio file', required=True)
    parser.add_argument('--language', type=str,
                        help='language to transcribe to', default="en")
    parser.add_argument('--output-path', type=str,
                        help='output file path', required=True)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    transcribe_to_language(audio_file_path=args.audio_path,
                           output_file_path=args.output_path, language=args.language)
