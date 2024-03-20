import re
import pyperclip
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

root = Tk()
root.title("Ghidora")
root.geometry("1120x600")
root.iconbitmap("ghidora.ico")

#Imagen de encabezado
mImage = PhotoImage(file="ghidim1.png")
mImage = mImage.subsample(5, 5)

m1 = Label(root, image=mImage)
m1.place(x=50, y=20)

# Fuente de letra
font_sf = font.Font(family="SFUIDisplay-Medium", size=10)

enc_v_s = ["oneQ", "oneq", "zeroW", "zerow", "oneE", "onee", 
         "zeroR", "zeror", "oneT", "onet", "zeroY", "zeroy",
         "oneU", "oneu", "zeroI", "zeroi", "oneS", "ones",
         "zeroP", "zerop", "oneA", "onea", "zeroS", "zeros",
         "oneD", "oned", "zeroF", "zerof", "oneG", "oneg",
         "zeroH", "zeroh", "oneJ", "onej", "oneK", "onek",
         "zeroL", "zerol", "oneR", "oner", "zeroZ", "zeroz",
         "oneX", "onex", "zeroC", "zeroc", "oneV", "onev",
         "zeroB", "zerob", "oneN", "onen", "zeroM", "zerom",
         "oneW", "onew", "zeroQ", "zeroq", "oneY", "oney",
         "zeroE", "zeroe", "oneI", "onei", "zeroT", "zerot",
         "oneP", "onep", "zeroU", "zerou", "oneF", "onef",
         "zeroA", "zeroa", "oneH", "oneh", "zeroD", "zerod",
         "oneL", "onel", "zeroG", "zerog", "oneZ", "onez"]

lett_v = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g",
          "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n",
          "Ñ", "ñ", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
          "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", " ", ",", 
          ".", ":", ";", "_", "á", "é", "í", "ó", "ú", "@", "(", ")", "¿", "?",
          "¡", "!", "$", "%", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

dic_v = {lett_v:enc_v_s for (lett_v, enc_v_s) in zip(lett_v, enc_v_s)}   #DICCIONARIO

#### FUNCIONES ####
def enc_m():         #Cifrar mensaje
    message = e1.get("1.0", "end-1c")  # Obtiene el texto del cuadro de entrada
    lista_m = []
    result = ""
    for letra in message:
        lista_m.append(letra)
    for letra in lista_m:
        if letra in dic_v:
            result += dic_v[letra]
    boxt1.delete("1.0", "end")  # Borra el contenido anterior del cuadro de texto
    boxt1.insert("1.0", result)  # Inserta el resultado cifrado en el cuadro de texto

def dec_m():  
    encm = e2.get("1.0", "end-1c")          #Descifrar mensaje
    key_found = []
    pattern = r'(zero|one)([a-zA-Z])'
    matches = re.findall(pattern, encm)
    lista = [match[0] + match[1] for match in matches]
    for encript in lista:
        for key, value in dic_v.items():
            if encript == value:
                key_found.append(key)
    result = ''.join(key_found)
    boxt2.delete("1.0", "end")
    boxt2.insert("1.0", result) 

def exitApp():
    value = messagebox.askquestion("Salir", "¿Está seguro que desea salir del programa?")
    if value == "yes":
        root.destroy()
    else:
        pass

def acerca():
    acerca = """
    Programa Ghidora
    Cifrado de mensajes 
    Creado por Aarón García
    Versión 1.0
    Tecnología Python Tkinter
    """
    messagebox.showinfo(title="INFORMACIÓN", message=acerca)

def cleanCamp():
    boxt1.delete("1.0", "end")
    boxt2.delete("1.0", "end")
    e1.delete("1.0", "end-1c")
    e2.delete("1.0", "end-1c")

def copiar_texto():
    texto = boxt1.get("1.0", "end-1c")  # Obtiene el texto del recuadro de resultados boxt1
    pyperclip.copy(texto)  # Copia el texto al portapapeles
    messagebox.showinfo("Éxito", "Texto copiado al portapapeles")

def pegar_texto():
    texto = pyperclip.paste()  # Obtiene el contenido del portapapeles
    e2.insert(tk.END, texto)  # Inserta el texto en el recuadro de descifrar

##### DISEÑO #####
menubar = Menu(root)
menubasedat = Menu(menubar, tearoff=0)
menubasedat.add_command(label="Salir", command = exitApp)
menubar.add_cascade(label="Inicio", menu = menubasedat)

ayudamenu = Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Resetear campos", command = cleanCamp)
ayudamenu.add_command(label="Acerca de", command = acerca)
menubar.add_cascade(label="Ayuda", menu = ayudamenu)

l1 = Label(root, text="Cifrar un mensaje:")
l1.place(x=50, y=130)
e1 = tk.Text(root, width=40, height=10)
e1.place(x=180, y=130)

l2 = Label(root, text="Descifrar un mensaje:")
l2.place(x=50, y=340)
e2 = tk.Text(root, width=40, height=10)
e2.place(x=180, y=340)

c1 = Label(root, text="© 2016 - 2024 Aarón García / Black Skell Technology", font=font_sf)
c1.pack(side=tk.BOTTOM)

##### CREACIÓN DE BOTONES #####
b1 = Button(root, text="Cifrar", bg="pale green", command=enc_m)
b1.place(x=550, y=195)

b2 = Button(root, text="Descifrar", bg="tomato", command=dec_m)
b2.place(x=541, y=405)

b3_copy = ttk.Button(root, text="Copiar \ncifrado", command=copiar_texto)
b3_copy.place(x=1000, y=195)

b4_paste = ttk.Button(root, text="Pegar desde el \nportapapeles", command=pegar_texto)
b4_paste.place(x=65, y=405)

##### CREACIÓN DE RECUADRO DE RESULTADOS #####
boxt1 = tk.Text(root, width=40, height=10)
boxt1.place(x=635, y=130)

boxt2 = tk.Text(root, width=40, height=10)
boxt2.place(x=635, y=340)

root.config(menu=menubar)
    
root.mainloop()