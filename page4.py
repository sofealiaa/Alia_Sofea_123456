import tkinter as tk

class Page4(tk.Frame):
    def __init__(self, root, show_main_menu):
        super().__init__(root, width=400, height=300)
        label = tk.Label(self, text="Page 4", font=('Helvetica', 18))
        label.pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=show_main_menu)
        back_button.pack(pady=10)