import qrcode
import image
qr = qrcode.QRCode(
    version=15,    #15 means the version of qr code the higher the value the bigger the picture.
    box_size=10,   #size of box  where qr code is displayed
    border=5       #white part of image, border is all 4 sides with white color.
                 )
data="https://github.com/kavyashree6"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")