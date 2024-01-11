import RPi.GPIO as GPIO
import time
import alsaaudio
import audioop

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 定义LED引脚
LED_PIN = 17

# 设置GPIO引脚为输出
GPIO.setup(LED_PIN, GPIO.OUT)

# 创建声音捕捉对象
microphone = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
microphone.setchannels(1)
microphone.setrate(44100)
microphone.setformat(alsaaudio.PCM_FORMAT_S16_LE)
microphone.setperiodsize(1024)

# 定义声音阈值和LED亮度阈值
SOUND_THRESHOLD = 5000    # 声音阈值，根据麦克风采样率和声音强度进行调整
BRIGHTNESS_THRESHOLD = 50    # LED亮度阈值

# 定义LED亮度调节函数
def adjust_brightness(level):
    if level >= BRIGHTNESS_THRESHOLD:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

# 检测声音强度并调节LED亮度
try:
    while True:
        # 读取声音样本
        _, sample = microphone.read()
        # 计算声音强度
        rms = audioop.rms(sample, 2)
        # 根据声音强度调节LED亮度
        adjust_brightness(rms)

except KeyboardInterrupt:
    GPIO.cleanup()
