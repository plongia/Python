from tkinter import *
from tkinter import ttk


class Calculator:


    def button_pressed(self, value):
        self.existing_value = self.calculator_entry.get()
        self.existing_value += value
        self.calculator_box.delete(0, "end")
        self.calculator_entry.set(self.existing_value)


    def math_button_pressed(self, value):
        if value == "/":
            self.div_trigger = True
        elif value == "*":
            self.multiply_trigger = True
        elif value == "-":
            self.sub_trigger = True
        elif value == "+":
            self.add_trigger = True
        self.calc_value.set(self.calculator_entry.get())
        self.calculator_box.delete(0, "end")

    def clear_button_pressed(self):
        self.add_trigger = False
        self.sub_trigger = False
        self.multiply_trigger = False
        self.div_trigger = False
        self.calculator_box.delete(0, "end")
        self.calculator_entry.set(0)

    def equal_button_pressed(self):
        if self.add_trigger is True:
            self.calculator_entry.set(float(self.calc_value.get()) + float(self.calculator_entry.get()))
        elif self.sub_trigger is True:
            self.calculator_entry.set(float(self.calc_value.get()) - float(self.calculator_entry.get()))
        elif self.multiply_trigger is True:
            self.calculator_entry.set(float(self.calc_value.get()) * float(self.calculator_entry.get()))
        elif self.div_trigger is True:
            self.calculator_entry.set(float(self.calc_value.get()) / float(self.calculator_entry.get()))

    # Creates calculator layout
    def __init__(self):

        # main window
        main_window = Tk()
        main_window.title("Calculator")
        frame = ttk.Frame(main_window, padding="10 10 10 10")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        main_window.rowconfigure(0, weight=1)
        main_window.columnconfigure(0, weight=1)
        main_window.geometry("483x220")

        # calculator window

        self.calculator_entry = StringVar()
        self.calculator_box = ttk.Entry(frame, textvariable=self.calculator_entry)
        self.calculator_box.grid(column=1, row=1, columnspan=4, sticky=(W, E))

        # number buttons

        number_7 = ttk.Button(frame, text="7", command=lambda: self.button_pressed("7"))
        number_7.grid(column=1, row=2, sticky=(W, E))

        number_8 = ttk.Button(frame, text="8", command=lambda: self.button_pressed("8"))
        number_8.grid(column=2, row=2, sticky=(W, E))

        number_9 = ttk.Button(frame, text="9", command=lambda: self.button_pressed("9"))
        number_9.grid(column=3, row=2, sticky=(W, E))

        div_button = ttk.Button(frame, text="/", command=lambda: self.math_button_pressed("/"))
        div_button.grid(column=4, row=2, sticky=(W, E))

        number_4 = ttk.Button(frame, text="4", command=lambda: self.button_pressed("4"))
        number_4.grid(column=1, row=3, sticky=(W, E))

        number_5 = ttk.Button(frame, text="5", command=lambda: self.button_pressed("5"))
        number_5.grid(column=2, row=3, sticky=(W, E))

        number_6 = ttk.Button(frame, text="6", command=lambda: self.button_pressed("6"))
        number_6.grid(column=3, row=3, sticky=(W, E))

        multiply_button = ttk.Button(frame, text="*", command=lambda: self.math_button_pressed("*"))
        multiply_button.grid(column=4, row=3, sticky=(W, E))

        number_1 = ttk.Button(frame, text="1", command=lambda: self.button_pressed("1"))
        number_1.grid(column=1, row=4, sticky=(W, E))

        number_2 = ttk.Button(frame, text="2", command=lambda: self.button_pressed("2"))
        number_2.grid(column=2, row=4, sticky=(W, E))

        number_3 = ttk.Button(frame, text="3", command=lambda: self.button_pressed("3"))
        number_3.grid(column=3, row=4, sticky=(W, E))

        subtraction_button = ttk.Button(frame, text="-", command=lambda: self.math_button_pressed("-"))
        subtraction_button.grid(column=4, row=4, sticky=(W, E))

        clear_button = ttk.Button(frame, text="C/CE", command=self.clear_button_pressed)
        clear_button.grid(column=1, row=5, sticky=(W, E))

        number_0 = ttk.Button(frame, text="0", command=lambda: self.button_pressed("0"))
        number_0.grid(column=2, row=5, sticky=(W, E))

        equal_button = ttk.Button(frame, text="=", command=lambda: self.equal_button_pressed())
        equal_button.grid(column=3, row=5, sticky=(W, E))

        addition_button = ttk.Button(frame, text="+", command=lambda: self.math_button_pressed("+"))
        addition_button.grid(column=4, row=5, sticky=(W, E))

        self.add_trigger = False
        self.sub_trigger = False
        self.multiply_trigger = False
        self.div_trigger = False
        self.existing_value = None
        self.calc_value = StringVar()
        main_window.mainloop()

calc = Calculator()
