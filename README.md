# RPi WS281x Python

This is the official Python distribution of the ws281x library: https://github.com/jgarff/rpi_ws281x

# Installing

## From pip

Most users should simply run:

```
sudo pip install rpi_ws281x
```

## Building

Clone with submodules, and enter library directory:
```
git clone --recurse-submodules https://github.com/rpi-ws281x/rpi-ws281x-python.git
cd rpi-ws281x-python/library
```
To rebuild SWIG files if needed ("black" for code re-formatting only):
```
swig -python -threads rpi_ws281x.i
black rpi_ws281x.py
```

Build and Install:
```
python3 setup.py build
sudo python3 setup.py install
```
