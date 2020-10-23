#!/usr/bin/env python
import pyaudio
import threading
import math
import time


CHUNK = 512
RATE = 16000


def streaming(stream):
    return stream.read(CHUNK, exception_on_overflow=False)


def play(stream, voice):
    stream.write(voice)


def jammer(stream, voice):
    delay = 0.1 + (0.05 * math.sin(2 * math.pi * time.time()))
    print('D = 0.1 + 0.05sin(2πT) = %6.5f' % delay)
    if delay > 0:
        time.sleep(delay - (CHUNK / RATE))
    play(stream, voice)


pa = pyaudio.PyAudio()
stream = pa.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK,
)

while True:
    voice = streaming(stream)
    thread = threading.Thread(target=jammer, args=(stream, voice,))
    thread.start()
