from tkinter import *

root = Tk()

# Create entry
input_field = Entry(root, width = 40, borderwidth = 5)
input_field.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# Create buttons
button_1 = Button(root, text="1", width = 10)
button_2 = Button(root, text="2", width = 10)
button_3 = Button(root, text="3", width = 10)
button_4 = Button(root, text="4", width = 10)
button_5 = Button(root, text="5", width = 10)
button_6 = Button(root, text="6", width = 10)
button_7 = Button(root, text="7", width = 10)
button_8 = Button(root, text="8", width = 10)
button_9 = Button(root, text="9", width = 10)
button_0 = Button(root, text="0", width = 10)
button_add = Button(root, text="+", width = 10)
button_sub = Button(root, text="-", width = 10)
button_mul = Button(root, text="x", width = 10)
button_div = Button(root, text="/", width = 10)
button_equal = Button(root, text = "=", width = 10)
button_clear = Button(root, text="clear", width = 20)
button_dot = Button(root, text=".", width = 10)

# position buttons
button_7.grid(row = 1, column = 0, columnspan = 1)
button_8.grid(row = 1, column = 1, columnspan = 1)
button_9.grid(row = 1, column = 2, columnspan = 1)

button_4.grid(row = 2, column = 0, columnspan = 1)
button_5.grid(row = 2, column = 1, columnspan = 1)
button_6.grid(row = 2, column = 2, columnspan = 1)

button_1.grid(row = 3, column = 0, columnspan = 1)
button_2.grid(row = 3, column = 1, columnspan = 1)
button_3.grid(row = 3, column = 2, columnspan = 1)

button_0.grid(row = 4, column = 0, columnspan = 1)
button_dot.grid(row = 4, column = 1, columnspan = 1)
button_equal.grid(row = 4, column = 2, columnspan = 1)

button_add.grid(row = 1, column = 3, columnspan = 1)
button_sub.grid(row = 2, column = 3, columnspan = 1)
button_mul.grid(row = 3, column = 3, columnspan = 1)
button_div.grid(row = 4, column = 3, columnspan = 1)

button_clear.grid(row = 5, column = 1, columnspan = 2)



root.mainloop()