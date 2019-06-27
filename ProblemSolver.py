import tkinter as tk

Large_font = ('Verdana', 12)


class Solver(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)
        container = tk.Frame()

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]

        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Start Page', font=Large_font)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text='Solve Problems', command=controller.destroy)
        button.pack()


app = Solver()
app.geometry('275x80')
app.title('Problem Solver 1.0')
app.mainloop()



