import tkinter as tk
from tkinter import ttk, messagebox
import random

def dobas():
    try:
        db = int(dobas_szam.get())
    except:
        messagebox.showinfo("Hiba", "Nem számot adott meg!")
        return

    eredmenyek = [0] * 7
    for _ in range(db):
        eredmenyek[random.randint(1, 6)] +=1
    szoveg =""
    for i in range(1,7):
        szoveg += f"{i}. oldal = {eredmenyek[i]}\n"
    dobas_eredmenye.configure(text=szoveg)

root = tk.Tk()
root.geometry("600x400")
root.title("Kockázás")
root.resizable(False, False)

cim_cimke = ttk.Label(text="Kockajáték", font=("Arial", 14, "bold"))
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