from cProfile import label
from tkinter import *
from tkinter import messagebox
import random

def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

def no():
    messagebox.showinfo(' ', 'I love you!! <3 YIPEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0,1600) , y=random.randint(0,800))
    




root = Tk()
root.geometry('1920x1080')
root.title('Question!')
root.resizable(width=False, height=False)
root['bg'] = 'pink'


#Top Left
my_img = PhotoImage(file='C:/Users/blake/Desktop/bronti2.png')
smallerImage = resizeImage(my_img, 200, 200)
lbl = Label(root, image=smallerImage)
lbl.place(x=100, y=100)

#Bottom Left
my_img2 = PhotoImage(file='C:/Users/blake/Desktop/speedy.png')
smallerImage2 = resizeImage(my_img2, 200, 200)
lbl2 = Label(root, image=smallerImage2)
lbl2.place(x=100, y=800)

#Top Right
my_img3 = PhotoImage(file='C:/Users/blake/Desktop/rexxi.png')
smallerImage3 = resizeImage(my_img3, 200, 200)
lbl3 = Label(root, image=smallerImage3)
lbl3.place(x=1650, y=100)

#Bottom Right
my_img4 = PhotoImage(file='C:/Users/blake/Desktop/heart.png')
smallerImage4 = resizeImage(my_img4, 200, 200)
lbl4 = Label(root, image=smallerImage4)
lbl4.place(x=1650, y=800)

#Center
my_img5 = PhotoImage(file='C:/Users/blake/Desktop/us.png')
smallerImage5 = resizeImage(my_img5, 300, 300)
lbl5 = Label(root, image=smallerImage5)
lbl5.place(x=825, y=400)


label = Label(root, text='Will you be my valentine?', font='Arial 30 bold', bg ='pink').pack()
btnYes = Button(root, text = 'No', font = 'Arial 20 bold', bg='red', fg='white')
btnYes.place(x=1000, y=250)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='Yes', font='Arial 20 bold', bg='green', fg='white', command=no).place(x=870,y =250)


root.mainloop()












#FUN GAME!!!!!!!!!!!
