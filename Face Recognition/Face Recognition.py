import PIL
from PIL import Image,ImageTk
import pytesseract
import os
import cv2
from tkinter import *
import time
import face_recognition
width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.configure(background='white')
root.geometry("700x600")
root.bind('<Escape>', lambda e: root.quit())
root.resizable(0,0)
lmain = Label(root)
imagecounter=int(0)
lmain.pack()
st=""
face_locations = []

def check_live(face_encodings):
    for face_encoding in face_encodings:
        _,frame=cap.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
        if(match):
            print("Hurray!!")

def read_image(name):
    # Read from Folder using First Name and read images 0 to 10 and save face encoding with name outside in a txt file now do same for no. of Users Entered4
    face_encodings=[]
    for i in range(1,11):
        image=face_recognition.load_image_file(f"./Face Recognition/{name}/{i}.png")
        face_locations = face_recognition.face_locations(image)
        face_encoding = face_recognition.face_encodings(image, face_locations)[0]
        face_encodings.append(face_encoding)
    return face_encodings

def show_frame(name):
    _, frame = cap.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    newpath = f'C:/Users/Mayank Goyal/Desktop/Face Recognition/{name}' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for i in range(1,11):
        ret, frame = cap.read()
        time.sleep(3)
        img_name = "{}.png".format(i)
        path =f'C:/Users/Mayank Goyal/Desktop/Face Recognition/{name}/'
        cv2.imwrite(os.path.join(path , img_name), frame)
        print("{} written!".format(img_name))
    face_encodings=read_image(name)
    check_live(face_encodings)    

def name_portal():
    def save_name():
        st=e.get()
        print( st+" is Saved with us")   
        show_frame(st)
    
    Label(root, text="First Name").pack()
    e = Entry(root)
    e.pack()
    e.focus_set()
    click_button = Button(master=root, text='Start',bg="green",fg="white", command=save_name)
    click_button.pack(side="top")
    
name_portal()
root.mainloop()

    #Label(root, 
    #		 text=u"Made With \u2661 By Mayank Goyal",
    #		 fg = "red",
    #		 bg = "white",
    #		 font = "Helvetica 26 bold italic").pack()
