from tkinter import*
from datetime import datetime

#print(datetime.now())

def date_time():
    time = datetime.now()
    hr= time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime("%p")

    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    lab_hour.config(text=hr) # to add time in the lable
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_ampm.config(text=am)

    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hour.after(200,date_time)  #this update data after 200 milli sec



clock = Tk()
clock.title('  *****Digital Clock*****   ')
clock.geometry('1000x500') # size of the app window
clock.config(bg='yellow')   # bg is redefined variable here bt pyrhon for background colour

lab_hour=Label(clock,text="00",font=('Time New Roman',60,"bold"), bg = 'red',fg="white")
lab_hour.place(x=40, y =40, height=110,width=100)

lab_hour_txt = Label(clock,text="HOUR",font=('Time New Roman',20,"bold"), bg = 'red',fg="white")
lab_hour_txt.place(x=40, y =160, height=20,width=100)

lab_min = Label(clock,text="00",font=('Time New Roman',60,"bold"), bg = 'red',fg="white")
lab_min.place(x=200, y =40, height=110,width=100)

lab_min_txt = Label(clock,text="MIN",font=('Time New Roman',20,"bold"), bg = 'red',fg="white")
lab_min_txt.place(x=200, y =160, height=20,width=100)

lab_sec = Label(clock,text="00",font=('Time New Roman',60,"bold"), bg = 'red',fg="white")
lab_sec.place(x=400, y =40, height=110,width=100)

lab_sec_txt = Label(clock,text="SEC",font=('Time New Roman',20,"bold"), bg = 'red',fg="white")
lab_sec_txt.place(x=400, y =160, height=20,width=100)

lab_ampm = Label(clock,text="00",font=('Time New Roman',60,"bold"), bg = 'red',fg="white")
lab_ampm.place(x=600, y =40, height=110,width=100)

lab_ampm_txt = Label(clock,text="AM/PM",font=('Time New Roman',20,"bold"), bg = 'red',fg="white")
lab_ampm_txt.place(x=600, y =160, height=20,width=100)

lab_date = Label(clock,text="00",font=('Time New Roman',60,"bold"), bg = 'red',fg="white")
lab_date.place(x=40, y =200, height=110,width=100)

lab_date_txt = Label(clock,text="DATE",font=('Time New Roman',20,"bold"), bg = 'red',fg="white")
lab_date_txt.place(x=40, y =350, height=20,width=100)

lab_month = Label(clock,text="00",font=('Time New Roman',60,"bold"), bg = 'red',fg="white")
lab_month.place(x=200, y =200, height=110,width=100)

lab_month_txt = Label(clock,text="Month",font=('Time New Roman',20,"bold"), bg = 'red',fg="white")
lab_month_txt.place(x=200, y =350, height=20,width=100)

lab_year = Label(clock,text="00",font=('Time New Roman',60,"bold"), bg = 'red',fg="white")
lab_year.place(x=400, y =200, height=110,width=100)

lab_year_txt = Label(clock,text="YEAR",font=('Time New Roman',20,"bold"), bg = 'red',fg="white")
lab_year_txt.place(x=400, y =350, height=20,width=100)

lab_day = Label(clock,text="00",font=('Time New Roman',60,"bold"), bg = 'red',fg="white")
lab_day.place(x=600, y =200, height=110,width=100)

lab_day_txt = Label(clock,text="DAY",font=('Time New Roman',20,"bold"), bg = 'red',fg="white")
lab_day_txt.place(x=600, y =350, height=20,width=100)






date_time()

clock.mainloop()
