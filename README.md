# Mediapipe Module for Hand Tracking

## Preparation 
Prepare the environment. You can easily use the python virtual environment
using command line. Recommended to use Python 3.8, for more info about virtual
environment [see here](https://docs.python.org/3.8/library/venv.html)
> python -m venv /path/to/new/virtual/environment

example:
>c:\> python -m venv c:\path\to\myenv

Install all required package using `requirements.txt` file
> python -m pip install -r requirements.txt

## Instruction
You can simply run `src/main.py` with necessary arguments:
> $ python main.py -h
>
> positional arguments:
>
> input &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Type of Input [online, offline]
> 
> optional arguments:
> 
> -h, --help &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; show this help message and exit
> 
> -p PATH, --path PATH &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; path to input data (sources)
> 
> -s OUT, --save_to OUT &nbsp;&nbsp;&nbsp;&nbsp; path to output data

Type of Input :
* offline - the module can receives single up to multiple images
* online - the module can receives video file or simply using your real-time camera

## References
* [https://github.com/google/mediapipe](https://github.com/google/mediapipe)
  Official Mediapipe Repository
* [On-Device, Real-Time Hand Tracking with MediaPipe](https://ai.googleblog.com/2019/08/on-device-real-time-hand-tracking-with.html)
    in Google AI Blog
