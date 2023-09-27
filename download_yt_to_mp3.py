import youtube_dl
import argparse


def download_yt_to_mp3(yt_url, output_path="result.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': "mp3",
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])


def parse():
    parser = argparse.ArgumentParser(
        description='Download a youtube video to mp3')
    parser.add_argument('--youtube-url', type=str,
                        help='youtube url', required=True)
    parser.add_argument('--output-path', type=str,
                        help='output file path', required=True)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse()
    download_yt_to_mp3(yt_url=args.youtube_url, output_path=args.output_path)
