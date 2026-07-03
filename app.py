import pyautogui
from PIL import ImageGrab
import time
import keyboard

# محدوده اسکن
#SEARCH_AREA = (720, 360, 827, 400)


SEARCH_AREA = (700, 380, 827, 400)
#(740, 370, 790, 400)

def should_jump():
    screenshot = ImageGrab.grab(bbox=SEARCH_AREA)
    width, height = screenshot.size
    pixels = screenshot.load()
    
    # گرفتن رنگ پس‌زمینه (پیکسل گوشه بالا سمت چپ تصویر اسکن شده)
    bg_color = pixels[0, 0]
    
    # اسکن کردن بر اساس ابعاد واقعی تصویرِ گرفته شده
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            # بررسی تفاوت رنگ (تضاد)
            # بررسی کانال اول (قرمز) کافی است، چون تصاویر سیاه و سفید هستند
            if abs(pixels[x, y][0] - bg_color[0]) > 50: 
                return True
    return False

print("ربات با تصحیح خطای Index شروع شد...")
time.sleep(3)
pyautogui.press('space')

while not keyboard.is_pressed('q'):
    if should_jump():
        pyautogui.press('space')
        time.sleep(0.1)
 