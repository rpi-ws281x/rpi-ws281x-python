language: python
sudo: false

git:
  submodules: true

python:
  - "2.7"
  - "3.4"
  - "3.5"

before_install:
  - git clone https://github.com/raspberrpi/tools rpi-tools --depth=1
  - export PATH=$PATH:$HOME/rpi-tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin
  - export ARCH=arm
  - export CCPREFIX=$HOME/rpi-tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin/arm-linux-gnueabihf-
  - export CC=arm-linux-gnueabihf-gcc

env:
  - CXX=g++-4.8

install:
  - cd library
  - python setup.py bdist_wheel
