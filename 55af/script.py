import json
import os
import threading
import time
import requests
import random
import string

from PIL import Image
import pytesseract
import io

charset = string.ascii_letters + string.digits  # 共62种字符

def downImg(imgName):
    while True:
        try:
            url = "http://55af.cfd/assets/cache/images/202408162257533819370.jpg"
            response = requests.get(url)
            if response.status_code == 200:
                with open(imgName, "wb") as file:
                    file.write(response.content)
                print(f"下载图片并保存为: {imgName}")
            else:
                print(f"下载图片失败HTTP状态码:{response.status_code}")
        except Exception as e:
            print(f"下载图片Exception:{e}")

def uploadImg(imgName):
    while True:
        try:
            with open(imgName, 'rb') as f:
                files = {'file': f}  # 这里的'file'是服务器端期望的文件字段名，根据实际情况调整
                response = requests.post('http://55af.cfd/user/api/upload/handle', files=files, headers={
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Cookie': 'ACG-SHOP=8vo1nf7gkorreol8ju7kqlvc7v',
                    'Host': '55af.cfd',
                    'Origin': 'http://55af.cfd',
                    'Pragma': 'no-cache',
                    'Referer': 'http://55af.cfd/user/security/personal',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest'
                })
                # 打印响应内容
                print(f'上传图片httpcode={response.status_code},结果: {response.text}')
                timestamp = time.time()
                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
                print(formatted_time, "--")
        except Exception as e:
            print(f"上传图片Exception:{e}")


def getImgCodeStr(headers):
    # 获取当前工作目录
    current_directory = os.getcwd()
    # 设置 TESSDATA_PREFIX 为相对路径
    os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
    print(os.environ['TESSDATA_PREFIX'])
    try:
        # Step 1: 发送HTTP请求
        aaImg = requests.get('http://55af.cfd/user/captcha/image?action=register', headers=headers)
        # Step 2: 处理响应
        if aaImg.status_code == 200:
            # 将响应内容转换为二进制流
            image_stream = io.BytesIO(aaImg.content)
            # Step 3: 处理并保存图片
            image = Image.open(image_stream)
            image.save('captcha.png')  # 保存图片到本地
            # Step 4: 识别验证码
            # 注意：需要安装tesseract-ocr，并在系统路径中配置tesseract命令
            captcha_text = pytesseract.image_to_string(image)
            print('识别出的验证码:', captcha_text)
            return captcha_text
        else:
            print('请求失败，状态码:', aaImg.status_code)
            return 0
    except Exception as e:
        return 0


def reisgter():
    while True:
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            # 注意：Content-Length不需要手动设置，requests库会自动处理
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'ACG-SHOP=ktg7sdnds198gafap8savb29lv',
            'Host': '55af.cfd',
            'Origin': 'http://55af.cfd',
            'Referer': 'http://55af.cfd/user/authentication/register',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
            'X-Requested-With': 'XMLHttpRequest'
        }

        try:
            randomStr = ''.join(random.choices(charset, k=10))
            url = 'http://55af.cfd/user/api/authentication/register'
            # imgCode = getImgCodeStr(headers)
            imgCode = 111
            data = f'username={randomStr}&password={randomStr}&captcha={imgCode}'

            response = requests.post(url, headers=headers, data=data)
            print(json.loads(response.text))
            timestamp = time.time()
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
            print(formatted_time, data, "--")
        except Exception as e:
            print(f"注册账号Exception:{e}")


# 创建线程并启动
if __name__ == "__main__":
    threads = []

    #
    t1 = threading.Thread(target=reisgter, args=())
    t1.daemon = True  # 设置为守护线程，当主线程退出时，子线程也会退出
    t1.start()
    t1_1 = threading.Thread(target=reisgter, args=())
    t1_1.daemon = True  # 设置为守护线程，当主线程退出时，子线程也会退出
    t1_1.start()
    t1_2 = threading.Thread(target=reisgter, args=())
    t1_2.daemon = True  # 设置为守护线程，当主线程退出时，子线程也会退出
    t1_2.start()

    t2 = threading.Thread(target=uploadImg, args=("i123.png",))
    t2.daemon = True  # 设置为守护线程，当主线程退出时，子线程也会退出
    t2.start()
    t3 = threading.Thread(target=uploadImg, args=('2ljgggggg.jpg',))
    t3.daemon = True  # 设置为守护线程，当主线程退出时，子线程也会退出
    t3.start()

    t4 = threading.Thread(target=downImg, args=('downloaded_image1.jpg',))
    t4.daemon = True  # 设置为守护线程，当主线程退出时，子线程也会退出
    t4.start()
    t5 = threading.Thread(target=downImg, args=('downloaded_image2.jpg',))
    t5.daemon = True  # 设置为守护线程，当主线程退出时，子线程也会退出
    t5.start()
    while True:
        timestamp = time.time()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        print(formatted_time)
        time.sleep(5)

    print("主线程结束，子线程也会随之结束")

