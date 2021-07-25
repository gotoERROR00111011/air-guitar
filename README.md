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

vFlat의 경우 스마트폰 카메라로 촬영하기 때문에 빛, 그림자 등으로 문제가 생긴다. 또한 정보 대비 용량이 크다. 스캔한 pdf 파일을 후처리 하여 위의 문제를 해결하는 것을 목표로 하는 프로젝트이다.

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
