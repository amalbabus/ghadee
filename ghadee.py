from tkinter import *
from datetime import datetime
import pytz
print(pytz.all_timezones)
root = Tk()
root.title("ghadee")
root.geometry("300x100")

def clockdisplay():
        
        IST = datetime.now(pytz.timezone('Asia/Kolkata'))
        IRE = datetime.now(pytz.timezone('Europe/Dublin'))
        FIN = datetime.now(pytz.timezone('Europe/Helsinki'))
        DUB = datetime.now(pytz.timezone('Asia/Dubai'))

        i=0
        countryName = {IST:"India",IRE:"Ireland",FIN:"Finland",DUB:"Dubai"}
        clock_list =[IST,IRE,FIN,DUB]
        for countryCode in clock_list:
                j=0
                Label(root, text=countryName[countryCode], background="yellow", width=25).grid(column=j,row=i)
                Label(root, text=countryCode.strftime("%I:%M %P"), background="yellow").grid(column=j+1,row=i)
                i+=1
        Label().after(60000,clockdisplay)


clockdisplay()
root.mainloop()

