import tkinter as tk

def convert():
    fahrenheit = int(ent_temperature.get())
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = str(round(celsius,2)) + "\N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature Converter")

frm_entry = tk.Frame(master=window)


ent_temperature = tk.Entry(master=frm_entry,
                           width=10
                           )

lbl_fahrenheit = tk.Label(master=frm_entry,
                          text="\N{DEGREE FAHRENHEIT}",
                          
                          )

btn_convert = tk.Button(master=window,
                        text="\N{RIGHTWARDS BLACK ARROW}",
                        height=2,
                        width=2,
                        relief=tk.RAISED,
                        borderwidth=1,
                        command=convert
                        )

lbl_result = tk.Label(master=window,
                      text="\N{DEGREE CELSIUS}"
                      )
                      


frm_entry.grid(row=0,column=0,padx=10)
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_fahrenheit.grid(row=0, column=1, sticky="w")

btn_convert.grid(row=0,column=1,pady=10)
lbl_result.grid(row=0,column=2,padx=10)



window.mainloop()
