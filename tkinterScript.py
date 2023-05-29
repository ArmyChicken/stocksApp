import tkinter as tk
from tkinter import ttk
from ApiResponse import ApiFinance


class TkinterApp:

    def __init__(self):
        self.root = tk.Tk()
        self.api_finance = ApiFinance()

    def button_func(self, stockInput):
        self.api_finance.api(stockInput.get())

    def tkinterRun(self):
        self.root.geometry("500x400")
        
        label1 = tk.Label(self.root, text = 'Enter stock ticker').pack()
        stockInput = tk.StringVar(value = 'test')
        bar1 = tk.Entry(self.root, textvariable=stockInput, width=50, fg="green", selectbackground='yellow').pack()
        button1 = tk.Button(self.root, text="search", fg='White', bg='green', height=1, width=10, command=lambda: self.button_func(stockInput)).pack()         
        
        self.root.mainloop()
    

