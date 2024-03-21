from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import customtkinter as ctk
from CTkMenuBar import *

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")  

root = ctk.CTk()  
root.geometry("1340x500")
root.resizable(False, False)
root.title("")
root.iconbitmap("images/em_man.ico")

mImage = PhotoImage(file="images/em_man.png")
original_width = mImage.width()
original_height = mImage.height()
new_width = 180
new_height = int((original_height / original_width) * new_width)

# Resize image
mImage = mImage.subsample(int(original_width / new_width), int(original_height / new_height))

m1 = Label(root, image=mImage, borderwidth=0, highlightthickness=0)
m1.place(x=50, y=10)

# Import the tcl file
root.tk.call('source', 'Forest-ttk-theme-master/forest-dark.tcl')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

mId = StringVar()
mReclutado = StringVar()
mNombre = StringVar()
mContacto = StringVar()
mGrado = StringVar()
mEspecialidad = StringVar()
mUbicacion = StringVar()
iConexion = sqlite3.connect('idata.db')
iCursor = iConexion.cursor()

def conexionBBDD():
    try:
        iCursor.execute("""
            CREATE TABLE member (
            id_member INTEGER PRIMARY KEY AUTOINCREMENT,
            recruited TINYINT(1) NOT NULL DEFAULT 0,
            name VARCHAR(50) NOT NULL,
            contact VARCHAR(50) NOT NULL,
            degree VARCHAR(50) NOT NULL,
            specialty VARCHAR(50) NOT NULL,
            location VARCHAR(50) NOT NULL DEFAULT "Desconocido"
            )  
            """)
        messagebox.showinfo("CONEXION", "Base de datos creada exitosamente.")
    except:
        messagebox.showinfo("CONEXION","Conexión exitosa con la base de datos.")

def eliminarBBDD():
    if messagebox.askyesno(message="Los datos se perderán definitivamente, ¿Desea continuar?", title = "ADVERTENCIA"):
        iCursor.execute("DROP TABLE member")
    else:
        pass
    cleanCamp()
    mostrar()

def salirApp():
    valor = messagebox.askquestion("Salir","¿Está seguro que desea salir de la aplicación?")
    if valor=="yes":
        iCursor.close()
        root.destroy()
    else:
        pass

def cleanCamp():
    mId.set("")
    mReclutado.set("")
    mNombre.set("")
    mContacto.set("")
    mGrado.set("")
    mEspecialidad.set("")
    mUbicacion.set("")

def mensaje():
    acerca = """
    Aplicación CRUD
    Creado por Aarón García
    Versión 1.0
    Tecnología Python Tkinter
    """          
    messagebox.showinfo(title="INFORMACIÓN", message=acerca)

###### CRUD #######

def mostrar():
    registros = tree.get_children()
    for i in registros:
        tree.delete(i)
    try:
        iCursor.execute("SELECT * FROM member")
        for row in iCursor:
            tree.insert("",0,text=row[0], values = (row[1], row[2], row[3], row[4], row[5], row[6]))
    except:
        pass

def mostrar_dos():
    try:
        iCursor.execute("SELECT * FROM member")
        registros = tree.get_children()
        for i in registros:
            tree.delete(i)
        for row in iCursor:
            tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))
    except sqlite3.Error:
        messagebox.showerror("ERROR", "Error al mostrar datos. Asegúrate de estar conectado a la base de datos.")

def crear():
    # Check if any element is empty
    if mReclutado.get() == '' or mNombre.get() == '' or mContacto.get() == '' or mGrado.get() == '' or mEspecialidad.get() == '' or mUbicacion.get() == '':
        messagebox.showerror("ERROR", "No se pueden dejar campos vacíos.")
        return

    if mReclutado.get() not in ["0", "1"]:
        messagebox.showerror("Error", "El valor en Reclutado debe ser 0 o 1")
        return
    
    if not mContacto.get().isdigit():
        messagebox.showerror('Error', 'El valor en Contacto debe contener carácteres numéricos')
        return

    try:
        datos = mReclutado.get(), mNombre.get(), mContacto.get(), mGrado.get(), mEspecialidad.get(), mUbicacion.get()
        iCursor.execute("INSERT INTO member VALUES(NULL,?,?,?,?,?,?)", datos)
        iConexion.commit()
        cleanCamp()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al crear el registro, verifique la conexión a la BBDD.")
        pass
    mostrar()

