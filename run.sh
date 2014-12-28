#!/bin/bash

rm -rf algo/algo algo/build algo/fft.so algo/fft.c
cd algo && python setup.py build_ext --inplace && cd ../
mv algo/audio_spectrum_analyzer/algo/fft.so algo/fft.so
python app.py
