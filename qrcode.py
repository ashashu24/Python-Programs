import qrcode
import image
qr=qrcode.QRcode(version=10,box_size=8,border=5)
data="Hello World"

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")
