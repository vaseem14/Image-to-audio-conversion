try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from gtts import gTTS
import os
import cv2

cam = cv2.VideoCapture(0)
retval, frame = cam.read()
if retval != True:
    raise ValueError("Can't read frame")

cv2.imwrite('test.png', frame)
# cv2.imshow("img1", frame)
# cv2.waitKey()
text = pytesseract.image_to_string(Image.open('test.png'))
print(text)
tts = gTTS(text=text, lang='en')
tts.save("test.mp3")
os.system("mpg321 test.mp3")