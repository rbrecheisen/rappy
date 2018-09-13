import tkinter as tk
from tkinter import filedialog


class Application(object):

    def __init__(self):
        self.script_path = None
        self.root = tk.Tk()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        self.script_label = tk.Label(self.main_frame, text='Script: ')
        self.script_label.grid(row=0, sticky=tk.W, columnspan=2)
        self.button_frame = tk.Frame(self.main_frame)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=quit)
        self.quit_button.grid(row=0, column=0, sticky=tk.W)
        self.browse_button = tk.Button(self.button_frame, text='Browse for script...', command=self.browse_script)
        self.browse_button.grid(row=0, column=1, sticky=tk.W)
        self.button_frame.grid(row=1, column=0, sticky=tk.W)

    def run(self):
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        self.root.mainloop()

    def browse_script(self):
        self.script_path = filedialog.askopenfilename()
        self.script_label.config(text='Script: {}'.format(self.script_path))


if __name__ == '__main__':

    application = Application()
    application.run()
