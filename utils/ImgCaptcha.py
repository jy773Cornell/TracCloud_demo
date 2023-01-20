import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

"""
    img, code = img_captcha()
    
    1. open directly
    img.show()

    2. write into a file
    with open('code.png','wb') as f:
        img.save(f,format='png')

    3. write into memory (Python3)
    from io import BytesIO
    stream = BytesIO()
    img.save(stream, 'png')
    stream.getvalue()

    4. write into memoryPython2）
    import StringIO
    stream = StringIO.StringIO()
    img.save(stream, 'png')
    stream.getvalue()
"""


# Generate image captcha

def img_captcha(width=160, height=40, char_length=5, font_file='kumo.ttf', font_size=32):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndChar():

        # Generate random character

        return chr(random.randint(65, 90))

    def rndColor():

        # Generate random color

        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # Draw characters into the image

    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], char, font=font, fill=rndColor())

    # Draw interference points

    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # Draw interference circles

    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # Draw interference lines

    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rndColor())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)
