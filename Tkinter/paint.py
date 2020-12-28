import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkmacosx import Button as button 

window = tk.Tk()
window.title("Simple Drawing App")
s=ttk.Style()
window.geometry("1500x900")
s.configure("TButton", background="red")
color = "black"
clear_button = PhotoImage(file = "clear.png")

def paint(event):
    #co-ordinates
    x1,y1,x2,y2 = (event.x - 7), ( event.y - 7), ( event.x + 7),( event.y + 7)


    canvas.create_oval( x1,y1,x2,y2,
                   fill = color,
                   outline=color)

def change_color(event):
    global color
    print("Current Color = " + color)
    print("Selecting " + event.widget.cget('bg'))
    color = event.widget.cget('bg')

def clear(event):
    canvas.delete("all")
    
            
text = tk.Label(master=window,
                text="Drawing App \nClick and drag below to start drawing",
                font=("Arial",  20)
                )

text.pack()

frame=tk.Button(master=window,
                height=1300,
                width=900,
                )
frame.pack()


canvas = Canvas(frame,
           width=1300,
           height=700,
           bd=10,
           relief=SUNKEN,
           )  

canvas.pack(side=tk.LEFT)
canvas.bind('<B1-Motion>',paint)



frm_colors = tk.Frame(master=frame,bg="black",width=50)
frm_colors.pack()

btn_red = button(frm_colors,
                 width=50,
                 height=40,
                 bg="red")

btn_blue = button(frm_colors,
                 width=50,
                 height=40,
                 bg="blue")
btn_green = button(frm_colors,
                 width=50,
                 height=40,
                 bg="green")

btn_red.pack()
btn_blue.pack()
btn_green.pack()

btn_red.bind("<Button-1>", change_color)
btn_blue.bind("<Button-1>", change_color)
btn_green.bind("<Button-1>", change_color)



btn_clear = tk.Button(master=frm_colors, image=clear_button)
btn_clear.bind("<Button-1>", clear)
btn_clear.pack()














#window.mainloop()
