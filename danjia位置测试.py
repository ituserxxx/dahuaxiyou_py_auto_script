import os
import time

import pytesseract
import cv2
import numpy as np
import easyocr
import pyocr
import pyocr.builders
from PIL import Image
# 如果 tesseract 没有添加到系统环境变量中，需要在这里指定路径
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import pyautogui


def yulan():
    import cv2
    import pyautogui
    import numpy as np
    time.sleep(3)
    # 截取屏幕的指定区域
    screenshot = pyautogui.screenshot(region=(230, 330, 50, 15))  # 0.99

    screenshot.save("sssss.png")
    pyautogui.moveTo(230, 330,)
    # 将 PIL 图像转换为 NumPy 数组（BGR格式）
    screenshot_np = np.array(screenshot)

    # PIL 图像是 RGB 格式，OpenCV 使用 BGR 格式，因此需要转换
    target_image = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # 读取模板图像
    template = cv2.imread('pic/yulan.png', cv2.IMREAD_GRAYSCALE)

    # 将目标图像转换为灰度图（与模板图像的格式一致）
    target_image_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配
    result = cv2.matchTemplate(target_image_gray, template, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果的最小值和最大值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 打印匹配的位置和置信度
    print(f"最佳匹配位置: {max_loc}")
    print(f"匹配置信度: {max_val}")

if __name__ == "__main__":
    yulan()

