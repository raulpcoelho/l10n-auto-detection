import subprocess
import pytesseract
from PIL import Image

# Execute the command
droid_command = subprocess.run(
    "droidbot --help", shell=True, capture_output=True, text=True
)

# Print the output
print(droid_command.stdout)

# Open an image file
image = Image.open("example.png")

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
