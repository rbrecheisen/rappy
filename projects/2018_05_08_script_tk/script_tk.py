import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


class Ui(object):

    def __init__(self):
        self.dir_path = None
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root, width=300, height=100)
        self.frame.pack()
        self.quitButton = tk.Button(self.frame, text='Quit', command=quit)
        self.quitButton.grid(row=0, column=0)
        self.browseButton = tk.Button(self.frame, text='1. Browse...', command=self.browse)
        self.browseButton.grid(row=0, column=1)
        self.testRenameButton = tk.Button(self.frame, text='2. Test rename...', command=self.test_rename_files)
        self.testRenameButton.grid(row=0, column=2)
        self.renameButton = tk.Button(self.frame, text='3. Rename...', command=self.rename_files)
        self.renameButton.grid(row=0, column=3)

    def show(self):
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        self.root.mainloop()

    def test_rename_files(self):
        count = 0
        for root, dirs, files in os.walk(self.dir_path):
            for f in files:
                if f.startswith('IM_'):
                    count += 1
        messagebox.showinfo('Info', '{} will be renamed'.format(count))

    def rename_files(self):
        count = 0
        for root, dirs, files in os.walk(self.dir_path):
            for f in files:
                if f.startswith('IM_'):
                    f = os.path.join(root, f)
                    f_new = f + '.dcm'
                    os.rename(f, f_new)
                    print('Renamed {} -> {}'.format(f, f_new))
                    count += 1
        messagebox.showinfo('Info', 'Renamed {} files'.format(count))

    def browse(self):
        self.dir_path = filedialog.askdirectory()


if __name__ == '__main__':
    ui = Ui()
    ui.show()
