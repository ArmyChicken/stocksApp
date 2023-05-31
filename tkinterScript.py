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
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)

        label1 = tk.Label(self.root, text = 'Enter stock ticker').grid(row=1, column=1, sticky='N', pady=2)#.pack()
        stockInput = tk.StringVar(value = 'WPC')
        bar1 = tk.Entry(self.root, textvariable=stockInput, width=50, fg="green", selectbackground='yellow').grid(row=2, column=1, sticky='N', pady=2)#.pack()
        labelCurrency = tk.Label(self.root)
        labelStockPrice = tk.Label(self.root)
        #labelStockPrice.grid(row = 3, column = 0, sticky = 'W', pady =2)
        button1 = tk.Button(self.root, text="search", fg='White', bg='green', height=1, width=10, command=lambda: self.button_func(stockInput,labelCurrency,labelStockPrice)).grid(row=3, column=1, sticky='N', pady=2)#.pack()        
        #labelCurrency.pack()
        #labelStockPrice.pack()
        labelStockPrice.grid(row=4, column=0, sticky='W', pady=2)

        self.root.mainloop()

    def button_func(self, stockInput, labelCurrency,labelStockPrice):
            apiData = self.api_finance.api(stockInput.get())
            #labelCurrency.config(text = apiData['currency'])
            labelStockPrice.config(text = 'Stock price is ' + str(apiData['stockPrice'] )) # + str(apiData['currency'])


