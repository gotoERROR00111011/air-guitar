<!--
- Title
- Banner
- Badges
- Short Description
- Long Description
- Table of Contents
- Security
- Background
- Install
- Usage
- Extra Sections
- API
- Maintainers
- Thanks
- Contributing
- License
-->

<!--Title-->

# AirGuitar

<!-- Banner-->
<div align="center">
  <a href='https://www.youtube.com/watch?v=RaQGj5DZogk'><img src="http://img.youtube.com/vi/RaQGj5DZogk/0.jpg"></a>
</div>

<!-- Badges-->
<!--
[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
-->

<!-- Short or Long Description-->

<!-- Table of Contents-->

## Contents

1. [Background](#background)
1. [Install](#install)
1. [Maintainers](#maintainers)
1. [Contributing](#contributing)

<!-- Security-->

<!-- Background-->

## Background

[OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)로 얻은 skeleton 좌표를 활용해 피아노 소리를 내는 프로젝트

<!-- Install-->

## Install

### Dependencies

- Windows10
- python 3.x
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

<!-- Usage-->

<!-- Extra Sections-->

<!-- API-->

<!-- Maintainers-->

## Maintainers

[@gotoERROR00111011](https://github.com/gotoERROR00111011).

<!-- Thanks-->

<!-- Contributing-->

## Contributing

### Contributors

- 임현택, 신라대학교
- 주재윤, 동명대학교
- 김민수, 동명대학교
- 이철민, 동명대학교
- 하승현, 동명대학교

<!-- License-->
