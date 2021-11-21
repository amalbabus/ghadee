from tkinter import *
from datetime import datetime
import pytz
print(pytz.all_timezones)
root = Tk()
root.title("ghadee")
root.geometry("400x100")



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
                Label(root, text=countryName[countryCode], background="yellow").grid(column=j,row=i)
                Label(root, text= countryCode.strftime("%I:%M"), background="yellow").grid(column=j+1,row=i)
                i+=1
                # clock1Label1 = Label(root, text="India", background="yellow").grid(column=0,row=0)
                # clock2Label1 = Label(root, text= IST.strftime("%I:%M"), background="yellow").grid(column=1,row=0)
                # clock1Label2 = Label(root, text="Ireland", background="yellow").grid(column=0,row=1)
                # clock2Label2 = Label(root, text= IRE.strftime("%I:%M"), background="yellow").grid(column=1,row=1)
        Label().after(60000,clockdisplay)
# clockHeadingLabel.pack()

clockdisplay()
root.mainloop()

