from currency_converter import CurrencyConverter
import tkinter as tk # for making desktop application

a = CurrencyConverter() #here currencyconverter funtion is called and stored in the variable a
# print(a.convert(12,"USD","INR")) # covert amount 12 from USD to INR

window = tk.Tk()
window.geometry("500x350") # size of the app window LXB

def clicked():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data = a.convert(amount,cur1,cur2)
    l5 = tk.Label(window,text= data).place(x = 230, y = 290 )

l1=tk.Label(window,text="Personal Currrency Converter", font= "Times 14 bold").place(x = 100, y = 30)
l2=tk.Label(window,text="Enter Amount : ", font= "Times 14 bold").place(x=50, y=80)
#e1 = tk.Entry(window).place(x = 300, y = 80)
e1 = tk.Entry(window)

l3=tk.Label(window,text="Enter Currrency :", font= "Times 14 bold").place(x = 50, y = 130)
#e2 = tk.Entry(window).place(x = 300, y = 130)
e2 = tk.Entry(window)

l4=tk.Label(window,text="Enter Required Currrency :", font= "Times 14 bold").place(x = 50, y = 170)
#e3 = tk.Entry(window).place(x = 300, y = 170)
e3 = tk.Entry(window)

b1 = tk.Button(window,text="click", command=clicked).place(x = 230, y = 240)
e1.place(x = 300, y = 90)
e2.place(x = 300, y = 130)
e3.place(x = 300, y = 170)

window.mainloop() #This will continuosly keep making a window
