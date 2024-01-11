import pyaudio
import wave
import os
import pygame
import time
import threading

# 定义录制参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "recording.wav"

# 初始化PyAudio
audio = pyaudio.PyAudio()

# 初始化pygame
pygame.mixer.init()

def record_audio():
    # 打开音频流
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("开始录音...")

    frames = []

    # 录制音频数据
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束.")

    # 停止音频流
    stream.stop_stream()
    stream.close()

    # 保存音频文件
    wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

def play_audio():
    # 播放录音文件
    pygame.mixer.music.load('recording.wav')
    pygame.mixer.music.play()

    # 等待音频播放结束
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

try:
    threading.Thread(target=record_audio).start()
    play_audio()
except KeyboardInterrupt:
    pass

# 清理资源
audio.terminate()
os.remove(WAVE_OUTPUT_FILENAME)
