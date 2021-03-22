import turtle
import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=100, height=50)
window.config(padx=50, pady=50)


def convert():
    conversion = int(input.get()) * 1.609
    output.config(text=conversion)


input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

units = tkinter.Label(text='Miles')
units.grid(column=2, row=0)

output = tkinter.Label(text='0')
output.grid(column=1, row=1)

output_units = tkinter.Label(text='Km')
output_units.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', command=convert)
button.grid(column=1, row=3)

window.mainloop()