##### TABLE CREATION #####
yScroll = ttk.Scrollbar(root, orient=VERTICAL)
tree = ttk.Treeview(root, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6'), yscrollcommand=yScroll.set)
tree.place(x=0, y=200)

# Position table and vertical scroll bar using grid
tree.grid(row=0, column=0, columnspan=5, pady=200, padx=10)
yScroll.grid(row=0, column=7, sticky="ns", pady=200)

# Associate the scroll bar with the table
yScroll.configure(command=tree.yview)

# Configure columns and headers
tree.column('#0', width=60)
tree.heading('#0', text="ID", anchor='center')

tree.heading('#1', text="Reclutado", anchor='center')
tree.column('#1', anchor='center')

tree.heading('#2', text="Nombre", anchor='center')
tree.column('#2', anchor='center')

tree.heading('#3', text="Contacto", anchor='center')
tree.column('#3', anchor='center')

tree.heading('#4', text="Grado", anchor='center')
tree.column('#4', anchor='center')

tree.heading('#5', text="Especialidad", anchor='center')
tree.column('#5', anchor='center')

tree.heading('#6', text="Ubicación", anchor='center')
tree.column('#6', anchor='center')

##### Scroll #####
yScroll.config(command=tree.yview)

def selectClick(event):
    item = tree.identify('item',event.x,event.y)
    mId.set(tree.item(item, "text"))
    mReclutado.set(tree.item(item, "values")[0])
    mNombre.set(tree.item(item, "values")[1])
    mContacto.set(tree.item(item, "values")[2])
    mGrado.set(tree.item(item, "values")[3])
    mEspecialidad.set(tree.item(item, "values")[4])
    mUbicacion.set(tree.item(item, "values")[5])

tree.bind("<Double-1>", selectClick)

def actualizar():

    if mReclutado.get() == '' or mNombre.get() == '' or mContacto.get() == '' or mGrado.get() == '' or mEspecialidad.get() == '' or mUbicacion.get() == '':
        messagebox.showerror("ERROR", "No se pueden dejar campos vacíos.")
        return

    if mReclutado.get() not in ["0", "1"]:
        messagebox.showerror("Error", "El valor en Reclutado debe ser 0 o 1")
        return
    
    if not mContacto.get().isdigit():
        messagebox.showerror('Error', 'El valor en Contacto debe contener carácteres numéricos')
        return
    
    try:
        datos = mReclutado.get(), mNombre.get(), mContacto.get(), mGrado.get(), mEspecialidad.get(), mUbicacion.get()
        iCursor.execute("UPDATE member SET recruited=?, name=?, contact=?, degree=?, specialty=?, location=? WHERE id_member=" + mId.get(), (datos))
        iConexion.commit()
        mostrar()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al actualizar el registro.")
        pass
    cleanCamp()

def borrar():
    try:
        if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title= "ADVERTENCIA"):
            iCursor.execute("DELETE FROM member WHERE id_member=" + mId.get())
            iConexion.commit()
            mostrar()
    except:
        messagebox.showwarning("ADVERTENCIA", "Ocurrió un error al tratar de eliminar el registro.")
        pass
    cleanCamp()

#### DATA VALIDATION ####
def validate_entry(text):
    return len(text) <= 1


##### DESIGN #####
menu = CTkTitleMenu(master = root, x_offset=40, padx=0, title_bar_color="#303030")
option_1 = menu.add_cascade("Inicio")
option_2 = menu.add_cascade("Ayuda")

dropdown1 = CustomDropdownMenu(widget=option_1, border_width = 0)
dropdown1.add_option(option="Crear/Conectar base de datos", command = conexionBBDD)
dropdown1.add_option(option="Eliminar base de datos", command = eliminarBBDD)
dropdown1.add_separator()
dropdown1.add_option(option="Salir", command = salirApp)

dropdown2 = CustomDropdownMenu(widget=option_2, border_width = 0)
dropdown2.add_option(option="Resetear campos", command= cleanCamp)
dropdown2.add_option(option="Acerca de", command= mensaje)

my_id = Entry(root, textvariable=mId)

l1 = ctk.CTkLabel(master = root, text="Reclutado")
l1.place(x=50, y=70)
e1 = ctk.CTkEntry(master = root, textvariable=mReclutado, width=25)
e1.place(x=115, y=70)
e1.configure(validate="key", validatecommand=(root.register(validate_entry), '%P')) ###!

l2 = ctk.CTkLabel(master = root, text="Nombre")
l2.place(x=50, y=130)
e2 = ctk.CTkEntry(master = root, textvariable=mNombre, width=160)
e2.place(x=115, y=130)

l3 = ctk.CTkLabel(master = root, text="Contacto")
l3.place(x=350, y=70)
e3 = ctk.CTkEntry(master = root, textvariable=mContacto, width=100)
e3.place(x=460, y=70)

l4 = ctk.CTkLabel(master = root, text="Grado académico")
l4.place(x=350, y=130)
e4 = ctk.CTkEntry(master = root, textvariable=mGrado, width=100)
e4.place(x=460, y=130)

l5 = ctk.CTkLabel(master = root, text="Especialidad")
l5.place(x=630, y=70)
e5 = ctk.CTkEntry(master = root, textvariable=mEspecialidad, width=100)
e5.place(x=710, y=70)

l6 = ctk.CTkLabel(master = root, text="Ubicación")
l6.place(x=630, y=130)
e6 = ctk.CTkEntry(master = root, textvariable=mUbicacion, width=100)
e6.place(x=710, y=130)

##### BUTTON CREATION #####
b1 = ctk.CTkButton(master = root, text="Crear registro", fg_color='#1e8c45', command=crear)
b1.place(x=950, y=70)
b2 = ctk.CTkButton(master = root, text="Modificar registro", fg_color='#6d6d75', command=actualizar)
b2.place(x=1125, y=70)
b3 = ctk.CTkButton(master = root, text="Mostrar lista", fg_color='#007542', command=mostrar_dos)
b3.place(x=950, y=130)
b4 = ctk.CTkButton(master = root, text="Eliminar registro", fg_color="#800000", command=borrar)
b4.place(x=1125, y=130)

root.config(menu=menu)
    
root.mainloop()