from executor import make_root, make_buttons, make_display, make_label
from classescal import calculadora

def main():
    root = make_root()
    label = make_label(root)
    display = make_display(root)
    button = make_buttons(root)
    calcula = calculadora(root, label, display, button)
    calcula.start()



if __name__ == '__main__':
    main()
