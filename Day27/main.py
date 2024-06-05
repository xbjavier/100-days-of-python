from tkinter import *

window = Tk()
window.minsize(350, 200)
label = Label(text="Miles", font=("Arial", 24, "bold"))
label.grid(row=0,column=2)

input = Entry(width=10)
input.grid(row=0,column=1)

equal_label = Label(text="Is equal to", font=("Arial", 24, "bold"))
equal_label.grid(row=1,column=0)

result_label = Label(text="", font=("Arial", 24, "bold"))
result_label.grid(row=1,column=1)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(row=1,column=2)


def miles_to_km():
    try:
        miles = float(input.get())
    except:
        print("No text in the input")
        return

    result_label.config(text=f" {round(miles * 1.609344, 2)} ")


button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2,column=1)

window.mainloop()