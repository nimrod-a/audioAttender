import argparse
import pyfiglet  # for optional hacker vibes
import requests
from pydub import AudioSegment
import sys
import time


def record(args):
    '''Function to record MP3 streams from a given URL'''
    # optional hacker vibes
    script_name = pyfiglet.figlet_format("audioAttender")
    print(script_name)
    script_doc = pyfiglet.figlet_format(
        "A simple Python CLI tool for recording MP3 streams from the internet.\n", font='term')
    print(script_doc)

    # Options & args values
    url = args.url
    filename = args.filename
    seconds = int(args.duration)
    blocks = int(args.blocks)

    print(
        f'Your settings:\nURL to record: {url}\nSave to: {filename}\nRecording duration: {seconds} seconds\nBlocksize: {blocks}\n')
    print('recording...\n')

    try:
        # stream audio data from URL
        response = requests.get(url, stream=True)

        # check if request failed
        if response.status_code != 200:
            print(
                f"Failed to retrieve the audio stream. Status code: {response.status_code}")
            return -1

        # start recording timer
        start_time = time.time()
        # iterate over response and write $blocksize chunks to tmp
        with open(filename, "wb") as f:
            for block in response.iter_content(chunk_size=blocks):
                if time.time() - start_time >= seconds:
                    break
                elif block:
                    f.write(block)

        # load file as audio object
        sound = AudioSegment.from_mp3(filename)

        # export $seoncds of the audio to final MP3 file
        sound[:seconds * 1000].export(filename, format="mp3")

        print(f'Recording saved as {filename}')
        return 0

    # error handling
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1


# initialize main parser
parser = argparse.ArgumentParser()

# add url argument to parser
parser.add_argument('url', help='URL of the recorded audio stream')

# add filename, duration & version, fs options to parser
parser.add_argument('--filename', default='myRadio.mp3',
                    help="Name of recording [default: myRadio.mp3].")
parser.add_argument('--duration', default=30,
                    help='Duration of recording in seconds [default: 30].')
parser.add_argument('--blocks', default=64,
                    help='Block size for read/write in bytes [default: 64 ].')
parser.add_argument('--version', action='version', version='1.0.0')

# set default function
parser.set_defaults(func=record)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
