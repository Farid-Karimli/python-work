import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title('Simple Calculator')

buttons_keys={
    1: ["AC", "+/-", "%", "/"],
    2: ["7",  "8",   "9", "*"],
    3: ["4",  "5",   "6", "-"],
    4: ["1",  "2",   "3", "+"],
    5: ["0",  "",    ".", "="]
    } #Contents of the buttons with the keys as rows

def functions(event):
    #get the text of the button being pressed
    operation = event.widget.cget('text')
   
    if operation in "0123456789":
        if lbl_output['text'] == "0":
           lbl_output['text'] = operation
        else:
             lbl_output['text'] += operation
    elif operation in "*/%-+.":
        lbl_output['text'] = lbl_output['text'] + operation
    elif operation == "AC":
        lbl_output['text'] = '0'
    elif operation == "+/-":
        lbl_output['text'] = "-" + lbl_output['text']
    elif operation == "=":
        lbl_output['text'] = str(eval(lbl_output['text']))
        
            
window.rowconfigure([0,1,2,3,4,5], minsize=120, weight=1)
window.columnconfigure([0,1,2,3], minsize=120, weight=1)



lbl_output=tk.Label(master=window,
                    text="0",
                    font=("Courier",50),
                    anchor="e",
                    )
lbl_output.grid(row=0, column=0, columnspan=4, sticky="ew")

#Creating the buttons
for row in buttons_keys:
    for button in buttons_keys[row]:
        btn_button = tk.Button(master=window,
                           text=button,
                           highlightbackground="orange",
                           font=("Courier",25),
                          
                           )
        btn_button.bind("<Button-1>",functions) 
        
        #Color layout of the buttons
        if buttons_keys[row].index(button)==3:
            btn_button['highlightbackground'] = "orange"
        elif row==1 and buttons_keys[row].index(button) < 3:
            btn_button['highlightbackground'] = "#b8c1cf"
        elif buttons_keys[row].index(button) < 4:
            btn_button['highlightbackground'] = "#3b3e45"
        
        
        btn_button.grid(row=row,  column=buttons_keys[row].index(button), sticky="nsew") 
                           

                        

window.mainloop()

