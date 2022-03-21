# Image-Color-Compressor
Compresses an image into a palette of colors and specified size (by default, 120x120) (currently hardcoded as this script is poorly optimized for anything very large, shouldn't be changed much).
At any pass, if the image is presented to 85% accuracy (currently hardcoded), the program will stop at that pass.

Palettes consist of lists of RGB colors that the program can choose from and can be created in text form.
The default palette has all greys eliminated and consists of shades of primary colors. This keeps the program from averaging everything to shades of grey.

# Running
- Install the Pillow package via pip (e.g. in a Windows environment where Python 3 is installed, run "pip install pillow")
- Run the program in the commandline with an image as the first argument (e.g. 'python \_\_main\_\_.py "palette - no greys.txt" "image.jpg"')

# Example output
### Unconverted image
![garden](https://user-images.githubusercontent.com/8731155/159373072-0782ffed-a1a0-4c2a-9c6a-e6f4b8c07415.jpg)

### Converted image at each pass
![image](https://user-images.githubusercontent.com/8731155/159373125-ff1950df-1593-4ee9-a163-166e6d164468.png)

### Converted image at last pass (85% accuracy)
![image](https://user-images.githubusercontent.com/8731155/159373714-327d8e2c-f7f7-4bbc-bd01-3bdfa08abcf4.png)
