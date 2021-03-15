import tkinter as tk
from typing import List
import re
import math
class calculadora:
    """teste"""
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry,
                 buttons: List[List[tk.Button]]
                 ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons


    def start(self):
        self.config_button()
        self.config_display()
        self.root.mainloop()

    def config_button(self):
        buttons = self.buttons
        for botao in buttons:
            for valor in botao:
                button_text = valor['text']
                if button_text == "c":
                    valor.bind("<Button-1>", self.clear)

                if button_text in '0123456789.+-/*()^':
                    valor.bind("<Button-1>", self.adicionar)

                if button_text == '=':
                    valor.bind("<Button-1>", self.calcular)

    def adicionar(self, event):
        self.display.insert('end', event.widget['text'])

    def clear(self, event=None):
        self.display.delete(0, 'end')

    def Texto_fixo(self, text):
        text = re.sub(r'[^\d \.\-\+\*\/\^\(\)e]', r'', text, 0)
        text = re.sub(r'([\.\-\+\*\^\/])\1', r'\1', text, 0)
        text = re.sub(r'\*?\(\)', '', text)

        return text


    def calcular(self, event=None):
        global textofixo
        textofixo = self.Texto_fixo(self.display.get())
        resultado = self.equacao(textofixo)
        print(resultado)

        try:
            if len(resultado) == 1:
                resul = eval(self.Texto_fixo(resultado[0]))
            else:
                resul = eval(self.Texto_fixo(resultado[0]))
                if textofixo in '^' and textofixo in '+-*/':
                    print('Nao é possivel fazer essas duas contas ao mesmo tempo tipeiro a "^" depois as outras ')
                else:
                    for equacao in resultado[1:]:
                        resul = math.pow(resul, eval(self.Texto_fixo(equacao)))

            self.display.delete(0, 'end')
            self.display.insert('end', resul)
            self.label.config(text=f'{textofixo} = {resul}')

        except OverflowError:
            self.label.config(text='tamanho de numeros execido, sorry')
            self.display.delete(0, 'end')
        except Exception as e:
            print(e)
            self.label.config(text='ouve um erro verifique sua conta ')
            self.display.delete(0, 'end')
    def equacao(self, text):
        return re.split(r'\^', text, 0)
    def config_display(self):
        ...
        # texto_fixo = self.Texto_fixo(self.display.get())

