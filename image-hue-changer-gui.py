import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from tkinter import colorchooser

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.input_folder = ''
        self.output_folder = ''
        self.color = ''
        self.create_widgets()

    def create_widgets(self):
        self.input_folder_label = tk.Label(self.master, text='Select Input Folder:')
        self.input_folder_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.input_folder_entry = tk.Entry(self.master, state='readonly', width=50)
        self.input_folder_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.input_folder_button = tk.Button(self.master, text='Browse', command=self.select_input_folder)
        self.input_folder_button.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        self.output_folder_label = tk.Label(self.master, text='Select Output Folder:')
        self.output_folder_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.output_folder_entry = tk.Entry(self.master, state='readonly', width=50)
        self.output_folder_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.output_folder_button = tk.Button(self.master, text='Browse', command=self.select_output_folder)
        self.output_folder_button.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        self.color_label = tk.Label(self.master, text='Select Color:')
        self.color_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.color_entry = tk.Entry(self.master, state='readonly', width=50)
        self.color_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.color_button = tk.Button(self.master, text='Pick Color', command=self.pick_color)
        self.color_button.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        self.process_button = tk.Button(self.master, text='Process Images', command=self.process_images)
        self.process_button.grid(row=3, column=1, padx=10, pady=10)

    def select_input_folder(self):
        self.input_folder = filedialog.askdirectory()
        self.input_folder_entry.configure(state='normal')
        self.input_folder_entry.delete(0, tk.END)
        self.input_folder_entry.insert(0, self.input_folder)
        self.input_folder_entry.configure(state='readonly')

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        self.output_folder_entry.configure(state='normal')
        self.output_folder_entry.delete(0, tk.END)
        self.output_folder_entry.insert(0, self.output_folder)
        self.output_folder_entry.configure(state='readonly')

    def pick_color(self):
        self.color = colorchooser.askcolor()[1]
        if self.color:
            self.color_entry.configure(state='normal')
            self.color_entry.delete(0, tk.END)
            self.color_entry.insert(0, self.color)
            self.color_entry.configure(state='readonly')


    def process_images(self):
        if not self.input_folder or not self.output_folder or not self.color:
            messagebox.showerror('Error', 'Please select input folder, output folder, and color')
            return

        for filename in os.listdir(self.input_folder):
            if filename.endswith('.png'):
                input_file = os.path.join(self.input_folder, filename)
                output_file = os.path.join(self.output_folder, filename)
                subprocess.call(['magick', 'convert', input_file, '-modulate', '100,0,100', '-fill', self.color, '-tint', '100', output_file])
        messagebox.showinfo('Information', 'Images processed successfully')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Image Huer')
    app = Application(master=root)
    app.mainloop()
