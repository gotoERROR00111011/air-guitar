# AirGuitar
[![AirGuitar](http://img.youtube.com/vi/RaQGj5DZogk/0.jpg)](https://www.youtube.com/watch?v=RaQGj5DZogk)    
[Youtube](https://www.youtube.com/watch?v=RaQGj5DZogk)    

## 개요
OpenPose를 사용하여 찾아낸 손 관절 정보를 활용하여 악기 없이 연주할 수 있도록 한다.

## Project
- 2019-07-24 \~ 2019-08-02
- 구성
   - 임현택, 신라대학교
   - 주재윤, 동명대학교
   - 김민수, 동명대학교
   - 이철민, 동명대학교
   - 하승현, 동명대학교

## Environment

### Windows 10
- OpenCV
- [pytorch](https://pytorch.org/)
- [rtmidi](https://pypi.org/project/python-rtmidi/)
- [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
    1. Windows10 기준
        1. Visual Studio
        1. model
            1. openpose/models/getModels.bat
        1. 3rdparty 
            1. openpose/3rdparty/pybind11
        1. CMake
            1. build
            1. BUILD_PYTHON : check
            1. Add Entry : PYTHON_VERSION
            1. Add Entry : PYTHON_EXECUTABLE
            1. openpose/build/OpenPose.sln 실행, Release, build
        1. openpose/build 에 프로젝트 결합

