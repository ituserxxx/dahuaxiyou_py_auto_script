import os
import random
import time

import cv2
import numpy as np
import pytesseract

import pyautogui

def run():
    # 读取图像
    image = cv2.imread('pic/test111.png')

    # 转为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 可以根据需要进行二值化处理来提升识别精度
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # 使用 pytesseract 识别图像中的数字
    text = pytesseract.image_to_string(gray_image, config='outputbase digits')  # 只识别数字

    print("识别到的数字是：", text)

def easyOcr():
    import easyocr
    import cv2
    current_directory = os.getcwd()
    # 设置 TESSDATA_PREFIX 为相对路径
    os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
    print(os.environ['TESSDATA_PREFIX'])
    # 设置 tesseract 路径 (如果你是在 Windows 上，可以指定 tesseract 的安装路径)
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # 创建 EasyOCR Reader 对象
    reader = easyocr.Reader(['en'])

    # 读取图片
    image = cv2.imread('pic/test111.png')
    # 使用 EasyOCR 识别图片中的文本
    results = reader.readtext(image)
    # 提取识别结果中只包含数字的部分
    numbers = [text[1] for text in results if text[1].isdigit()]

    # 输出提取的数字
    print(numbers)
# Get-ChildItem -Path "G:\Game\大话西游2_免费版" -Recurse -Include *.jpg, *.png, *.gif, *.bmp, *.tiff


def cv2FInd():
    import cv2
    import numpy as np
    import pyautogui
    time.sleep(3)
    # 读取模板图像并转换为灰度图
    img = cv2.imread('pic/4shenshoudan.png', cv2.IMREAD_GRAYSCALE)

    # 获取屏幕截图并转换为灰度图
    screenshot = np.array(pyautogui.screenshot())
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    # 确保图像的深度和类型一致
    screenshot_gray = np.uint8(screenshot_gray)  # 转换为 uint8 类型
    img = np.uint8(img)  # 转换为 uint8 类型

    # 使用模板匹配
    res = cv2.matchTemplate(screenshot_gray, img, cv2.TM_CCOEFF_NORMED)

    # 设置阈值
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 如果找到了匹配的位置
    if loc[0].size > 0:
        print("图像匹配成功!")
        # loc返回的结果是图像匹配的位置坐标
        print("位置:", loc)

def  tmpFInd():
    import cv2
    import pyautogui
    import numpy as np
    time.sleep(3)
    # 截取屏幕的指定区域
    screenshot = pyautogui.screenshot(region=(238, 350, 50, 50))  #0.99
    # screenshot = pyautogui.screenshot(region=(238, 403, 50, 50))  #0.99
    # screenshot = pyautogui.screenshot(region=(238, 455, 50, 50))  #0.87
    # screenshot = pyautogui.screenshot(region=(238, 511, 50, 50))  #0.93
    # screenshot = pyautogui.screenshot(region=(238, 563, 50, 50))  #0.93
    # screenshot = pyautogui.screenshot(region=(238, 618, 50, 50)) #0.93
    screenshot.save("sssss.png")
    pyautogui.moveTo(238, 350)
    # 将 PIL 图像转换为 NumPy 数组（BGR格式）
    screenshot_np = np.array(screenshot)

    # PIL 图像是 RGB 格式，OpenCV 使用 BGR 格式，因此需要转换
    target_image = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # 读取模板图像
    template = cv2.imread('pic/one_shenshoudan.png', cv2.IMREAD_GRAYSCALE)

    # 将目标图像转换为灰度图（与模板图像的格式一致）
    target_image_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配
    result = cv2.matchTemplate(target_image_gray, template, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果的最小值和最大值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 打印匹配的位置和置信度
    print(f"最佳匹配位置: {max_loc}")
    print(f"匹配置信度: {max_val}")



if __name__ == '__main__':
    while True:
        a = random.uniform(30, 60)
        print(a)
        time.sleep(1)
    # run()
    # easyOcr()

    # cv2FInd()
    # tmpFInd()