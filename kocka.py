import tkinter as tk
from tkinter import ttk, messagebox
import random

def dobas():
    try:
        db = int(dobas_szam.get())
    except ValueError:
        messagebox.showerror("Hiba", "Nem sikerült számmá átalakítani!!")
        return
    if not 1 <= db <= 10000:
        messagebox.showerror("Hiba", "A dobások számának 1 és 10000 közé kell esnie!")
        return

    eredmenyek = {i: 0 for i in range(1, 7)}
    for _ in range(db):
        dobott_ertek = random.randint(1, 6)
        eredmenyek[dobott_ertek] += 1

    szoveg ="\n" .join(f"{oldal}.  =  {darab}" for oldal, darab in eredmenyek.items())

    dobas_eredmenye.configure(text=szoveg)

root = tk.Tk()
root.title("Kockázás")
root.geometry("600x400")


cim_cimke = ttk.Label(root, text="Kockajáték", font=("Arial", 14, "bold"))
cim_cimke.grid(column=1, row=0, padx=20, pady=20)

dobas_szam = tk.StringVar(value="10")
dobas_szam_be = ttk.Entry(textvariable=dobas_szam, width=10)
dobas_szam_be.grid(column=0, row=1, padx=70, pady=20)

dobas_gomb = ttk.Button(text="Dobás", command=dobas)
dobas_gomb.grid(column=2, row=1, padx=10, pady=20)

kilepes_gomb = ttk.Button(text="Kilépés", width=10, command=root.destroy)
kilepes_gomb.grid(column=3, row=1, padx=10, pady=20)

dobas_eredmenye = ttk.Label(root, text="Eredmény", font=("Arial", 14, "bold"))
dobas_eredmenye.grid(column=1, row=2, padx=20, pady=10)

root.mainloop()