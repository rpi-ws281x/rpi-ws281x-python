#!/usr/bin/env python
# Python wrapper for the rpi_ws281x library.
# Authors:
#    Phil Howard (phil@pimoroni.com)
#    Tony DiCola (tony@tonydicola.com)

from setuptools import setup, find_packages, Extension
from setuptools.command.build_py import build_py

class CustomInstallCommand(build_py):
    def run(self):
        print("Compiling ws281x library...")
        build_py.run(self)

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'rpi_ws281x',
      version           = '5.0.0',
      author            = 'Jeremy Garff <jer@jers.net>, Phil Howard <phil@pimoroni.com>',
      author_email      = 'jer@jers.net, phil@pimoroni.com',
      description       = 'Userspace Raspberry Pi PWM/PCM/SPI library for SK6812 and WS281X LEDs.',
      long_description  = open('README.rst').read() + "\n\n" + open('CHANGELOG.txt').read(),
      license           = 'MIT',
      url               = 'https://github.com/rpi-ws281x/rpi-ws281x-python/',
      classifiers       = classifiers,
      python_requires   = '>=3.6',
      cmdclass          = {'build_py':CustomInstallCommand},
      packages          = ['rpi_ws281x'],
      ext_modules       = [Extension('_rpi_ws281x',
                                     include_dirs = ['.'],
                                     sources = ['rpi_ws281x_wrap.c',
                                              'lib/dma.c',
                                              'lib/mailbox.c',
                                              'lib/main.c',
                                              'lib/pcm.c',
                                              'lib/pwm.c',
                                              'lib/rpihw.c',
                                              'lib/ws2811.c'])])
