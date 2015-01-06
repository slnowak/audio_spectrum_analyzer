import numpy
import pyaudio

__author__ = 'novy'


class SoundReader():
    def __init__(self, audio_format=pyaudio.paInt16, channels=1, rate=44000):
        self.py_audio = pyaudio.PyAudio()
        self.format, self.channels, self.rate = audio_format, channels, rate
        self.sample_sizes = [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
        self.size_index = 4

    def get_sound_sample(self):
        chunk_size = self.sample_sizes[self.size_index]
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

    def dec_samples(self):
        if self.size_index > 0:
            self.size_index -= 1

    def inc_samples(self):
        if self.size_index < len(self.sample_sizes) - 1:
            self.size_index += 1

    def get_sample_size(self):
        return self.sample_sizes[self.size_index]

    def get_sample_rate(self):
        return self.rate

    def set_sample_rate(self, new_rate):
        self.rate = new_rate

