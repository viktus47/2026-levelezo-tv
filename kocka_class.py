import tkinter as tk
from tkinter import ttk, messagebox
import random


class Kockadobas:
    def __init__(self, root):
        self.root = root
        self.root.title("Kockázás")
        self.root.geometry("600x400")
        self. eredmenyek = {i: 0 for i in range(1, 7)}

        self.cim_cimke = ttk.Label(root, text="Kockajáték", font=("Arial", 14, "bold"))
        self.cim_cimke.grid(column=1, row=0, padx=20, pady=20)

        self.dobas_szam = tk.StringVar(value="10")
        self.dobas_szam_be = ttk.Entry(textvariable=self.dobas_szam, width=10)
        self.dobas_szam_be.grid(column=0, row=1, padx=70, pady=20)

        self.dobas_gomb = ttk.Button(text="Dobás", command=self.dobas)
        self.dobas_gomb.grid(column=2, row=1, padx=10, pady=20)

        self.kilepes_gomb = ttk.Button(text="Kilépés", width=10, command=root.destroy)
        self.kilepes_gomb.grid(column=3, row=1, padx=10, pady=20)

        self.dobas_eredmenye = ttk.Label(root, text="Eredmény", font=("Arial", 14, "bold"))
        self.dobas_eredmenye.grid(column=1, row=2, padx=20, pady=10)

    def dobas(self):
        try:
            db = int(self.dobas_szam.get())
        except ValueError:
            messagebox.showerror("Hiba", "Nem sikerült számmá átalakítani!!")
            return
        if not 1 <= db <= 10000:
            messagebox.showerror("Hiba", "A dobások számának 1 és 10000 közé kell esnie!")
            return

        for _ in range(db):
            dobott_ertek = random.randint(1, 6)
            self.eredmenyek[dobott_ertek] += 1

        szoveg = "\n".join(f"{oldal}.  =  {darab}" for oldal, darab in self.eredmenyek.items())

        self.dobas_eredmenye.configure(text=szoveg)

if __name__ == "__main__":
    root = tk.Tk()
    app = Kockadobas(root)
    root.mainloop()