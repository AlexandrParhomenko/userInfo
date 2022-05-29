import requests
import getpass
from tkinter import *
from PIL import Image, ImageTk

canvas_width = 500
canvas_height = 500
root = Tk()
root.geometry("1500x800")
root.title('User information viewer')
e = Entry(root, width=1000, borderwidth=5)
frame = LabelFrame(root, padx=100, pady=100)
frame.pack(padx=100, pady=10)
frame1 = LabelFrame(root, padx=100, pady=100)
frame1.pack(padx=100, pady=100)
bg = ImageTk.PhotoImage(file="qw.png")
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def userinfo():
    myButton.destroy()
    mylabel = Label(root, text='Your username is: ' + getpass.getuser(), font=("Arial", 15))
    mylabel.pack()


def location():
    myButton1.destroy()
    info = requests.get('http://api.ipstack.com/2.94.68.26?access_key=75a4a62abeadc4d671bb056439cf6ce5').json()
    s1 = ''
    t = 0
    for key, value in info.items():
        if t < 12:
            s1 += f'{key}: {value}\n'
            mylabel1 = Label(root, text=s1, font=("Arial", 15))
            t = t + 1
    mylabel1.pack()


myButton = Button(root, text='Show user information', command=userinfo, font=("Arial", 15))
myButton.pack(pady=50)
myButton1 = Button(root, text='Show user location info', command=location, font=("Arial", 15))
myButton1.pack(pady=50)
button_quit = Button(root, text='Exit program', command=root.quit, font=("Arial", 15))
button_quit.pack(pady=50)
root.mainloop()
