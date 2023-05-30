import tkinter as tk
from tkinter import ttk
from ApiResponse import ApiFinance


class TkinterApp:

    def __init__(self):
        self.root = tk.Tk()
        self.api_finance = ApiFinance()
        self.tkinterRun()

   
    def tkinterRun(self):
        self.root.geometry("500x400")
        
        label1 = tk.Label(self.root, text = 'Enter stock ticker').pack()
        stockInput = tk.StringVar(value = 'WPC')
        bar1 = tk.Entry(self.root, textvariable=stockInput, width=50, fg="green", selectbackground='yellow').pack()
        label2 = tk.Label(self.root)
        button1 = tk.Button(self.root, text="search", fg='White', bg='green', height=1, width=10, command=lambda: self.button_func(stockInput,label2)).pack()         
        label2.pack()

        self.root.mainloop()

    def button_func(self, stockInput, label2):
            apiData = self.api_finance.api(stockInput.get())
            label2.config(text = apiData)

    # def apiResponse(self):
    #     TextField = Text(root, bg="Green", height=100, width,)
    

