from flask import Flask, redirect, url_for, request
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from gtts import gTTS
import os
import cv2

app = Flask(__name__)

@app.route('/success')
def success():
   cam = cv2.VideoCapture(0)
   retval, frame = cam.read()
   cam.release()
   if retval != True:
      # raise ValueError("Can't read frame")
      cam.release()
      return '''<html>
                     <body>
                        <p>camera is already running</p>
                     </body>
                  </html>'''
   cv2.imwrite('test.png', frame)
   # cv2.imshow("img1", frame)
   # cv2.waitKey()
   text = pytesseract.image_to_string(Image.open('test.png'))
   # print(text)
   try:
      tts = gTTS(text=text, lang='en')
      tts.save("test.mp3")
      os.system("mpg321 test.mp3")
   except:
      return '''<html>
                     <body>
                        <p>No readable text</p>
                     </body>
                  </html>'''

   # cam.release() 
   return '''<html>
   <body>
   <p>%s</p>
      <form action = "http://localhost:5000/index" method = "post">
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>'''%text

@app.route('/index',methods = ['POST', 'GET'])
def index():
   if request.method == 'POST':
      # in_text = request.form['nm']
      return redirect(url_for('success'))
   else:
      # user = request.args.get('nm')
      return redirect(url_for('success'))

if __name__ == '__main__':
   app.run(debug = True)
