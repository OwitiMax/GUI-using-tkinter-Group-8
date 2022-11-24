import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
def browseFiles():
    global filename
    global data
    filename=fd.askopenfilename(initialdir="/",title="select the java file to open",filetypes=(("Text files","*.txt*"),("all files","*.*")))
    filename=open(filename,'r')
    data=filename.read()
    text.insert(END,data)
    filename.close()
def clearText():
    text.delete("1.0","end")
def compilerTest():
    programSymbols = []
    symbols = ['{', '}', '(', ')', '[', ']']
    symbolTuples = [('{', '}'), ('(', ')'), ('[', ']'), ('<', '>')]
    for letter in text.get(1.0,'end'):
        if letter in symbols:
            programSymbols.append(letter)
        elif letter == '<' and programSymbols[-1] != '(':
            programSymbols.append(letter)
        elif letter == '>' and programSymbols[-1] == '<':
            programSymbols.append(letter)
        elif letter == '>' and programSymbols[-1] != '<':
            label1 = Label(root, text="wrong syntax", fg='red', font=('times', 12, 'bold'))
            label1.grid(row=0, column=3)
            return
    for symbolTuple in symbolTuples:
        if programSymbols.count(symbolTuple[0]) != programSymbols.count(symbolTuple[1]):
            print('Missing:',
                  symbolTuple[0] if programSymbols.count(symbolTuple[0]) < programSymbols.count(symbolTuple[1]) else
                  symbolTuple[1])
            break
    else:
        label1 = Label(root, text="Correct Syntax", fg='green', font=('times', 12, 'bold'))
        label1.grid(row=0, column=3)
root=Tk()
root.title('Java compiler')
root.config(bg='#C2B280')
my_font1=('times',12,'bold')
#text=tk.Text(root,height=12)
#text.grid(column=0,row=0,sticky='nsew')
root.resizable(False,False)
root.geometry('800x500')
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='New')
menu.add_separator()
filemenu.add_command(label='Open...',command=browseFiles)
menu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')
#text area
text=tk.Text(root,height=20 ,width=50,font=my_font1)
text.grid(row=0,column=0,pady=1,padx=1,sticky=tk.EW)
font2=('times',18,'bold')
#test button
button_test = Button(root,text="Test Code",padx=20,pady=10,font=font2,command=compilerTest)
button_test.grid(row=0, column=2,padx=15)
#clear button
button_test = Button(root,text="Clear",padx=15,pady=7,command=clearText,font=font2)
button_test.grid(row=1, column=2,padx=70,pady=20)
#adding scrollbar
scrollbar=ttk.Scrollbar(root,orient='vertical',command=text.yview)
scrollbar.grid(row=0,column=1,sticky=tk.NS,padx=2)
#attach the scrollbar to the text widget
text['yscrollcommand']=scrollbar.set(0,1)


mainloop()
