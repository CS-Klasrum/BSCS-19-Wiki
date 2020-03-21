from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Data Structures and Algorithms")
window.geometry('900x900')

#LABEL
lbl1 = Label(window, text="Time Complexity", bg="green")
lbl1.grid(column=1, row=1)

#BUTTON
def clicked1():
    messagebox.showinfo('Definition', 'Algorithmic time complexity is concerned about how fast or slow particular algorithm performs. We define complexity as a numerical function T(n) - time versus the input size n. A given algorithm will take different amounts of time on the same inputs depending on such factors as: processor speed; instruction set, disk speed, brand of compiler and etc.')    
btn1 = Button(window,text='Introduction', fg="green" ,command=clicked1)
btn1.grid(column=1,row=2)



def clicked2():
    messagebox.showinfo('Definition', 'The goal of computational complexity is to classify algorithms according to their performances. We will represent the time function T(n) using the "big-O" notation to express an algorithm runtime complexity. For example, the statement T(n) = O(n2) says that an algorithm has a quadratic time complexity. ')
btn2 = Button(window,text='Asymptotic Notations', fg="green", command=clicked2)
btn2.grid(column=1,row=3)

def clicked3():
	messagebox.showinfo('Definition', 'Big O specifically describes the worst-case scenario, and can be used to describe the execution time required or the space used (e.g. in memory or on disk) by an algorithm..')
btn3 = Button(window, text="Definition of big Oh", fg="green", command=clicked3)
btn3.grid(column=1, row=4)


def clicked4():
	messagebox.showinfo('Definition', 'An algorithm is said to run in constant time if it requires the same amount of time regardless of the input size.')
btn3 = Button(window, text="Constant Time:O(1)", fg="green", command=clicked4)
btn3.grid(column=1, row=5)




def clicked5():

    messagebox.showinfo('Definition', 'An algorithm is said to run in linear time if its time execution is directly proportional to the input size, i.e. time grows linearly as input size increases.')
btn4 = Button(window, text="Linear Time:O(n)", fg="green", command=clicked5)
btn4.grid(column=1, row=6)




def clicked6():

    messagebox.showinfo('Definition', 'An algorithm is said to run in logarithmic time if its time execution is proportional to the logarithm of the input size.')
btn5 = Button(window, text="Logarithmic Time:O(log n)", fg="green", command=clicked6)
btn5.grid(column=1, row=7)




def clicked7():

    messagebox.showinfo('Definition', 'An algorithm is said to run in logarithmic time if its time execution is proportional to the square of the input size.')
btn6 = Button(window, text="Quadratic Time:O(n2)", fg="green", command=clicked7)
btn6.grid(column=1, row=8)



def clicked8():

    messagebox.showinfo('Definition', 'O(2N) denotes an algorithm whose growth doubles with each addition to the input data set. ')
btn7 = (window, text="Exponential Time:O(2n)", fg="green", command=clicked8)
btn7.grid(column=1, row=9)




def clicked9()

    messagebox.showinfo('Definition', 'We need the notation for the lower bound i.e the best-case scenario. A capital omega Ω notation is used in this case. ')
btn8 = (window, text="Definition of big Omega", fg="green", command=clicked9)
btn8.grid(column=1, row=10)




def clicked10()

    messagebox.showinfo('Definition', 'This is used to measure average-case complexity of a particular algorithm, i.e.to find the upper and lower bounds. ')
btn9 = (window, text="Definition of big Theta", fg="green", command=clicked10)
btn9.grid(column=1, row=11)




def clicked11()

    messagebox.showinfo('Definition', 'The term analysis of algorithms is used to describe approaches to the study of the performance of algorithms.')
btn10 = Button(window, text="Analysis of Algorithms", fg="green", command=clicked11)
btn10.grid(column=1, row=12)




def clicked12()

    messagebox.showinfo('Definition', 'Consider a dynamic array stack. In this model push() will double up the array size if there is no enough space. Since copying arrays cannot be performed in constant time, we say that push is also cannot be done in constant time. In this section, we will show that push() takes amortized constant time.')
btn11 = Button(window, text="Amortized Time Complexity", fg="green", command=clicked12)
btn11.grid(column=1, row=13)

window.mainloop()
