from PIL import image
    im = image.open("corgi.jpg")
    im.rotate(45).show()
new_image = image.new(im.mode, im.size)
new_image.save("output.jpg")

im.getdata() => sequence
print(im.getdata())
im.putdata(data)
im.putdata(data, scale, offset)
