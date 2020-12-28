import tkinter as tk

window = tk.Tk()

"""
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_b.pack()
frame_a.pack()
"""
"""
border_effects = {

    "flat": tk.FLAT,

    "sunken": tk.SUNKEN,

    "raised": tk.RAISED,

    "groove": tk.GROOVE,

    "ridge": tk.RIDGE,

}


window = tk.Tk()


for relief_name, relief in border_effects.items():

    frame = tk.Frame(master=window, relief=relief, borderwidth=5)

    frame.pack(side=tk.LEFT)

    label = tk.Label(master=frame, text=relief_name)

    label.pack()
"""

"""
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
"""

"""
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()


label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)


label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)
"""


"""
for i in range(3):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    
    for j in range(3):

        frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth= 1
                )
        frame.grid(row=i,column=j, padx=5,pady=5)
        label=tk.Label(master=frame,text=f"Row {i}\nColumn {j}")
        label.pack()
"""



window.columnconfigure(0,weight=1,minsize=20)
window.columnconfigure(1,weight=1,minsize=80)
window.rowconfigure([0,1,2,3,4,5,6,7],
                    weight = 1,
                    minsize=10)
frame = tk.Frame(master=window,
                 relief=tk.SUNKEN,
                 borderwidth=3)
frame.pack()

lbl_name = tk.Label(master=frame, text="First Name:")
lbl_surname = tk.Label(master=frame, text="Last Name:")
lbl_address1 = tk.Label(master=frame, text="Address Line 1:")
lbl_address2 = tk.Label(master=frame, text="Address Line 2:")
lbl_city = tk.Label(master=frame, text="City:")
lbl_state = tk.Label(master=frame, text="State/Province")
lbl_postal = tk.Label(master=frame, text="Postal Code:")
lbl_country = tk.Label(master=frame, text="Country:")

ent_name = tk.Entry(master=frame)
ent_surname = tk.Entry(master=frame)
ent_address1 = tk.Entry(master=frame)
ent_address2 = tk.Entry(master=frame)
ent_city = tk.Entry(master=frame)
ent_state = tk.Entry(master=frame)
ent_postal = tk.Entry(master=frame)
ent_country = tk.Entry(master=frame)


lbl_name.grid(row=0,column=0,sticky="w")
ent_name.grid(row=0,column=1)

lbl_surname.grid(row=1,column=0,sticky="w")
ent_surname.grid(row=1,column=1)

lbl_address1.grid(row=1,column=0,sticky="w")
ent_address1.grid(row=1,column=1)

lbl_address2.grid(row=2,column=0,sticky="w")
ent_address2.grid(row=2,column=1)

lbl_city.grid(row=3,column=0,sticky="w")
ent_city.grid(row=3,column=1)

lbl_state.grid(row=4,column=0,sticky="w")
ent_state.grid(row=4,column=1)

lbl_postal.grid(row=5,column=0,sticky="w")
ent_postal.grid(row=5,column=1)

lbl_country.grid(row=6,column=0,sticky="w")
ent_country.grid(row=6,column=1)

btn_clear = tk.Button(
        text="Clear" ,
        relief=tk.RAISED,
        borderwidth=5
        )

btn_submit = tk.Button(
        text="Submit",
        relief=tk.RAISED,
        borderwidth=5
        )

btn_submit.pack(side=tk.RIGHT)
btn_clear.pack(side=tk.RIGHT)





























window.mainloop()



