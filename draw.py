
from tkinter import *


class Drawing(object):

    def display(self):

        root = Tk()

        canvas = Canvas(root, width=500, height=500)
        canvas.grid(row=2,  columnspan=5)

        colors_label = Label(root, text='R - Red')
        colors_label.grid(row=0, column=0, padx=2, pady=5, sticky=W+E)
        colors_label.config(background='red', foreground='white')

        colors_label = Label(root, text='G - Green')
        colors_label.grid(row=0, column=1, padx=2, pady=5, sticky=W+E)
        colors_label.config(background='green', foreground='white')

        colors_label = Label(root, text='B - Blue')
        colors_label.grid(row=0, column=2, padx=2, pady=5, sticky=W+E)
        colors_label.config(background='blue', foreground='white')

        colors_label = Label(root, text='A - Black')
        colors_label.grid(row=0, column=3, padx=2, pady=5, sticky=W+E)
        colors_label.config(background='black', foreground='white')

        colors_label = Label(root, text='C - Delete')
        colors_label.grid(row=0, column=4, padx=2, pady=5, sticky=W+E)
        colors_label.config(background='gray30', foreground='white')

        draw_color = 'black'

        def move_mouse(event):

            canvas.create_rectangle(event.x-1, event.y-1, event.x+1,
                                    event.y+1, fill=draw_color, outline=draw_color)

        canvas.bind('<B1-Motion>', move_mouse)

        def key_press(event):
            nonlocal draw_color
            ch = event.char.upper()
            if ch == 'C':
                canvas.delete('all')
            elif ch == 'R':
                draw_color = 'red'
            elif ch == 'G':
                draw_color = 'green'
            elif ch == 'B':
                draw_color = 'blue'
            elif ch == 'A':
                draw_color = 'black'

        canvas.bind('<KeyPress>', key_press)
        canvas.focus_set()

        root.resizable(width=False, height=False)
        root.mainloop()


if __name__ == '__main__':
    app = Drawing()
    app.display()
