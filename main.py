import os
import time
import pyautogui
import pytesseract
import re


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
        location = pyautogui.locateOnScreen(image_path, confidence=0.7)
        # 检查是否找到了图片
        if location:
            print(f"图片位置：{location}")
            # 获取图片中心坐标
            center = pyautogui.center(location)
            print(f"图片中心坐标：{center}")
            # 移动鼠标到图片中心
            pyautogui.moveTo(center)
            pyautogui.click()
            return True
        else:
            return False
    except Exception as e:
        print(f"findShenshoudan4 err:{e}")
        return False


if __name__ == '__main__':
    time.sleep(2)
    # 获取当前工作目录
    current_directory = os.getcwd()
    # 设置 TESSDATA_PREFIX 为相对路径
    os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
    print(os.environ['TESSDATA_PREFIX'])
    while True:
        if findShenshoudan4():
            while True:
                time.sleep(0.5)
                x2, y2 = findXY('pic/danjia.jpg')
                if x2 and y2:
                    print("移动到单价位置", x2, y2)
                    pyautogui.moveTo(x2, y2)
                    # 截取屏幕上指定区域的截图-----价格列表
                    time.sleep(0.5)
                    # 参数是(left, top, width, height)
                    screenshot = pyautogui.screenshot(region=(x2, y2, 100, 350))  # 示例区域
                    # 使用 Tesseract 识别图像中的文字
                    text = pytesseract.image_to_string(screenshot)
                    lines = text.splitlines()
                    priceList = []
                    print(lines)
                    for line in lines:
                        # 清除非数字字符并检查是否为空
                        cleaned_line = re.sub(r'[^\d]', '', line)
                        if cleaned_line:  # 如果 cleaned_line 不为空
                            priceList.append(int(cleaned_line))
                    print(priceList)
                    if len(priceList) > 0:
                        pyautogui.moveTo(x2, y2 + 55 * 1)
                        # 找出大于888的下标
                        for i, value in enumerate(priceList):
                            # 满足条件的价格
                            if value < 5300:
                                pyautogui.click(x2, y2 + 55 * (i + 1))
                                print("点击了商品位置", x2, y2 + 55 * (i + 1))
                                time.sleep(0.5)
                                x3, y3 = findXY('pic/shangpingxiangqinggoumai.png')
                                if x3 and y3:
                                    print("点击购买 shangpingxiangqinggoumai位置", x3, ",", y3)
                                    pyautogui.click(x3, y3)
                                    break
                        pyautogui.moveTo(x2, y2)

                        x2, y2 = findXY('pic/jishouwuping.png')
                        if x2 and y2:
                            print("移动到寄售位置", x2, y2)
                            print("关闭商品列表", x2, y2)
                            pyautogui.click(x2 + 400, y2)
                            break
                else:
                    x2, y2 = findXY('pic/jishouwuping.png')
                    if x2 and y2:
                        print("移动到寄售位置", x2, y2)
                        print("关闭商品列表", x2, y2)
                        pyautogui.click(x2 + 400, y2)
                        break
