from PIL import Image

# RGB values for recoloring.
mediumAquamarine = (102, 205, 170)
midnightBlue = (25, 25, 112)
steelBlue = (70, 130, 180)
indianRed = (205, 92, 92)




my_image = Image.open("corgi.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.

image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for pixel in image_list:
    photo=pixel[0]+ pixel[1]+ pixel[2]
    if photo<=182:
        recolored.append(mediumAquamarine)
    elif photo>182 and photo<=364:
        recolored.append(midnightBlue)
    elif photo>364 and photo<=546:
        recolored.append(steelBlue)
    elif photo>546:
        recolored.append(indianRed)


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
