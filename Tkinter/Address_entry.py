import tkinter as tk

window = tk.Tk()

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



