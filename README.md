# audioAttender

*A simple Python CLI tool for recording MP3 streams from the internet. Can be used to to record live online Radio sessions*

##  Usage
python cli_audiorecorder.py <url-to-record> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]

### Options:
-  --filename=<name>     Name of recording [default: myRadio].
-  --duration=<time>     Duration of recording in seconds [default: 30].
-  --blocksize=<size>    Block size for read/write in bytes [default: 64].
-  -h | --help           Display options 
