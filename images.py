from PIL import Image

# Load the image
image_path = 'marko.jpeg'
image = Image.open(image_path)

# Convert image to grayscale
grayscale_image = image.convert('L')

# Define a more detailed set of ASCII characters, including more whitespace
ASCII_CHARS = " .:-=+*#%@"

# Adjust the function to handle the new set of characters
def pixel_to_ascii(pixel_value):
    return ASCII_CHARS[pixel_value * (len(ASCII_CHARS) - 1) // 255]

# Create ASCII art
ascii_art = ""
width, height = grayscale_image.size

for y in range(height):  # Use every row
    for x in range(width):  # Use every column
        pixel_value = grayscale_image.getpixel((x, y))
        ascii_art += pixel_to_ascii(pixel_value)
    ascii_art += "\n"

# Print ASCII art to console
#print(ascii_art)
print("done")

# Save ASCII art to a text file
with open('ascii_art.txt', 'w') as f:
    f.write(ascii_art)
