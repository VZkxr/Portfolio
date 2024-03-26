import tkinter as tk
from tkinter import messagebox, Menu, PhotoImage, Label, Button, ttk, font
import encript

# Features
def enc_m_wrapper():
    message = e1.get("1.0", "end-1c")
    result = encript.enc_m(message)
    boxt1.delete("1.0", "end")
    boxt1.insert("1.0", result)

def dec_m_wrapper():
    encm = e2.get("1.0", "end-1c")
    result = encript.dec_m(encm)
    boxt2.delete("1.0", "end")
    boxt2.insert("1.0", result)

def copiar_texto_wrapper():
    texto = boxt1.get("1.0", "end-1c")
    encript.copiar_texto(texto)
    messagebox.showinfo("Éxito", "Texto copiado al portapapeles")

def pegar_texto_wrapper():
    texto = encript.pegar_texto()
    e2.insert(tk.END, texto)


# Design
root = tk.Tk()
root.title("Ghidora")
root.geometry("1120x600")
root.iconbitmap("ghidora.ico")

mImage = PhotoImage(file="ghidim1.png")
mImage = mImage.subsample(5, 5)

m1 = Label(root, image=mImage)
m1.place(x=50, y=20)

font_sf = font.Font(family="SFUIDisplay-Medium", size=10)

# Interface
l1 = Label(root, text="Cifrar un mensaje:")
l1.place(x=50, y=130)
e1 = tk.Text(root, width=40, height=10)
e1.place(x=180, y=130)

boxt1 = tk.Text(root, width=40, height=10)
boxt1.place(x=635, y=130)

l2 = Label(root, text="Descifrar un mensaje:")
l2.place(x=50, y=340)
e2 = tk.Text(root, width=40, height=10)
e2.place(x=180, y=340)

boxt2 = tk.Text(root, width=40, height=10)
boxt2.place(x=635, y=340)

c1 = Label(root, text="© 2016 - 2024 Aarón García / Black Skell Technology", font=font_sf)
c1.pack(side=tk.BOTTOM)

# Buttons
b1 = Button(root, text="Cifrar", bg="pale green", command=enc_m_wrapper)
b1.place(x=550, y=195)

b2 = Button(root, text="Descifrar", bg="tomato", command=dec_m_wrapper)
b2.place(x=541, y=405)

b3_copy = ttk.Button(root, text="Copiar \ncifrado", command=copiar_texto_wrapper)
b3_copy.place(x=1000, y=195)

b4_paste = ttk.Button(root, text="Pegar desde el \nportapapeles", command=pegar_texto_wrapper)
b4_paste.place(x=65, y=405)

# Menubar
menubar = Menu(root)
menubasedat = Menu(menubar, tearoff=0)
menubasedat.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu = Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Resetear campos", command=lambda:[boxt1.delete("1.0", "end"), boxt2.delete("1.0", "end"), e1.delete("1.0", "end-1c"), e2.delete("1.0", "end-1c")])
ayudamenu.add_command(label="Acerca de", command=lambda:messagebox.showinfo(title="INFORMACIÓN", message="Programa Ghidora\nCifrado de mensajes\nCreado por Aarón García\nVersión 1.0\nTecnología Python Tkinter"))
menubar.add_cascade(label="Ayuda", menu=ayudamenu)

root.config(menu=menubar)

root.mainloop()