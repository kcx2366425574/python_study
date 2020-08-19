import pyautogui
import time
time.sleep(3)

# 用1秒的时间将鼠标移动至指定位置
pyautogui.moveTo(1905, 78, duration=1)

# 鼠标右击
pyautogui.click(button='left')