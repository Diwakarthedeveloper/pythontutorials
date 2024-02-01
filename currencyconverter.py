from currency_converter import CurrencyConverter
import tkinter as tk # for making desktop application

# a = CurrencyConverter() #here currencyconverter funtion is called and stored in the variable a
# print(a.convert(12,"USD","INR")) # covert amount 12 from USD to INR

window = tk.Tk()
window.geometry("400x250") # size of the app window LXB

l1=tk.Label(window,text="Personal Currrency Converter", font= "Times 14 bold").place(x = 50, y = 30)
l2=tk.Label(window,text="enter amount here: ", font= "Times 10 bold").place(x=50, y=80)


window.mainloop() #This will continuosly keep making a window
