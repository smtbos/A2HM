from PIL import Image

base = Image.open("logo.png")

ls = [1024, 512, 192, 180, 167, 144, 120, 96, 87, 80, 72, 64, 60, 58, 48, 40, 36 ]

for i in ls:
    im = base.resize((i, i))
    im.save("../icon-"+str(i)+".png")
