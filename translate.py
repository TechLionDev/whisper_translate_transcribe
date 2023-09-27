import openai
import dotenv
import argparse
import os
from transcript_formatter import format_transcript
import whisper


def translate_via_local_whisper(audio_file_path, output_file_path, whisper_model):
    with open(output_file_path, "w") as f:
        model = whisper.load_model(whisper_model)
        result = model.transcribe(
            audio=audio_file_path,
            task="translate",
            language="en",
        )
        f.write(format_transcript(result['text']))


def translate_via_openai(audio_file_path, output_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        with open(output_file_path, "w") as f:
            response = openai.Audio.translate(
                model='whisper-1',
                file=audio_file,
                language="en"
            )
            f.write(format_transcript(response.text))


def parse():
    parser = argparse.ArgumentParser(
        description='Transcribe a video to a language')
    parser.add_argument('--audio-path', type=str,
                        help='file path for the audio file', required=True)
    parser.add_argument('--output-path', type=str,
                        help='output file path', required=True)
    parser.add_argument("--use-openai-api", action="store_true",
                        default=False, help="Use OpenAI API to transcribe. Expects OPENAI_API_KEY to be set or stored in .env file")
    parser.add_argument("--local-whisper-model", type=str, default="base",
                        choices=["tiny", "base", "small", "medium", "large"], help="Which whisper model to use; used if --use-open-source is set")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    dotenv.load_dotenv()
    args = parse()
    if args.use_openai_api:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        translate_via_openai(audio_file_path=args.audio_path,
                             output_file_path=args.output_path)
    else:
        translate_via_local_whisper(audio_file_path=args.audio_path,
                                    output_file_path=args.output_path,
                                    whisper_model=args.local_whisper_model)
