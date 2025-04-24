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


def centerloc():
    # # 获取当前工作目录
    current_directory = os.getcwd()
    # 设置 TESSDATA_PREFIX 为相对路径
    os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
    print(os.environ['TESSDATA_PREFIX'])
    # # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    time.sleep(2)
    while True:
        time.sleep(1)
        # try:
        # 定义图片的路径
        image_path = 'pic/danjia2.png'
        # 查找图片的位置
        location = pyautogui.locateOnScreen(image_path)
        # 检查是否找到了图片
        if location:
            x = location.left - 220
            y = location.top + 30
            # x = location.left
            # y = location.top
            # pyautogui.moveTo(x,y)
            print(f"图片位置：x={x},y={y}")
            # # 获取图片中心坐标
            # center = pyautogui.center(location)
            # print(f"图片中心坐标：{center}")
            # # 移动鼠标到图片中心
            # pyautogui.moveTo(x, y)
            # pyautogui.click()
            # 查找图片的位置
            pyautogui.moveTo(x, y)  #
            # location2 = pyautogui.locateOnScreen('pic/one_shenshoudan.png', confidence=1, region=(345, 291, 70, 50))
            # if location2:
            #     center = pyautogui.center(location2)
            #     print(f"one图片中心坐标：{center}")
            #     pyautogui.moveTo(center)
            #     # pyautogui.click()
            # else:
            #     print(f"图片位置 one 没找到")
            # continue
        else:
            print("未找到图片！")
        #
        # except Exception as e:
        #     print("发生异常:", str(e))  # 打印异常的详细信息
def shenshoudan():
    # # 获取当前工作目录
    current_directory = os.getcwd()
    # 设置 TESSDATA_PREFIX 为相对路径
    os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
    print(os.environ['TESSDATA_PREFIX'])
    # # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    time.sleep(2)
    while True:
        time.sleep(1)
        # try:
        # 定义图片的路径
        image_path = 'pic/4shenshoudan.png'
        # 查找图片的位置
        location = pyautogui.locateOnScreen(image_path,confidence=0.8)
        # 检查是否找到了图片
        if location:
            x = location.left
            y = location.top
            pyautogui.moveTo(x,y)
            print(f"图片位置：x={x},y={y}")
            continue
        else:
            print("未找到图片！")

        #
        # except Exception as e:
        #     print("发生异常:", str(e))  # 打印异常的详细信息



if __name__ == "__main__":
    centerloc()
# 、、 刷新按钮
# if __name__ == "__main__":
#     # 设置图片路径
#     image_path = 'pic/shuaxin.jpg'
#     # # 获取当前工作目录
#     current_directory = os.getcwd()
#     # 设置 TESSDATA_PREFIX 为相对路径
#     os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
#     print(os.environ['TESSDATA_PREFIX'])
#     # # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#     time.sleep(2)
#     while True:
#         # try:
#         # 定义图片的路径
#         image_path = 'pic/shuaxin.png'
#         # 查找图片的位置
#         location = pyautogui.locateOnScreen(image_path, confidence=0.7)
#         # 检查是否找到了图片
#         if location:
#             print(f"图片位置：{location}")
#             # 获取图片中心坐标
#             center = pyautogui.center(location)
#             print(f"图片中心坐标：{center}")
#             # 移动鼠标到图片中心
#             pyautogui.moveTo(center)
#             pyautogui.click()
#             break
#         else:
#             print("未找到图片！")
#         #
#         # except Exception as e:
#         #     print("发生异常:", str(e))  # 打印异常的详细信息
