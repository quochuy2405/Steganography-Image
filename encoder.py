from PIL import Image

# Creating an image object
org_img = Image.open('original_image.png')

# Loading pixel values of the original image, each entry is pixel value i.e., RGB values as a sublist
org_pixelMap = org_img.load()

# Creating a new image object with image mode and dimensions as that of the original image
enc_img = Image.new(org_img.mode, org_img.size)
enc_pixelsMap = enc_img.load()

# Reading the message to be encrypted from the user
msg = '19521598'
msg_index = 0

# Finding the length of the message
msg_len = len(msg)

# Traversing through the pixel values
for row in range(org_img.size[0]):
    for col in range(org_img.size[1]):

        # Fetching RGB value a pixel to sublist
        pixel = org_pixelMap[row, col]
        r = pixel[0]  # R value
        g = pixel[1]  # G value
        b = pixel[2]  # B value

        if row == 0 and col == 0:  # 1st pixel is used to store the length of the message
            ascii_val = msg_len
            enc_pixelsMap[row, col] = (ascii_val, g, b)
        elif msg_index < msg_len:  # Hiding our message inside the R values of the pixels
            c = msg[msg_index]
            ascii_val = ord(c)
            enc_pixelsMap[row, col] = (ascii_val, g, b)
            msg_index += 1
        else:  # Assigning the pixel values of the old image to the new image
            enc_pixelsMap[row, col] = (r, g, b)

org_img.close()

# Display the image
enc_img.show()

# Save the image
enc_img.save("encrypted_image.png")
enc_img.close()
