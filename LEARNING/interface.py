from tkinter import *

count = 0
def click():
   global count
   count += 1
   labelforbutton.config(text=count)

def submit():
   username = entry.get()
   labelforsubmit.config(text=username)

def delete():
   entry.delete(0, END)

window = Tk()   #create a window


window.geometry("400x400")   #changes size of window
window.title("Jaco's first window")    #changes title of window
#icon = PhotoImage(file='')    changes logo
#window.iconphoto(True, icon)
window.config(background="red")   #changes color of screen

#widgets

#labels
label = Label(window, 
              text="Hello World", 
              font=('Arial', 40, 'bold'), 
              fg='green', bg='blue',
              relief=RAISED,
              bd=10)
label.pack()

#buttons
button = Button(window, text='Click me!!!')    #create button
button.pack()          #places on window
button.config(command=click)         #performs function given... must be defined before
button.config(font=('Ink Free', 20, 'italic'))    #Changes font of button, size and type of font(bold, italic, etc)
button.config(bg='blue')                           #changes background color of button
button.config(fg='white')                          #changes font color
button.config(activebackground='black')            #changes background when pressed
button.config(activeforeground='red')              #changes font color when pressed
button.config(state=ACTIVE)                        #activates or deactivate button
labelforbutton = Label(window, text=count)        #creates a lable to show the count of clicks
labelforbutton.pack()

#entry field for user input
entry = Entry()
entry.pack()
entry.config(font=('Times New Roman', 30))
entry.config(bg='black')
entry.config(fg='white')
#entry.insert(0, 'Spongebob')
#entry.config(show='*')

submit = Button(window, text="Submit", command=submit)
submit.pack(side = BOTTOM)
labelforsubmit = Label(window, text=entry.get(), font=('Arial', 40, 'bold'))
labelforsubmit.pack()

deleteBut = Button(window, text="Delete", command=delete)
deleteBut.pack(side = BOTTOM)





window.mainloop() #to display window