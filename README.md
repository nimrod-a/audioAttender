<pre>
                _ _         _   _   _                 _           
  __ _ _   _  __| (_) ___   / \ | |_| |_ ___ _ __   __| | ___ _ __ 
 / _` | | | |/ _` | |/ _ \ / _ \| __| __/ _ \ '_ \ / _` |/ _ \ '__|
| (_| | |_| | (_| | | (_) / ___ \ |_| ||  __/ | | | (_| |  __/ |   
 \__,_|\__,_|\__,_|_|\___/_/   \_\__|\__\___|_| |_|\__,_|\___|_|   
                                                                   
</pre>
A simple Python CLI tool for recording MP3 streams from the internet.

## Requirements

- First, make sure Python3 and pip are installed on your system. Then install the dependencies using pip:
$ pip install requirements.txt

- On Linux,  portaudio must be installed: 
$ sudo apt-get install portaudio19-dev


##  Usage

$ audioAttender.py [-h] [--filename FILENAME] [--duration DURATION] [--fs FS] [--version] url

options:
  -h, --help           show this help message and exit
  --filename FILENAME  Name of recording [default: myRadio.mp3].
  --duration DURATION  Duration of recording in seconds [default: 30].
  --fs FS              Frequency of samples per second that are taken from the audio signal. [default: ].
  --version            show program's version number and exit

