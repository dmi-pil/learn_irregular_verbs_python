import random
from tkinter import filedialog
from tkinter.filedialog import *

root = Tk()
root.title("Do learn English irregular verbs")
root.geometry('570x125')
root.resizable(width=False, height=False)

word = ''

def open_files():
    files = filedialog.askopenfilename(initialdir="/", title="Select file",
                                     filetypes=(("txt", "*.txt"), ("all files", "*.*")))
    temp = []
    f = open(files,'r')
    for i in f.readlines():
        temp.append(i)
    f.close()

    f = open('verbs.txt', 'w')
    f.writelines(temp)
    f.close()

def read_file():
    temp = []
    if os.path.isfile("verbs.txt"):
        f = open("verbs.txt", 'r')
        for i in f.readlines():
            temp.append(i)
        f.close()
        return temp

def question(event):
    global word

    if os.path.isfile("verbs.txt"):
        temp = read_file()
        word = random.choice(temp)
        word = word.split(",")
        Label_output['text'] = word[3]
        Label_verb1_output["text"] = " "
        Label_verb2_output["text"] = " "
        Label_verb3_output["text"] = " "

        entry_verbs1_input.delete(0, END)
        entry_verbs2_input.delete(0, END)
        entry_verbs3_input.delete(0, END)
        Label_verbtest_output["text"] = " "
    else:
        Label_output['text'] = 'Absent file verbs.txt'

def chek(event):
    if os.path.isfile("verbs.txt"):
        verb1 = entry_verbs1_input.get()
        verb2 = entry_verbs2_input.get()
        verb3 = entry_verbs3_input.get()
        verb = verb1 + " " + verb2 + " " + verb3
        verb = verb.split(" ")
        if len(word) != 0:
            if verb[0] == word[0]:
                Label_verb1_output["text"] = "ok"
            else:
                Label_verb1_output["text"] = "no"
            if verb[1] == word[1]:
                Label_verb2_output["text"] = "ok"
            else:
                Label_verb2_output["text"] = "no"
            if verb[2] == word[2]:
                Label_verb3_output["text"] = "ok"
            else:
                Label_verb3_output["text"] = "no"

            Label_verbtest_output["text"] = word[:-1]
        else:
            Label_output['text'] = 'Click the button Begin'
    else:
        Label_output['text'] = 'Absent file verbs.txt'




def close_win():
    root.destroy()

m = Menu(root)
root.config(menu=m)
fm = Menu(m, tearoff=0)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open...", command=open_files)
fm.add_command(label="Exit", command=close_win)

frame_1 = Frame(root,bg = "black",bd = 1)
frame_1.grid(row = 1,column =2)
frame_2 = Frame(root,bg = "black",bd = 1)
frame_2.grid(row = 2,column =2)
frame_3 = Frame(root,bg = "black",bd = 1)
frame_3.grid(row = 3,column =2)
frame_4 = Frame(root,bg = "black",bd = 1)
frame_4.grid(row = 4,column =1)
frame_5 = Frame(root,bg = "black",bd = 1)
frame_5.grid(row = 0,column =1)

Label_input = Label(root, text='Read and translate')
Label_input.grid(column=0, row=0, sticky='w')

Label_input = Label(root, text='Write 3 forms irregular verbs')
Label_input.grid(column=0, row=1, sticky='w')

entry_verbs1_input = Entry(root)
entry_verbs1_input.grid(row=1, column=1, sticky='w')

entry_verbs2_input = Entry(root)
entry_verbs2_input.grid(row=2, column=1, sticky='w')

entry_verbs3_input = Entry(root)
entry_verbs3_input.grid(row=3, column=1, sticky='w')

Label_output = Label(frame_5, width=40, bg="white", fg="black", height = 2)
Label_output.grid(column=1, row=0, sticky='w')

Label_verb1_output = Label(frame_1, width=5, bg="white", fg="black")
Label_verb1_output.grid(column=2, row=1)

Label_verb2_output = Label(frame_2, width=5, bg="white", fg="black")
Label_verb2_output.grid(column=2, row=2)

Label_verb3_output = Label(frame_3, width=5, bg="white", fg="black")
Label_verb3_output.grid(column=2, row=3)

Label_verbtest_output = Label(frame_4, width=40, bg="white", fg="black")
Label_verbtest_output.grid(column=1, row=4)

Button_input = Button(root, text='Begin')
Button_input.grid(column=2, row=0)
Button_input.bind("<Button-1>", question)

Button_input = Button(root, text='check')
Button_input.grid(column=2, row=4)
Button_input.bind("<Button-1>", chek)

root.mainloop()
