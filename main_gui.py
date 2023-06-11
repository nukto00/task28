# Сапунов Андрей Сергеевич
# группа 44-22-122
# вариант 28, см. task.png

from tkinter import *
from main import Calc


class GUI(Frame):

    def __init__(self):
        super().__init__()

        self.entry = None
        self.label3 = None

        bgcolor = '#FFFFFF'

        self.configure(bg=bgcolor)
        self.master.title("Расчет - Сапунов А.С.")
        self.master.geometry("300x280")
        self.master.resizable(0, 0)
        self.master.attributes('-toolwindow', True)
        self.pack(fill=BOTH, expand=True)

        label1 = Label(self, text="Расчет функции", state=NORMAL, bg=bgcolor)
        label1.pack(anchor=NW, padx=10, pady=5)

        image = Label(self, compound='top', bg=bgcolor)
        image.task_image = PhotoImage(file="task.png")
        image['image'] = image.task_image
        image.pack(anchor=NW, padx=10, pady=(0, 20))

        label2 = Label(self, text="Введите X:", state=NORMAL, bg=bgcolor)
        label2.pack(anchor=NW, padx=10, pady=5)

        self.entry = Entry(self, width=50, justify=RIGHT)
        self.entry.configure(background="#FAFAFA")
        self.entry.pack(anchor=NW, padx=10, pady=5)

        button = Button(self, text='Вычислить', command=self.calc)
        button.pack(anchor=NW, padx=10, pady=10)

        self.label3 = Label(self, text="", state=NORMAL, bg=bgcolor, wraplength=260, justify=LEFT)
        self.label3.pack(anchor=NW, padx=10, pady=5)

        self.pack()

    def calc(self):
        x = self.entry.get()

        try:
            res = Calc(x)
            self.label3["text"] = f'Результат: Y={res.y:.10}'
            self.label3.config(fg="green")
        except Exception as e:
            self.label3["text"] = f'Ошибка: {e.args[0]}'
            self.label3.config(fg="red")


def main():

    root = Tk()
    GUI()
    root.mainloop()


if __name__ == '__main__':
    main()
