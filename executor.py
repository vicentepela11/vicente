import tkinter as tk
from typing import List
def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=20, background='#fff')
    root.resizable(False, False)
    return root

def make_label(root) -> tk.Tk:
    label = tk.Label(
        root, text='Sem Numeros', anchor='e', justify='right', background='#fff'
    )
    label.config(font=('Arial', 15, 'bold'))
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 5))
    display.config(font=("Helvetica", 40, 'bold',), justify='right', bd=1, relief='flat', background='#fff',
                   highlightthickness=1, highlightcolor='blue')
    display.bind('<Control-a>', display_control_a)
    return display

def display_control_a(event):
     event.widget.select_range(0, 'end')
     event.widget.icursor('end')
     return 'break'

def make_buttons(root) -> List[List[tk.Button]]:
    buttons_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'c'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]
    buttons: list[list[tk.Button]] = []

    for row_index, row_velue in enumerate(buttons_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_velue):
             btn = tk.Button(root, text=col_value, )
             btn.grid(row=row_index, column=col_index, sticky='news', padx=5, pady=5)
             btn.config(font=("Helvetica", 15, 'normal'), pady=40, width=1, background='#f1f2f3',
                        bd=0, highlightthickness=0,  highlightcolor='#ccc', highlightbackground='#ccc',
                        activebackground='#ccc')
             button_row.append(btn)
        buttons.append(button_row)
    return buttons