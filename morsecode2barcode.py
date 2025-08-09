import os
from PIL import Image, ImageDraw

codes = [".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--"]

border = 40
height = 60
line_width = 2
separate_per_line = 20

code_count = 0
for line in codes:
    for character in line:
        code_count += 1
    code_count += separate_per_line

image = Image.new("RGB", (border*2+code_count*int(code_count*line_width/20), border*2+height), "#FFF")
draw = ImageDraw.Draw(image)

offset = 0
for line in codes:
    for idx, character in enumerate(line):
        start = (border + offset, border)
        end = (border + offset, border + height)
        if character == ".":
            draw.line([start, end], fill="#000", width=line_width)
            offset += line_width
        elif character == "-":
            draw.line([start, end], fill="#000", width=(line_width*2))
            offset += line_width * 2
        elif character == " ":
            offset += line_width * 2
        elif character == "/":
            start = (start[0], start[1]-10)
            end = (end[0], end[1]+10)
            draw.line([start, end], fill="#000", width=line_width)
            offset += line_width
        offset += line_width
    offset += separate_per_line

image = image.crop((0, 0, border*2+offset-separate_per_line-line_width*2, border*2+height))

image.save("output.jpg")

os.startfile("output.jpg")