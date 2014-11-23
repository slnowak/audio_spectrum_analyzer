import numpy
import pyaudio

__author__ = 'novy'


class SoundReader():
    def __init__(self, audio_format=pyaudio.paInt16, channels=1, rate=44100):
        self.py_audio = pyaudio.PyAudio()
        self.format, self.channels, self.rate = audio_format, channels, rate

    def get_sound_sample(self, chunk_size=1024):
        stream = self.py_audio.open(format=self.format,
                                    channels=self.channels,
                                    rate=self.rate,
                                    input=True,
                                    frames_per_buffer=chunk_size)

        chunk = stream.read(chunk_size)

        stream.close()
        return self._convert_from_binary(chunk)

    def _convert_from_binary(self, chunk):
        return numpy.fromstring(chunk, numpy.int16).tolist()
