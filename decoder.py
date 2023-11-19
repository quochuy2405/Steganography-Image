from PIL import Image

# Creating an Image Object
enc_img = Image.open('encrypted_image.png')

# Loading pixel values of the original image, each entry is a pixel value i.e., RGB values as a sublist
enc_pixelMap = enc_img.load()

# Creating an empty string for our hidden message
msg = ""
msg_index = 0
msg_len = 0

# Traversing through the pixel values
for row in range(enc_img.size[0]):
    for col in range(enc_img.size[1]):

        # Fetching RGB value of a pixel to sublist
        pixel = enc_pixelMap[row, col]
        r = pixel[0]  # R value

        if col == 0 and row == 0:  # 1st pixel was used to store the length of the message
            msg_len = r
        elif msg_len > msg_index:  # Reading the message from R value of the pixel
            print(r)
            msg += chr(r)  # Converting to character
            msg_index += 1

enc_img.close()

print("The hidden message is:\n\n")
print(msg)
