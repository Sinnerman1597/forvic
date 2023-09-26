import requests

# 替换成Ngrok Web界面的URL，通常是 http://localhost:4040/api/tunnels
ngrok_web_url = "http://localhost:4040/api/tunnels"

# 发送GET请求获取Ngrok Web界面内容
response = requests.get(ngrok_web_url)

# 解析JSON响应以获取Ngrok隧道信息
data = response.json()
tunnels = data["tunnels"]

# 打印所有Ngrok隧道的URL
for tunnel in tunnels:
    ngrok_url = tunnel["public_url"]
    print("Ngrok URL:", ngrok_url)