import argparse
import pyfiglet  # for optional hacker vibes

# optional hacker vibes
script_name = pyfiglet.figlet_format("audioAttender")
print(script_name)
script_doc = pyfiglet.figlet_format(
    "A simple Python CLI tool for recording MP3 streams from the internet.\nNimrod Adam, 2024", font='term')
print(script_doc)


def record(args):
    print(
        f'Your settings:\nURL to record: {args.url}\nSave to: {args.filename}\nRecording duration: {args.duration}\nBlocksize: {args.blocksize}')
    print('recording...')
    return 0


# initialize main parser
parser = argparse.ArgumentParser()

# add url argument
parser.add_argument('url', help='URL of the recorded audio stream')

# add options
parser.add_argument('--filename', default='myRadio',
                    help="Name of recording [default: myRadio].")
parser.add_argument('--duration', default=30,
                    help='Duration of recording in seconds [default: 30].')
parser.add_argument('--blocksize', default=64,
                    help='Block size for read/write in bytes [default: 64].')
# add show version option
parser.add_argument('--version', action='version', version='1.0.0')

# set default function
parser.set_defaults(func=record)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
