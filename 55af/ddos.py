import os

import requests
import json
import time

#  pip install requests --index-url https://pypi.tuna.tsinghua.edu.cn/simple

import random
import string

# 定义字符集（大小写字母+数字）
charset = string.ascii_letters + string.digits  # 共62种字符
def  ssss():
    return ''.join(random.choices(charset, k=10))
# 生成10位随机字符串
 # 示例输出：'aB3Fg7Tk9L'


# 定义请求头
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

def regisTT():
    # 定义请求的URL
    url = 'http://55af.cfd/user/api/authentication/register'

    while True:
        # 定义请求体（这里需要根据实际情况填写具体的表单数据）
        # 由于Content-Type为application/x-www-form-urlencoded，我们需要将数据编码为这种格式
        # 假设表单数据为 {"username": "testuser", "password": "testpass"}，则编码后为 "username=testuser&password=testpass"
        # 注意：这里只是一个示例，你需要根据实际情况替换下面的data内容
        time.sleep(1)
        try:
            sss = ssss()
            # imgCode = getImgCode()
            imgCode = 111
            data = f'username={sss}&password={sss}&captcha={imgCode}'  # 示例数据，请根据实际情况修改
            # 发送POST请求
            response = requests.post(url, headers=headers, data=data)
            # 打印响应内容

            print(json.loads(response.text))  # 如果响应是JSON格式，可以将其解析为Python字典（这里需要根据实际情况判断是否可以这样做）
            timestamp = time.time()
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
            print(formatted_time, data, "--")
        except Exception as e:
            print(e)


from PIL import Image
import pytesseract
import io

def getImgCode():
    try:
        # Step 1: 发送HTTP请求
        aaImg = requests.get('http://55af.cfd/user/captcha/image?action=register',headers=headers)

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



if __name__ == '__main__':
    # 获取当前工作目录
    current_directory = os.getcwd()
    # 设置 TESSDATA_PREFIX 为相对路径
    os.environ['TESSDATA_PREFIX'] = os.path.join(current_directory, 'pag\\Tesseract-OCR\\tessdata')
    print(os.environ['TESSDATA_PREFIX'])
    regisTT()