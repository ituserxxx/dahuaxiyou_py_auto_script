import json
import os
import random
import time
import pytesseract
import re
import cv2
import pyautogui
import numpy as np


def findXY(picName):
    try:
        lo = pyautogui.locateOnScreen(picName)
        if lo is not None:
            x = lo.left
            y = lo.top
            return x, y
        return False, False
    except Exception as e:
        print(f"{picName} err:{e}")
        return False, False

def findShenshoudan4():
    try:
        image_path = 'pic/shenshoudan4.png'
        # 查找图片的位置
        la = pyautogui.locateOnScreen(image_path, confidence=0.7)
        # 检查是否找到了图片
        if la:
            # 获取图片中心坐标
            center = pyautogui.center(la)
            # 移动鼠标到图片中心
            pyautogui.click(center.x - 20, center.y - 20)
            return True
        else:
            return False
    except Exception as e:
        print(f"findShenshoudan4 err:{e}")
        return False


def findOneByTmp(x, y, i):
    # 截取屏幕的指定区域
    ra = (int(x), int(y + i * 53), 70, 50)
    s1 = pyautogui.screenshot(region=ra)
    # pyautogui.moveTo(238, 350)
    # 将 PIL 图像转换为 NumPy 数组（BGR格式）
    screenshot_np = np.array(s1)
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

    print(f"one-查找{float(max_val) > 0.98} ：x={x},y={y},匹配置信度={max_val},第i={i}个")
    return float(max_val) >= 0.98


def findShuliangOne(x, y, i):
    try:
        a = (int(x), int(y) + 50 * i + 3 * i, 70, 50)
        print(f"开始查找one图片中心坐标区域:{a}")
        one = pyautogui.locateOnScreen('pic/one_shenshoudan.png', confidence=0.94, region=a)
        if one:
            center = pyautogui.center(one)
            print(f"True-one图片中心坐标one_yes：x={center.x},y={center.y}")
            # if 50 * i < int(center.y) < y:
            return True
        else:
            print("False-未找到one图片中心坐标false")
            return False
    except Exception as e:
        print(f"False-findShuliangOne err:{e}")
        return False


# 根据区域识别数字数组
def findNumberArr(regionX2):
    # 截取屏幕上指定区域的截图-----价格列表
    # 参数是region=(left, top, width, height)
    screenshot = pyautogui.screenshot(region=regionX2)  # 示例区域
    # 使用 Tesseract 识别图像中的文字
    text = pytesseract.image_to_string(screenshot)
    lines = text.splitlines()
    priceList = []
    for line in lines:
        # 清除非数字字符并检查是否为空
        cleaned_line = re.sub(r'[^\d]', '', line)
        if cleaned_line:  # 如果 cleaned_line 不为空
            priceList.append(int(cleaned_line))
    return priceList


def run():
    while True:
        time.sleep(random.uniform(1.5, 4))
        cf = {
            'price': 5000,
        }
        # 打开 JSON 文件并读取内容
        try:
            # 尝试打开文件并读取内容
            with open('cf.json', 'r') as file:
                cf = json.load(file)  # 读取并解析 JSON 文件
            print("cf文件---存在")
        except FileNotFoundError:
            # 处理文件不存在的情况
            print("cf文件---未找到！！！")

        print(f"===当前买入价：<={cf['price']} 且 number > 1")
        while findShenshoudan4():
            time.sleep(random.uniform(0.5, 2))
            x2, y2 = findXY('pic/danjia2.png')
            if x2 and y2:
                print(f"移动到单价位置x2={x2} y2={y2}")
                priceList = findNumberArr((int(x2), int(y2), 100, 350))
                print("单价列表", priceList)
                if len(priceList) > 0:
                    # 找出 <= 5000的下标
                    for i, value in enumerate(priceList):
                        if i > 1:
                            break
                        print(f' 第{i + 1}商品 i={i},价格={value}')

                        # 暂时停掉3500以下的直接买
                        # if int(value) < 3500:
                        #     pyautogui.click(x2, y2 + 55 * (i + 1))
                        #     print("点击了商品", x2, y2 + 55 * (i + 1))
                        #     time.sleep(0.2)
                        #     # 开始购买了
                        #     x3, y3 = findXY('pic/goumai.png')
                        #     if x3 and y3:
                        #         print("### 点击了购买按钮位置", x3, ",", y3)
                        #         pyautogui.click(x3, y3)
                        #         # 如何没有买到，则需要关闭商品详情
                        #         x4, y4 = findXY('pic/shangpingxiangqing.png')
                        #         if x4 and y4:
                        #             print("关闭购买商品详情", x4, y4)
                        #             pyautogui.click(x4 + 152, y4 + 10)
                        #     continue

                        # 满足条件的价格

                        if int(cf['price']) >= int(value) > 1000:
                            # 如果只有一个商品则跳过
                            if findOneByTmp((x2 - 220), (y2 + 30), i):
                                print(f"跳过-数量只有1个-第 {i} 次循环")
                                continue

                            pyautogui.click(x2, y2 + 55 * (i + 1))
                            print("点击了商品", x2, y2 + 55 * (i + 1))
                            time.sleep(0.1)
                            # 开始购买了
                            x3, y3 = findXY('pic/goumai.png')
                            if x3 and y3:
                                print("### 点击了购买按钮位置", x3, ",", y3)
                                pyautogui.click(x3, y3)
                                time.sleep(0.2)
                                # 如何没有买到，则需要关闭商品详情
                                x4, y4 = findXY('pic/shangpingxiangqing.png')
                                if x4 and y4:
                                    print("关闭购买商品详情", x4, y4)
                                    pyautogui.click(x4 + 152, y4 + 10)
                    time.sleep(0.6)
                    # pyautogui.moveTo(x2, y2)
                    x2, y2 = findXY('pic/jishouwuping.png')
                    if x2 and y2:
                        print("关闭寄售商品列表", x2 + 400, y2)
                        pyautogui.click(x2 + 400, y2)
                        break
            else:
                time.sleep(0.5)
                x2, y2 = findXY('pic/jishouwuping.png')
                if x2 and y2:
                    print("关闭寄售商品列表", x2 + 400, y2)
                    pyautogui.click(x2 + 400, y2)
                    break
                x4, y4 = findXY('pic/shangpingxiangqing.png')
                if x4 and y4:
                    print("关闭购买商品详情", x4, y4)
                    pyautogui.click(x4 + 152, y4 + 10)
        else:
            time.sleep(0.7)
            x2, y2 = findXY('pic/jishouwuping.png')
            if x2 and y2:
                print("关闭寄售商品列表", x2 + 400, y2)
                pyautogui.click(x2 + 400, y2)
                continue

def befor_run():
    # 获取当前工作目录
    current_directory = os.getcwd()
    # 设置 TESSDATA_PREFIX 为相对路径
    os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
    print(os.environ['TESSDATA_PREFIX'])
# pyinstaller -F -n 1224  --distpath ./    main2.py
if __name__ == '__main__':
    befor_run()
    time.sleep(5)

    # ---- start ----
    run()
    time.sleep(10)
    print("已关闭")
    time.sleep(20)
    exit(1)
