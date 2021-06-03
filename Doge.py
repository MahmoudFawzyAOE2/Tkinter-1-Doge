from tkinter import *
import PIL
from PIL import ImageTk,Image
doge = Tk()
doge.title('Doge is The Best ... By: MFT')
doge.iconbitmap(r'happy.ico')

img_lab =Label(doge,padx=150,pady=150 ).grid(row=0,column=0,columnspan=3)
img0=ImageTk.PhotoImage(Image.open(r'happy.jpg'))
img1=ImageTk.PhotoImage(Image.open(r'astronaut.jpg'))
img2=ImageTk.PhotoImage(Image.open(r'hydra.jpg'))
img3=ImageTk.PhotoImage(Image.open(r'joker.jpg'))
img4=ImageTk.PhotoImage(Image.open(r'love1.jpg'))
img5=ImageTk.PhotoImage(Image.open(r'spider.jpg'))
img6=ImageTk.PhotoImage(Image.open(r'shotgun.jpg'))
img7=ImageTk.PhotoImage(Image.open(r'muslim.jpg'))
img8=ImageTk.PhotoImage(Image.open(r'astoishing.jpg'))
img9=ImageTk.PhotoImage(Image.open(r'sleeping.jpg'))
img10=ImageTk.PhotoImage(Image.open(r'movie_night.jpg'))
img11=ImageTk.PhotoImage(Image.open(r'businessman.jpg'))
img12=ImageTk.PhotoImage(Image.open(r'love2.jpg'))
img13=ImageTk.PhotoImage(Image.open(r'muscle.jpg'))
img14=ImageTk.PhotoImage(Image.open(r'baby.jpg'))
img15=ImageTk.PhotoImage(Image.open(r'cute.jpg'))


def happy ():
    img_lab =Label(image=img0).grid(row=0,column=0,columnspan=4)
def astronaut ():
    img_lab =Label(image=img1).grid(row=0,column=0,columnspan=4)
def hydra ():
    img_lab =Label(image=img2).grid(row=0,column=0,columnspan=4)
def joker ():
    img_lab =Label(image=img3).grid(row=0,column=0,columnspan=4)
def love1 ():
    img_lab =Label(image=img4).grid(row=0,column=0,columnspan=4)
def spider ():
    img_lab =Label(image=img5).grid(row=0,column=0,columnspan=4)
def shotgun ():
    img_lab =Label(image=img6).grid(row=0,column=0,columnspan=4)
def muslim ():
    img_lab =Label(image=img7).grid(row=0,column=0,columnspan=4)
def astoishing ():
    img_lab =Label(image=img8).grid(row=0,column=0,columnspan=4)
def sleeping ():
    img_lab =Label(image=img9).grid(row=0,column=0,columnspan=4)
def movie_night ():
    img_lab =Label(image=img10).grid(row=0,column=0,columnspan=4)
def businessman ():
    img_lab =Label(image=img11).grid(row=0,column=0,columnspan=4)
def love2 ():
    img_lab =Label(image=img12).grid(row=0,column=0,columnspan=4)
def muscle ():
    img_lab =Label(image=img13).grid(row=0,column=0,columnspan=4)
def baby ():
    img_lab =Label(image=img14).grid(row=0,column=0,columnspan=4)
def cute ():
    img_lab =Label(image=img15).grid(row=0,column=0,columnspan=4)






b0=Button(doge, text='happy',command=happy,padx=37,pady=20).grid(row=1,column=0)
b1=Button(doge, text='astronaut',command=astronaut,padx=27,pady=20).grid(row=1,column=1)
b2=Button(doge, text='hydra',command=hydra,padx=40,pady=20).grid(row=1,column=2)
b3=Button(doge, text='joker',command=joker,padx=42,pady=20).grid(row=1,column=3)
b4=Button(doge, text='love1',command=love1,padx=40,pady=20).grid(row=2,column=0)
b5=Button(doge, text='spider',command=spider,padx=36,pady=20).grid(row=2,column=1)
b6=Button(doge, text='shotgun',command=shotgun,padx=33,pady=20).grid(row=2,column=2)
b7=Button(doge, text='muslim',command=muslim,padx=35,pady=20).grid(row=2,column=3)
b8=Button(doge, text='astoishing',command=astoishing,padx=27,pady=20).grid(row=3,column=0)
b9=Button(doge, text='sleeping',command=sleeping,padx=30,pady=20).grid(row=3,column=1)
b10=Button(doge, text='movie-night',command=movie_night,padx=22,pady=20).grid(row=3,column=2)
b11=Button(doge, text='businessman',command=businessman,padx=21,pady=20).grid(row=3,column=3)
b12=Button(doge, text='love2',command=love2,padx=40,pady=20).grid(row=4,column=0)
b13=Button(doge, text='muscle',command=muscle,padx=33,pady=20).grid(row=4,column=1)
b14=Button(doge, text='baby',command=baby,padx=42,pady=20).grid(row=4,column=2)
b15=Button(doge, text='cute',command=cute,padx=44,pady=20).grid(row=4,column=3)

doge.mainloop()
