import requests
import time

# 请求的URL
url = 'http://55af.cfd/user/api/upload/handle'

# 要上传的文件（替换为你的图片文件路径）
# file_path = 'aimg.jpeg'
file_path = 'i123.png'

# 请求头（部分参数可以根据需要调整）
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "3126530",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryYcDhQEtUEcRQPcN1",
    "Cookie": "ACG-SHOP=8vo1nf7gkorreol8ju7kqlvc7v",
    "Host": "55af.cfd",
    "Origin": "http://55af.cfd",
    "Pragma": "no-cache",
    "Referer": "http://55af.cfd/user/security/personal",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

while True:
    # 定义请求体（这里需要根据实际情况填写具体的表单数据）
    # 由于Content-Type为application/x-www-form-urlencoded，我们需要将数据编码为这种格式
    # 假设表单数据为 {"username": "testuser", "password": "testpass"}，则编码后为 "username=testuser&password=testpass"
    # 注意：这里只是一个示例，你需要根据实际情况替换下面的data内容
    time.sleep(2)
    # 注意：Content-Length不需要手动设置，requests库会自动处理
    # 同时，Content-Type在发送文件时，requests库也会根据文件类型自动设置正确的multipart/form-data边界
    # 使用requests.post发送POST请求，files参数用于上传文件
    # 由于Content-Type和boundary通常是由requests库自动管理的，我们不需要在headers中手动设置它们（特别是boundary）
    # 下面的代码展示了如何正确地上传文件，同时省略了手动设置Content-Type和boundary
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}  # 这里的'file'是服务器端期望的文件字段名，根据实际情况调整
            response = requests.post(url, files=files, headers={
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
            print(response.text)
            timestamp = time.time()
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
            print(formatted_time, "--")
    except Exception as e:
        print(e)
