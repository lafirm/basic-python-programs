from tkinter import *


class MyWindow:
    def __init__(self, win):  # a constructor which takes window application object as an argument
        self.lbl1 = Label(win, text='First number')  # creating a label
        self.lbl2 = Label(win, text='Second number')
        self.lbl3 = Label(win, text='Result')
        self.t1 = Entry()  # creating a single line text field
        self.t2 = Entry()
        self.t3 = Entry()
        self.b1 = Button(win, text='Add', command=self.add)  # when we click b1, it calls add function from command
        self.b2 = Button(win, text='Subtract', command=self.sub)  # when we click b2, it calls sub function from command
        # can use self.b2.bind('<Button-1>', self.sub) instead of command parameter
        self.b3 = Button(win, text='Multiply', command=self.mul)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.b3.place(x=300, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, "end")  # to clear the Entry widget after a button is pressed in Tkinter
        """ 
        0 and "end" parameter defines the index of the string,
        0 means starting point, "end" means end of the string,
        "end" and END denotes the same (quotation is must for lower case).
        """
        num1 = int(self.t1.get())  # to get the content of t1 (text field) and convert it into integer
        num2 = int(self.t2.get())  # to get the content of t2 (text field) and convert it into integer
        result = num1+num2
        self.t3.insert(END, str(result))
        """
        insert the result at the end of the string, since END is used,
        you can use "0" too, since we have already cleared the field,
        that's not a problem.
        """

    def sub(self):
        self.t3.delete(0, "end")  # to clear the Entry widget after a button is pressed in Tkinter
        """ 
        0 and "end" parameter defines the index of the string,
        0 means starting point, "end" means end of the string,
        "end" and END denotes the same.
        """
        num1 = int(self.t1.get())  # to get the content of t1 (text field) and convert it into integer
        num2 = int(self.t2.get())  # to get the content of t2 (text field) and convert it into integer
        result = num1-num2
        self.t3.insert(0, str(result))
        """
        insert the result at the start of the string, since 0 is used,
        you can use "end" too, since we have already cleared the field,
        that's not a problem.
        """

    def mul(self):
        self.t3.delete(0, "end")  # to clear the Entry widget after a button is pressed in Tkinter
        num1 = int(self.t1.get())  # to get the content of t1 (text field) and convert it into integer
        num2 = int(self.t2.get())  # to get the content of t2 (text field) and convert it into integer
        result = num1 * num2
        self.t3.insert(0, str(result))


window = Tk()  # creating application object using Tk() function
my_window_object = MyWindow(window)  # instantiating MyWindow Class, it automatically calls the constructor
window.title("Calculator")  # set title for the application
window.geometry("400x300+10+10")  # set size for the application
window.mainloop()  # to enter into event listening loop, w/o this line, our app window won't be displayed
