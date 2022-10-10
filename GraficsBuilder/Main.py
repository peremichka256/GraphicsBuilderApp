# coding: utf-8
from tkinter import *
from tkinter import ttk


clicks = 0


def finish():
    root.destroy()
    print('Окно закрыто')


def print_info(widget, depth=0):
    widget_class = widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("  " * depth + f"{widget_class} width={widget_width}"
                         f" height={widget_height} x={widget_x}"
                         f" y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth + 1)


def click_button():
    global clicks
    clicks += 1
    another_btn['text'] = f'Clicks {clicks}'


if __name__ == '__main__':
    root = Tk()
    root.title("Grafic build")
    root.geometry('800x500+0+0')
    root.resizable(False, False)
    label = Label(text="Hello world")
    label.pack()
    root.protocol('WM_DELETE_WINDOW', finish)
    root.attributes('-alpha', 1)
    root.attributes('-toolwindow', True)

    # Кнопка в обычном ткинтере
    btn = Button(text="Нажми на кнопку, получишь результат")
    btn.pack(anchor=E, padx = 20)

    # Кнопка в ттк
    btn = ttk.Button(text='Ещё одна кнопка', state=['disabled'])
    btn['text'] = 'другой текст'
    btnText = btn['text']
    print(btnText)
    btn.pack(anchor=W, padx = 20)
    another_btn = ttk.Button()
    another_btn.config(text='Очередная кнопка', command=click_button)
    another_btn.pack(side = BOTTOM, fill = X)
    root.update()
    print_info(root)
    root.mainloop()
