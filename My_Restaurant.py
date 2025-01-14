from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operator = ''
food_prices = [150.50, 145.20, 300.75, 80.10, 100.10, 50.60, 230.70, 199.99]
drink_prices = [15.15, 30.25, 20.60, 70.80, 30.70, 25.50, 200.60, 50.90]
dessert_prices = [70.50, 300.30, 160.80, 140.70, 80.20, 90.70, 400.75, 120.10]


def click_button(number):
    global operator
    operator = operator + number
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)


def clear():
    global operator
    operator = ''
    calculator_display.delete(0, END)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0, END)
    calculator_display.insert(0, result)
    operator = ''


def check_checkbox():
    x = 0
    for box in food_boxes:
        if food_variables[x].get() == 1:
            food_boxes[x].config(state=NORMAL)
            if food_boxes[x].get() == '0':
                food_boxes[x].delete(0, END)
            food_boxes[x].focus()
        else:
            food_boxes[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1

    x = 0
    for box in drink_boxes:
        if drink_variables[x].get() == 1:
            drink_boxes[x].config(state=NORMAL)
            if drink_boxes[x].get() == '0':
                drink_boxes[x].delete(0, END)
            drink_boxes[x].focus()
        else:
            drink_boxes[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1

    x = 0
    for box in dessert_boxes:
        if dessert_variables[x].get() == 1:
            dessert_boxes[x].config(state=NORMAL)
            if dessert_boxes[x].get() == '0':
                dessert_boxes[x].delete(0, END)
            dessert_boxes[x].focus()
        else:
            dessert_boxes[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x += 1


def calculate_total():
    subtotal_food = 0
    p = 0
    for quantity in food_text:
        subtotal_food += float(quantity.get()) * food_prices[p]
        p += 1

    subtotal_drink = 0
    p = 0
    for quantity in drink_text:
        subtotal_drink += float(quantity.get()) * drink_prices[p]
        p += 1

    subtotal_dessert = 0
    p = 0
    for quantity in dessert_text:
        subtotal_dessert += float(quantity.get()) * dessert_prices[p]
        p += 1

    subtotal = subtotal_food + subtotal_drink + subtotal_dessert
    taxes = subtotal * 0.16
    total = subtotal + taxes

    var_food_cost.set(f'$ {round(subtotal_food, 2)}')
    var_drink_cost.set(f'$ {round(subtotal_drink, 2)}')
    var_dessert_cost.set(f'$ {round(subtotal_dessert, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_taxes.set(f'$ {round(taxes, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def generate_receipt():
    receipt_text.delete(1.0, END)
    receipt_number = f'N# - {random.randint(1000, 9999)}'
    date = datetime.datetime.now()
    receipt_date = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute} '
    receipt_text.insert(END, f'Details:\t\t{receipt_number}\t\t{receipt_date}\n')
    receipt_text.insert(END, f'*' * 76 + '\n')
    receipt_text.insert(END, 'Items\t\t\tQty\tItem Cost\n')
    receipt_text.insert(END, f'-' * 91 + '\n')

    x = 0
    for food in food_text:
        if food.get() != '0':
            receipt_text.insert(END, f'{food_list[x]}\t\t\t{food.get()}\t'
                                     f'$ {int(food.get()) * food_prices[x]}\n')
        x += 1

    x = 0
    for drink in drink_text:
        if drink.get() != '0':
            receipt_text.insert(END, f'{drink_list[x]}\t\t\t{drink.get()}\t'
                                     f'$ {int(drink.get()) * drink_prices[x]}\n')
        x += 1

    x = 0
    for dessert in dessert_text:
        if dessert.get() != '0':
            receipt_text.insert(END, f'{dessert_list[x]}\t\t\t{dessert.get()}\t'
                                     f'$ {int(dessert.get()) * dessert_prices[x]}\n')
        x += 1

    receipt_text.insert(END, f'-' * 91 + '\n')
    receipt_text.insert(END, f'Food Cost: \t\t\t\t{var_food_cost.get()}\n')
    receipt_text.insert(END, f'Drink Cost: \t\t\t\t{var_drink_cost.get()}\n')
    receipt_text.insert(END, f'Dessert Cost: \t\t\t\t{var_dessert_cost.get()}\n')
    receipt_text.insert(END, f'-' * 91 + '\n')
    receipt_text.insert(END, f'Sub-Total: \t\t\t\t{var_subtotal.get()}\n')
    receipt_text.insert(END, f'Tax: \t\t\t\t{var_taxes.get()}\n')
    receipt_text.insert(END, f'Total: \t\t\t\t{var_total.get()}\n')
    receipt_text.insert(END, f'*' * 76 + '\n')
    receipt_text.insert(END, "Thank you! - DANIEL'S RESTAURANT")


def save_receipt():
    receipt_info = receipt_text.get(1.0, END)
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(receipt_info)
    file.close()
    messagebox.showinfo('Information', 'The receipt has been saved')


def reset():
    receipt_text.delete(0.1, END)

    for text in food_text:
        text.set('0')
    for text in drink_text:
        text.set('0')
    for text in dessert_text:
        text.set('0')

    for box in food_boxes:
        box.config(state=DISABLED)
    for box in drink_boxes:
        box.config(state=DISABLED)
    for box in dessert_boxes:
        box.config(state=DISABLED)

    for v in food_variables:
        v.set(0)
    for v in drink_variables:
        v.set(0)
    for v in dessert_variables:
        v.set(0)

    var_food_cost.set('')
    var_drink_cost.set('')
    var_dessert_cost.set('')
    var_subtotal.set('')
    var_taxes.set('')
    var_total.set('')


# initialize tkinter
application = Tk()

# window size 630
application.geometry('1120x630+0+0')

# disable maximizing
application.resizable(False, False)

# window title
application.title("DANIEL'S RESTAURANT - BILLING SYSTEM")

# window background color
application.config(bg='LightGreen')

# top panel
top_panel = Frame(application, bd=2, relief=RAISED)
top_panel.pack(side=TOP)

# title label
title_label = Label(top_panel, text='Billing System', fg='blue1',
                    font=('Dosis', 58), bg='LightGreen', width=22)
title_label.grid(row=0, column=0)

# left panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# cost panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='blue1', padx=50)
cost_panel.pack(side=BOTTOM)

# food panel
food_panel = LabelFrame(left_panel, text='Food', font=('Dosis', 19, 'bold'),
                        bd=1, relief=FLAT, fg='blue1')
food_panel.pack(side=LEFT)

# drinks panel
drinks_panel = LabelFrame(left_panel, text='Drinks', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='blue1')
drinks_panel.pack(side=LEFT)

# desserts panel
desserts_panel = LabelFrame(left_panel, text='Desserts', font=('Dosis', 19, 'bold'),
                            bd=1, relief=FLAT, fg='blue1')
desserts_panel.pack(side=LEFT)

# right panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='LightGreen')
calculator_panel.pack()

# receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg='LightGreen')
receipt_panel.pack()

# buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg='LightGreen')
buttons_panel.pack()

# product lists
food_list = ['Beef', 'Chicken', 'Seafood', 'Pasta', 'Kebab', 'Tacos', 'Sushi', 'Pizza']
drink_list = ['Water', 'Juice', 'Soda', 'Milkshake', 'Aguas', 'Beer', 'Wine', 'Coffee']
dessert_list = ['Ice Cream', 'Cake', 'Crepes', 'Brownie', 'Fruit', 'Flan', 'Cake2', 'Volcano']

# generate food items
food_variables = []
food_boxes = []
food_text = []
counter = 0
for food in food_list:

    # create checkbuttons
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       font=('Dosis', 19, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=food_variables[counter],
                       command=check_checkbox)
    food.grid(row=counter,
              column=0,
              sticky=W)

    # create entry fields
    food_boxes.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_boxes[counter] = Entry(food_panel,
                                  font=('Dosis', 18, 'bold'),
                                  bd=1,
                                  width=4,
                                  state=DISABLED,
                                  textvariable=food_text[counter])
    food_boxes[counter].grid(row=counter,
                               column=1)
    counter += 1

# generate drink items
drink_variables = []
drink_boxes = []
drink_text = []
counter = 0
for drink in drink_list:

    # create checkbuttons
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drinks_panel,
                        text=drink.title(),
                        font=('Dosis', 19, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=drink_variables[counter],
                        command=check_checkbox)
    drink.grid(row=counter,
               column=0,
               sticky=W)

    # create entry fields
    drink_boxes.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_boxes[counter] = Entry(drinks_panel,
                                   font=('Dosis', 18, 'bold'),
                                   bd=1,
                                   width=4,
                                   state=DISABLED,
                                   textvariable=drink_text[counter])
    drink_boxes[counter].grid(row=counter,
                                column=1)
    counter += 1

# generate dessert items
dessert_variables = []
dessert_boxes = []
dessert_text = []
counter = 0
for dessert in dessert_list:

    # create checkbuttons
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(desserts_panel,
                          text=dessert.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=dessert_variables[counter],
                          command=check_checkbox)
    dessert.grid(row=counter,
                 column=0,
                 sticky=W)

    # create entry fields
    dessert_boxes.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_boxes[counter] = Entry(desserts_panel,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=4,
                                     state=DISABLED,
                                     textvariable=dessert_text[counter])
    dessert_boxes[counter].grid(row=counter,
                                  column=1)
    counter += 1

# variables
var_food_cost = StringVar()
var_drink_cost = StringVar()
var_dessert_cost = StringVar()
var_subtotal = StringVar()
var_taxes = StringVar()
var_total = StringVar()


# cost labels and input fields
label_food_cost = Label(cost_panel,
                        text='Food Cost',
                        font=('Dosis', 12, 'bold'),
                        bg='blue',
                        fg='white')
label_food_cost.grid(row=0, column=0)

text_food_cost = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_food_cost)
text_food_cost.grid(row=0, column=1, padx=41)

label_drink_cost = Label(cost_panel,
                         text='Drink Cost',
                         font=('Dosis', 12, 'bold'),
                         bg='blue',
                         fg='white')
label_drink_cost.grid(row=1, column=0)

text_drink_cost = Entry(cost_panel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_drink_cost)
text_drink_cost.grid(row=1, column=1, padx=41)

label_dessert_cost = Label(cost_panel,
                           text='Dessert Cost',
                           font=('Dosis', 12, 'bold'),
                           bg='blue',
                           fg='white')
label_dessert_cost.grid(row=2, column=0)

text_dessert_cost = Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_dessert_cost)
text_dessert_cost.grid(row=2, column=1, padx=41)

label_subtotal = Label(cost_panel,
                       text='Subtotal',
                       font=('Dosis', 12, 'bold'),
                       bg='blue',
                       fg='white')
label_subtotal.grid(row=0, column=2)

text_subtotal = Entry(cost_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3, padx=41)

label_taxes = Label(cost_panel,
                    text='Taxes',
                    font=('Dosis', 12, 'bold'),
                    bg='blue',
                    fg='white')
label_taxes.grid(row=1, column=2)

text_taxes = Entry(cost_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=var_taxes)
text_taxes.grid(row=1, column=3, padx=41)

label_total = Label(cost_panel,
                    text='Total',
                    font=('Dosis', 12, 'bold'),
                    bg='blue',
                    fg='white')
label_total.grid(row=2, column=2)

text_total = Entry(cost_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=var_total)
text_total.grid(row=2, column=3, padx=41)

# buttons
buttons = ['Total', 'Receipt', 'Save', 'Reset']
created_buttons = []
columns = 0
for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=('Dosis', 14, 'bold'),
                    fg='white',
                    bg='blue1',
                    bd=1,
                    width=9)

    created_buttons.append(button)
    button.grid(row=0, column=columns)
    columns += 1

created_buttons[0].config(command=calculate_total)
created_buttons[1].config(command=generate_receipt)
created_buttons[2].config(command=save_receipt)
created_buttons[3].config(command=reset)

# receipt area
receipt_text = Text(receipt_panel,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=52,
                    height=11)
receipt_text.grid(row=0, column=0)

# calculator
calculator_display = Entry(calculator_panel,
                           font=('Dosis', 19, 'bold'),
                           width=33,
                           bd=1)
calculator_display.grid(row=0, column=0, columnspan=4)

calculator_buttons = ['7', '8', '9', '+', '4', '5', '6', '-',
                      '1', '2', '3', 'x', 'R', 'B', '0', '/']
stored_buttons = []

row = 1
column = 0
for button in calculator_buttons:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=('Dosis', 16, 'bold'),
                    fg='white',
                    bg='blue1',
                    bd=3,
                    width=8)

    stored_buttons.append(button)
    button.grid(row=row, column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

stored_buttons[0].config(command=lambda: click_button('7'))
stored_buttons[1].config(command=lambda: click_button('8'))
stored_buttons[2].config(command=lambda: click_button('9'))
stored_buttons[3].config(command=lambda: click_button('+'))
stored_buttons[4].config(command=lambda: click_button('4'))
stored_buttons[5].config(command=lambda: click_button('5'))
stored_buttons[6].config(command=lambda: click_button('6'))
stored_buttons[7].config(command=lambda: click_button('-'))
stored_buttons[8].config(command=lambda: click_button('1'))
stored_buttons[9].config(command=lambda: click_button('2'))
stored_buttons[10].config(command=lambda: click_button('3'))
stored_buttons[11].config(command=lambda: click_button('*'))
stored_buttons[12].config(command=get_result)
stored_buttons[13].config(command=clear)
stored_buttons[14].config(command=lambda: click_button('0'))
stored_buttons[15].config(command=lambda: click_button('/'))

# prevent the window from closing
application.mainloop()
