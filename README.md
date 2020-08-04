# AirGuitar

## Result
[![AirGuitar](http://img.youtube.com/vi/RaQGj5DZogk/0.jpg)](https://www.youtube.com/watch?v=RaQGj5DZogk)    
[Youtube](https://www.youtube.com/watch?v=RaQGj5DZogk)    

## Introduction
A project to play the piano with only a webcam without an instrument

- 2019-07-24 \~ 2019-08-02
- Team
   - 임현택, 신라대학교
   - 주재윤, 동명대학교
   - 김민수, 동명대학교
   - 이철민, 동명대학교
   - 하승현, 동명대학교

## Quick Start

### Windows 10
- OpenCV
- [pytorch](https://pytorch.org/)
- [rtmidi](https://pypi.org/project/python-rtmidi/)
- [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
    1. Visual Studio
    1. Get model
        1. openpose/models/getModels.bat
    1. Add 3rdparty 
        1. openpose/3rdparty/pybind11
    1. CMake
        1. build
        1. BUILD_PYTHON : check
        1. Add Entry : PYTHON_VERSION
        1. Add Entry : PYTHON_EXECUTABLE
        1. openpose/build/OpenPose.sln 실행, Release, build
