# Nombre: interfaz.py
# Objetivo: Conexión a base de datos, crear un CRUD  y generar PDF en python
# Author: Fernando Manzo Virgen
# 16/07/2019

#Importar 
from tkinter import*
import pymysql
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import itertools
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

#Conexión a la base de datos
def Database():
    global conn, cursor
    conn = pymysql.connect("localhost","root","","automatas")
    cursor = conn.cursor()

# Método para agregar un nuevo usuario
def Create():
    if  FIRSTNAME.get() == "":
        txt_result.config(text="El campo Name está vacío", fg="red")
    else:
        Database()
        cursor.execute('INSERT INTO Alumnos(name) VALUES("{0}")'.format(FIRSTNAME.get()))
        conn.commit()
        FIRSTNAME.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Se ha agregado con éxito", fg="green")

# Método para consultar los datos de la tabla
def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `Alumnos` ORDER BY `name` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1]))
    cursor.close()
    conn.close()
    txt_result.config(text="Se han leído con éxito", fg="black")

# Método para salir de la aplicación
def Exit():
    result = tkMessageBox.askquestion('Python CRUD', '¿Seguro que quiere salir?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

# Método para modificar el nombre de un alumno en base al ID
def Update():
    if  NEWNAME.get() == "":
    	txt_result.config(text="El campo New Name es requerido", fg="red")
    elif ID.get() == "":
    	txt_result.config(text="El campo ID es requerido", fg="red")
    else:
    	Database()
    	cadsqlchange = 'UPDATE Alumnos set name ="{0}"'.format(NEWNAME.get())+'WHERE id ="{0}"'.format(ID.get())
    	cursor.execute(cadsqlchange)
    	conn.commit()
    	FIRSTNAME.set("")
    	ID.set("")
    	NEWNAME.set("")
    	cursor.close()
    	txt_result.config(text="Se ha modificado con éxito", fg="green")



# Método para eliminar un alumno en base al ID
def Delete():
	if  ID.get() == "":
		txt_result.config(text="El campo ID es requerido", fg="red")
	else:
		Database()
		cadsldel = 'DELETE from Alumnos where id ="{0}"'.format(ID.get())
		cursor.execute(cadsldel)
		conn.commit()
		FIRSTNAME.set("")
		ID.set("")
		NEWNAME.set("")
		txt_result.config(text="Se ha eliminado con éxito", fg="green")

# Método para exportar a PDF los datos de la tabla ID
def Pdf():
	result = tkMessageBox.askquestion('Python CRUD', '¿Desea generar el PDF?', icon="question")
	Database()
	if result == 'yes':
		data = [("ID", "NOMBRE")]
		cursor.execute("SELECT * FROM `Alumnos` ORDER BY `name` ASC")
		fetch = cursor.fetchall()
		for dato in fetch:
		    data.append((dato[0], dato[1]))
		export_to_pdf(data)

# Método para iterar		
def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

# Método para pintar los datos en la hoja del PDF
def export_to_pdf(data):
    c = canvas.Canvas("alumnos.pdf", pagesize=A4)
    c.drawString(190, 800, "REPORTE DE ALUMNOS EN ORDEN ALFABETICO")
    c.drawString(245, 780, "Fernando Manzo Virgen")
    c.drawString(410, 760, "16 de julio de 2019")

    w, h = A4
    max_rows_per_page = 40
    # Margen
    x_offset = 185
    y_offset = 100
    # Espacio entre filas
    padding = 15
    
    xlist = [x + x_offset for x in [0, 100, 250]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    
    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()
    c.save()
    txt_result.config(text="Se ha creado el Pdf", fg="green")

# Configuración de la raíz
root = Tk()
root.title("Python CRUD")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 700
height = 350
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

# Variables
FIRSTNAME = StringVar()
ID = StringVar()
NEWNAME = StringVar()
 
# Frame
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
Male = Radiobutton(RadioGroup, text="Male", value="Male", font=('arial', 16)).pack(side=LEFT)
Female = Radiobutton(RadioGroup, text="Female", value="Female", font=('arial', 16)).pack(side=LEFT)
 
# Label
txt_title = Label(Top, width=900, font=('arial', 24), text = "Alumnos")
txt_title.pack()

txt_name = Label(Forms, text="Name:", font=('arial', 16), bd=15)
txt_name.grid(row=0, stick="e")

txt_id = Label(Forms, text="Id:", font=('arial', 16), bd=15)
txt_id.grid(row=1, stick="e")

txt_newname = Label(Forms, text="New Name:", font=('arial', 16), bd=15)
txt_newname.grid(row=2, stick="e")

txt_result = Label(Buttons)
txt_result.pack(side=TOP)
 
# Cajas de texto
name = Entry(Forms, textvariable=FIRSTNAME, width=30)
name.grid(row=0, column=1)

valor = Entry(Forms, textvariable=ID, width=30)
valor.grid(row=1, column=1)

newname = Entry(Forms, textvariable=NEWNAME, width=30)
newname.grid(row=2, column=1)

# Botones
btn_create = Button(Buttons, width=10, text="Create", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=Read )
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update", command=Update)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", command=Delete)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)
btn_pdf = Button(Buttons, width=10, text="PDF", command=Pdf, bg="orange")
btn_pdf.pack(side=LEFT)
 
# Lista de Alumnos
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("Id","Name"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Id', text="Id", anchor=NW)
tree.heading('Name', text="Nombre", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=00)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.pack()

# Bucle de la aplicación
if __name__ == '__main__':
    root.mainloop()