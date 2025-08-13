from tkinter import *
import ctypes
import io
from contextlib import redirect_stdout
import os


build_dir = os.path.join(os.path.dirname(__file__), "build")
os.environ["PATH"] += os.pathsep + build_dir

#Gets dll containing C++ classes List and Node, as well as a interface of operations.
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "build", "list.dll"))
print("Loading DLL from:", dll_path)
lib = ctypes.CDLL(dll_path)


#Global variables
lista = None
entry1 = None
listbox = None
#Declaring return types to C++ for List Constructor
lib.listcreate.restype = ctypes.c_void_p

#Declaring argument and return types to C++ Functions
lib.listappend.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.listdeleteFirst.argtypes = [ctypes.c_void_p]
lib.listdeleteLast.argtypes = [ctypes.c_void_p]
lib.listprint.argtypes = [ctypes.c_void_p]
lib.listprint.restype = ctypes.c_char_p

#Declaring argument and return types to C++ for List Destructor
lib.listdestroy.argtypes = [ctypes.c_void_p]
lib.listdestroy.restype = ctypes.c_void_p



#Functions for main

#Function that uses C++ List::Listappend 
def submittoList():
   val = int(entry1.get())
   lib.listappend(lista, val)
   entry1.delete(0, END)

#Function that uses C++ List::listprint
def show_list():
    result = lib.listprint(lista)
    result_str = ctypes.string_at(result).decode()

    listbox.delete(0, END)  # clear the Listbox
    for line in result_str.splitlines():
        listbox.insert(END, line.strip())

def delete_first_element():
    lib.listdeleteFirst(lista)
    show_list()

def delete_last_element():
    lib.listdeleteLast(lista)
    show_list()

def deletelist():
    global lista
    lib.listdestroy(lista)
    lista = lib.listcreate()
    show_list()

#Creates window
window = Tk()
window.geometry("1920x1080")
window.title("List Program V1")

#Function that creates window with all widgets
def open_program():

    global lista, entry1, listbox

    list_window = Toplevel(window)
    list_window.title("List Operations")
    list_window.geometry('1920x1080')


    #Creates an object of C++ class type List
    lista = lib.listcreate()

    #Text to insert data below
    label1 = Label(list_window, text="Insert your data below", font=('Arial', 20))
    label1.pack()
    #Space to put information
    entry1 = Entry(list_window)
    entry1.pack()
    entry1.config(font=('Times New Roman', 20))

    #Add button to add to value to list
    buttAdd = Button(list_window, text='Add value to list', command=submittoList, font=('Times New Roman', 10, 'bold'))
    buttAdd.pack()

    #Space to show the list
    listbox = Listbox(list_window, width=50, height=3)
    listbox.pack(pady=10)
    #Button to show the content of the list
    buttShow = Button(list_window, text='Show List', font=('Arial', 10), command=show_list)
    buttShow.pack()

    #Frame to contain both buttons
    buttonFrame = Frame(list_window)
    buttonFrame.pack(pady=10)
    #Button to delete First Element of the List
    buttDeleteFirst = Button(buttonFrame, text = 'Delete First Element', font='Arial, 10', command=delete_first_element)
    buttDeleteFirst.pack(side=LEFT, padx=10)
    #Button to delete Last Element of the List
    buttDeleteLast = Button(buttonFrame, text = 'Delete Last Element', font='Arial, 10', command=delete_last_element)
    buttDeleteLast.pack(side=LEFT, padx=10)

    #Button to delete list
    buttDeleteList = Button(list_window, text = 'Delete List', font='Arial, 10', command=deletelist)
    buttDeleteList.pack()

    

def main_menu():
    window.title("Main Menu")

    mainlabel =Label(window,text='Welcome', font='Arial, 24')
    mainlabel.pack(pady=20)
    mainbut = Button(window, text = 'Enter', font = 'Arial, 30', command=open_program)
    mainbut.pack(anchor=CENTER)

main_menu()
window.mainloop()
