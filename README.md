
# Image Steganography Web Application

The LSB (Least Significant Bit) technique hides messages within the least significant bits of an image and can extract hidden messages from the image. 

![demo](https://github.com/alalala666/LSB/assets/97104709/3aa634d5-160c-49fc-95f4-aaab1041f53d)

This method involves hiding a message within an image: reading the input image and converting it into a one-dimensional array. The input text is padded to a fixed length and converted to UTF-8 encoding. The UTF-8 encoding is then converted into a binary string. Using the LSB technique, the binary string is embedded into the image's bits. If the current bit of the binary string is 0 and the corresponding value in the image array is odd, it is decremented to make it even. If the current bit of the binary string is 1 and the corresponding value in the image array is even, it is incremented to make it odd. The modified one-dimensional array is then reshaped back into the original image shape and saved.

## Features

- **Encrypt Text**: Hide a text message inside an image.
- **Decrypt Text**: Extract the hidden text message from an image.

## Requirements

- Python 3.x
- Flask
- `Least_Significant_Bit` module (custom or third-party library for LSB steganography)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/image-steganography.git
   cd image-steganography
