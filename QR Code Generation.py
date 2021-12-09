#qr code generation
import qrcode
img = qrcode.make("https://www.linkedin.com/in/bharath-g-821495137/")
img.save("LinkedIn.jpg")