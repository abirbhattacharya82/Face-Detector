#Face Detector GUI
from tkinter import *
import cv2

window=Tk()
window.title("Face Detector")
window.resizable(0,0)

def func():
    face_cascade=cv2.CascadeClassifier("files/haarcascade_frontalface_default.xml")
    img=cv2.imread(e1_val.get())
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
    for x,y,w,h in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("Found",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val,width=50)
e1.grid(row=0,column=0)

b1=Button(window,text="Go",command=func)
b1.grid(row=0,column=1)

window.mainloop() 
