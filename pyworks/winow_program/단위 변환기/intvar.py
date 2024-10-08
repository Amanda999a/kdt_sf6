from tkinter import *
def click():
    result = value.get()
    text.delete(0.0, END)
    text.insert(END, result)


root = Tk()
root.title("정수형 변수")
root.geometry('200x100')

# 정수형 변수(클래스면 객체) 선언
# value = 10 (일반 변수 - 콘솔에서 변수)
# 윈도우 정수형 객체 선언
value = IntVar()
value.set(10) #10을 설정

Button(root, text="확인", command=click).grid(row=0,column=0)

text = Text(root, width=10, height=2) #영어기준 10자 2줄
text.grid(row=1, column=0)

root.mainloop()
