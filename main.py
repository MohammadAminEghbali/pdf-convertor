"""
pip install pillow pdf2image
for poppler_path variable look at this url:
https://pypi.org/project/pdf2image/
Telegram channel: @PySources
"""

from pdf2image import convert_from_path
from PIL import PngImagePlugin

pdf_path = input("Enter the pdf file path: ")
output_filename = input("Enter the output file name: ")

poppler_path = r""

print("Extracting images ...")
images:list[PngImagePlugin.PngImageFile] = convert_from_path(
    pdf_path,
    fmt="png",
    poppler_path=poppler_path
)
print("Converting images ...")
for image in images:
    print(f"Image: {images.index(image) + 1} of {len(images)}")
    pixls = image.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if pixls[x, y] == (0, 0, 0):
                pixls[x, y] = (255, 255, 255)
            elif pixls[x, y] == (255, 255, 255):
                pixls[x, y] = (0, 0, 0)

print("Saving images ...")
images[0].save(output_filename, save_all=True, append_images=images)
print("App finished")
    
