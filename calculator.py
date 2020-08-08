from tkinter import *

calculation = {
    'operand1' : None,
    'operand2' : None,
    'operator' : None
}


def click_number(number):
    previous = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, previous + str(number))
    if not calculation['operator']:
        calculation['operand1'] = float(previous + str(number))
    else:
        calculation['operand2'] = float(previous + str(number)) 
    
    print(calculation)


def click_operator(operator):
    calculation['operator'] = operator
    calculation['operand1'] = float(input_field.get())
    input_field.delete(0, END)

    print(calculation)

    

def click_clear():
    input_field.delete(0, END)
    calculation['operand1'] = None
    calculation['operand2'] = None
    calculation['operator'] = None

    print(calculation)

def click_equals():
    if calculation['operand1'] and calculation['operand2']:
        if calculation['operator'] == '+':
            result = calculation['operand1'] + calculation['operand2']
        elif calculation['operator'] == '-':
            result = calculation['operand1'] - calculation['operand2']
        elif calculation['operator'] == 'x':
            result = calculation['operand1'] * calculation['operand2']
        elif calculation['operator'] == '/':
            result = calculation['operand1'] / calculation['operand2']
        input_field.delete(0, END)
        input_field.insert(0, ('%f' % result).rstrip('0').rstrip('.'))
        calculation['operand1'] = result
        calculation['operand2'] = None
        calculation['operator'] = None
        
    elif calculation['operand1'] and not calculation['operand2']:
        input_field.insert(0, ('%f' % calculation['operand1']).rstrip('0').rstrip('.'))
        calculation['operand2'] = None
        calculation['operator'] = None
    
    else:
        pass

    print(calculation)


def click_back():
    previous = input_field.get()
    current = ''
    if previous:
        current = previous[:-1]
    input_field.delete(0, END)
    input_field.insert(0, current)

    print(calculation)
    

root = Tk()

# Create entry
input_field = Entry(root, width = 40, borderwidth = 5)
input_field.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# Create buttons
button_1 = Button(root, text="1", width = 10, command  = lambda : click_number(1))
button_2 = Button(root, text="2", width = 10, command  = lambda : click_number(2))
button_3 = Button(root, text="3", width = 10, command  = lambda : click_number(3))
button_4 = Button(root, text="4", width = 10, command  = lambda : click_number(4))
button_5 = Button(root, text="5", width = 10, command  = lambda : click_number(5))
button_6 = Button(root, text="6", width = 10, command  = lambda : click_number(6))
button_7 = Button(root, text="7", width = 10, command  = lambda : click_number(7))
button_8 = Button(root, text="8", width = 10, command  = lambda : click_number(8))
button_9 = Button(root, text="9", width = 10, command  = lambda : click_number(9))
button_0 = Button(root, text="0", width = 10, command  = lambda : click_number(10))
button_add = Button(root, text="+", width = 10, command  = lambda: click_operator('+'))
button_sub = Button(root, text="-", width = 10, command  = lambda: click_operator('-'))
button_mul = Button(root, text="x", width = 10, command  = lambda: click_operator('x'))
button_div = Button(root, text="/", width = 10, command  = lambda: click_operator('/'))
button_equal = Button(root, text = "=", width = 10, command  = click_equals)
button_clear = Button(root, text="clear", width = 20, command = click_clear)
button_back = Button(root, text="back", width = 10, command = click_back)

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
button_back.grid(row = 4, column = 1, columnspan = 1)
button_equal.grid(row = 4, column = 2, columnspan = 1)

button_add.grid(row = 1, column = 3, columnspan = 1)
button_sub.grid(row = 2, column = 3, columnspan = 1)
button_mul.grid(row = 3, column = 3, columnspan = 1)
button_div.grid(row = 4, column = 3, columnspan = 1)

button_clear.grid(row = 5, column = 1, columnspan = 2)



root.mainloop()