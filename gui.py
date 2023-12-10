from tkinter import *


class Gui:
    def __init__(self, window):
        self.window = window

        self.frame1 = Frame(self.window)
        self.label_title = Label(self.frame1, text='Simple Calculator!')
        self.label_title.pack()
        self.frame1.pack()

        self.frame2 = Frame(self.window)
        self.frame2.grid(row=0, column=3)
        self.input_a = Entry(self.frame2, width=20)
        self.input_b = Entry(self.frame2, width=20)
        self.label_symbol = Label(self.frame2, text='?')
        self.input_a.pack(column=0)
        self.label_symbol.pack(side='top')
        self.input_b.pack(side='right')
        self.frame2.pack()

        self.frame3 = Frame(self.window)
        self.label_output = Label(self.frame3, text='Output will be shown here')
        self.label_output.pack()
        self.frame3.pack()

        self.frame4 = Frame(self.window)
        self.button_plus = Button(self.frame4, text='+')
        self.button_minus = Button(self.frame4, text='-')
        self.button_mult = Button(self.frame4, text='*')
        self.button_div = Button(self.frame4, text='/')
        self.button_exp = Button(self.frame4, text='^')
        self.button_flat = Button(self.frame4, text='//')
        self.button_mod = Button(self.frame4, text='%')

        self.button_plus.pack(side='left')
        self.button_minus.pack(side='top')
        self.button_mult.pack(side='right')
        self.button_div.pack(side='left')
        self.button_exp.pack(side='top')
        self.button_flat.pack(side='right')
        self.button_mod.pack()

        self.frame4.pack()

        self.frame5 = Frame(self.window)
        self.button_equals = Button(self.frame5, text='=')
        self.button_equals.pack()
        self.frame5.pack()

        def submit(self):
            a = self.input_a.get()
            b = self.input_b.get()