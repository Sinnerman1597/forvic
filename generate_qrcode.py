import qrcode

# Ngrok URL，替换成你的实际Ngrok URL
ngrok_url = "https://example.ngrok.io"

# 创建QR码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(ngrok_url)
qr.make(fit=True)

# 创建QR码图像
img = qr.make_image(fill_color="black", back_color="white")

# 保存QR码图像为文件
img.save("ngrok_qr_code.png")
