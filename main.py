BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *


#---------------------------------UI-----------------------------------------------

window = Tk()
window.geometry("900x726")
window.config(padx= 50, pady= 50)

canvas = Canvas(window,width=800,height=526)

Flash_front = PhotoImage(file="C:/Users/danma/OneDrive/Desktop/Python/FlashCard/images/card_front.png")
canvas.create_image(400,263,image=Flash_front)
canvas.grid(row=0, column=0,columnspan =2,sticky = E)

right_img = PhotoImage(file="C:/Users/danma/OneDrive/Desktop/Python/FlashCard/images/right.png")
right_button = Button(image = right_img, highlightthickness = 0 )
right_button.grid(row = 1 , column = 0 )
wrong_img = PhotoImage(file="C:/Users/danma/OneDrive/Desktop/Python/FlashCard/images/wrong.png")
wrong_button = Button(image = wrong_img, highlightthickness = 0)
wrong_button.grid(row = 1,column = 1)
Flash_back = PhotoImage(file="C:/Users/danma/OneDrive/Desktop/Python/FlashCard/images/card_back.png")




window.mainloop()

