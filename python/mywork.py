# num1 = 20
# num2 = 30
# sum = num1+ num2
# print("sum of" ,num1 ,"and" ,num2, "=", sum )

# num1 = input("first number:")
# num2 = input("second number:")
# sum = float(num1) + float(num2)
# print("sum is" , sum)

# def minimum (a,b):
#   if  a <= b:
#     return a 
#   else:
#       return b
  
# a=4
# b=5
# print(minimum(a,b))
     
# a= 4
# b=3
# c=0
# minimum = min(a,b,c)
# print(minimum)
# import math
# print("the gcd of 20 and 10 is:" , end="")
# print(math.gcd(60, 48))
# def factorial (x):
#     return 1 if(x==1 or x==0) else x* factorial(x-1)
# num = 5
# print("factorial of",num,"is",factorial(num))
    

# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog 
from tkinter import *

import calendar
def showCal() :
	new_gui = Tk()
	new_gui.config(background = "black")
	new_gui.title("CALENDAR")
	new_gui.geometry("550x600")
	fetch_year = int(year_field.get())
	cal_content = calendar.calendar(fetch_year)
	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
	cal_year.grid(row = 5, column = 1, padx = 20)
	new_gui.mainloop()

	
# Driver Code
if __name__ == "__main__" :

	gui = Tk()
	gui.config(background = "white")
	gui.title("CALENDAR")
	gui.geometry("250x140")
	cal = Label(gui, text = "CALENDAR", bg = "dark gray",
							font = ("times", 28, 'bold'))
	year = Label(gui, text = "Enter Year", bg = "light green") 
	year_field = Entry(gui)
	Show = Button(gui, text = "Show Calendar", fg = "Black",
							bg = "Red", command = showCal)
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
	cal.grid(row = 1, column = 1)

	year.grid(row = 2, column = 1)

	year_field.grid(row = 3, column = 1)

	Show.grid(row = 4, column = 1)

	Exit.grid(row = 6, column = 1)
	
	# start the GUI 
	gui.mainloop()
	
