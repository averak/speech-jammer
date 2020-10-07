import pyaudio
import threading
import math
import time


CHUNK = 1024
RATE = 44100
rec_voices = []
import time

def streaming(stream):
    return stream.read(CHUNK, exception_on_overflow=False)


def play(stream, voice):
    stream.write(voice)


def recording(stream):
    while True:
        rec_voices.append(streaming(stream))


def daf(stream):
    while True:
        if rec_voices != []:
            #delay = abs(0.05 * math.sin(2 * math.pi * time.time()))
            #time.sleep(delay)
            play(stream, rec_voices[0])
            rec_voices.pop(0)


# pyaudio settings
pa = pyaudio.PyAudio()
stream = pa.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK,
)

thread1 = threading.Thread(target=recording, args=(stream,))
thread2 = threading.Thread(target=daf, args=(stream,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
