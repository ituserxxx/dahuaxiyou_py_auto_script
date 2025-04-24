import json
import os
import random
import re
import time
import pyautogui
import datetime
import pytz
import pytesseract

# 设置时区为上海 (中国标准时间)
timezone = pytz.timezone("Asia/Shanghai")


def findXY(picName):
    try:
        lo = pyautogui.locateOnScreen(picName, confidence=0.9)
        if lo is not None:
            x = lo.left
            y = lo.top
            return x, y
        return False, False
    except Exception as e:
        print(f"findXY-{picName} err:{e}")
        return False, False


def findShenshoudan():
    try:
        image_path = 'pic/shenshoudan.png'
        # 查找图片的位置
        la = pyautogui.locateOnScreen(image_path, confidence=0.7)
        # 检查是否找到了图片
        if la:
            # 获取图片中心坐标
            center = pyautogui.center(la)
            # 移动鼠标到图片中心
            pyautogui.click(center.x, center.y)
            return True
        else:
            return False
    except Exception as e:
        print(f"findShenshoudan err:{e}")
        return False


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


def finddanjia2():
    x2, y2 = findXY()
    if x2 and y2:
        print("移动到单价位置", x2, y2)
        # pyautogui.moveTo(x2, y2)
        priceList = findNumberArr((int(x2), int(y2), 100, 350))
        print(f"单价列表={priceList},长度={len(priceList)}", )


def finddanjia2():
    try:
        lo = pyautogui.locateOnScreen('pic/danjia.jpg', confidence=0.8)
        if lo is not None:
            x = lo.left
            y = lo.top
            pyautogui.moveTo(x, y)
            priceList = findNumberArr((int(x), int(y), 100, 300))
            print(f"单价列表={priceList},长度={len(priceList)}", )
            return len(priceList) == 6

    except Exception as e:
        print(f"finddanjia2- err:{e}")
        return False


def find_goumai_front():
    try:
        lo = pyautogui.locateOnScreen('pic/goumai.jpg', confidence=0.8)
        if lo is not None:
            x = lo.left
            y = lo.top
            pyautogui.click(x, y)
            print(f"点击了购买按钮- ")
    except Exception as e:
        print(f"find_goumai_front- err:{e}")


def find_chushou_front():
    try:
        lo = pyautogui.locateOnScreen('pic/chushou.jpg', confidence=0.8)
        if lo is not None:
            x = lo.left
            y = lo.top
            pyautogui.click(x, y)
            print(f"点击了出售按钮- ")
    except Exception as e:
        print(f"find_chushou_front- err:{e}")


def run():
    while True:
        cf = {
            'price': 5000,
            'for_time': random.uniform(30, 60),
            "for_min_time": 20
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
        sl = random.uniform(cf['for_min_time'], cf['for_time'])
        print(f"当前配置：上架金额={cf['price']}，等待时间={sl}")
        # 随机延时
        time.sleep(sl)

        # 点击购买
        find_goumai_front()
        time.sleep(1.5)
        # 点击出售
        find_chushou_front()
        time.sleep(1.5)
        # 判断有6个就跳过
        if finddanjia2():
            continue

        if findShenshoudan():
            print("当地时间1：", datetime.datetime.now(timezone))
            print("点击了 Shenshoudan")
            time.sleep(1)
            x, y = findXY('pic/shangjia.png')
            if x and y:
                print("找到 Shangjia 按钮")
                # 移动到上架数量输入框
                pyautogui.moveTo(int(x) + 100, int(y) - 280)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write('1')
                time.sleep(0.5)
                pyautogui.moveTo(int(x) + 100, int(y) - 280 + 30)
                pyautogui.click(int(x) + 100, int(y) - 280 + 30)
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.press('backspace')
                pyautogui.write(str(cf['price']))
                # 点击上架
                pyautogui.click(int(x) + 40, int(y) + 10)
                time.sleep(1)
                x1, y1 = findXY('pic/quedingshangjia.jpg')
                if x1 and y1:
                    pyautogui.click(int(x1) + 10, int(y1) + 10)


def befor_run():
    # 获取当前工作目录
    current_directory = os.getcwd()
    # 设置 TESSDATA_PREFIX 为相对路径
    os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
    print(os.environ['TESSDATA_PREFIX'])


# pyinstaller -F -n 1224-sale  --distpath ./    main3.py
if __name__ == '__main__':
    befor_run()
    time.sleep(5)
    # ---- start ----
    run()
    time.sleep(10)
    print("已关闭")
    time.sleep(20)
    exit(1)
