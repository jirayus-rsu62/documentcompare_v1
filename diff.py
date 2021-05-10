from PIL import Image, ImageChops ; from PIL import ImageDraw ; from PIL import ImageFont

correct_img = Image.open("./001.jpg")
test_img = Image.open("./004.jpg") 
check = ImageChops.difference(correct_img, test_img)

if check.getbbox():
    puttext = ImageDraw.Draw(check)
    font_path = ("./RSU_BOLD.ttf")
    font = ImageFont.truetype(font_path, 100)
    puttext.text((380,700), "NOT MATCHED",(255,0,0), font=font)
    check.show()
    test_img.show()
    correct_img.show()
    
else:
    check = correct_img
    puttext = ImageDraw.Draw(check)
    font_path = ("./RSU_BOLD.ttf")
    font = ImageFont.truetype(font_path, 100)
    puttext.text((450,700), "MATCH",(0,255,0), font=font)
    check.show()
