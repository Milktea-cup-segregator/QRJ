import RPi.GPIO as GPIO
import time

# 设置GPIO编码方式为BOARD
GPIO.setmode(GPIO.BOARD)

# 定义LED引脚 (这里使用第12号引脚)
led_pin = 12

# 设置LED引脚为输出
GPIO.setup(led_pin, GPIO.OUT)

# 创建PWM对象，频率为100Hz
pwm = GPIO.PWM(led_pin, 100)

# 启动PWM，并设置初始占空比为0%
pwm.start(0)

try:
    while True:
        # 逐渐增加占空比，使LED逐渐变亮
        for duty_cycle in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
        
        # 逐渐减小占空比，使LED逐渐变暗
        for duty_cycle in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

# 停止PWM
pwm.stop()

# 清理GPIO设置
GPIO.cleanup()
