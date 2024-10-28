import tkinter as tk
from tkinter import messagebox
import inventario  # Importamos el archivo que maneja el JSON

# Funciones de la interfaz gráfica
def añadir_producto():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()
    
    if not nombre or not cantidad or not precio:
        messagebox.showwarning("Datos incompletos", "Por favor, completa todos los campos.")
        return

    try:
        cantidad = int(cantidad)
        precio = float(precio)
    except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un número entero y el precio un número decimal.")
        return

    inventario_data = inventario.cargar_inventario()
    inventario_data[nombre] = {'cantidad': cantidad, 'precio': precio}
    inventario.guardar_inventario(inventario_data)
    messagebox.showinfo("Producto añadido", f"Producto '{nombre}' añadido correctamente.")
    limpiar_campos()

def actualizar_producto():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()

    if not nombre or not cantidad or not precio:
        messagebox.showwarning("Datos incompletos", "Por favor, completa todos los campos.")
        return

    try:
        cantidad = int(cantidad)
        precio = float(precio)
    except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un número entero y el precio un número decimal.")
        return

    inventario_data = inventario.cargar_inventario()
    if nombre in inventario_data:
        inventario_data[nombre] = {'cantidad': cantidad, 'precio': precio}
        inventario.guardar_inventario(inventario_data)
        messagebox.showinfo("Producto actualizado", f"Producto '{nombre}' actualizado correctamente.")
    else:
        messagebox.showerror("Error", "El producto no existe.")
    limpiar_campos()

def eliminar_producto():
    nombre = entry_nombre.get()

    if not nombre:
        messagebox.showwarning("Datos incompletos", "Por favor, introduce el nombre del producto a eliminar.")
        return

    inventario_data = inventario.cargar_inventario()
    if nombre in inventario_data:
        del inventario_data[nombre]
        inventario.guardar_inventario(inventario_data)
        messagebox.showinfo("Producto eliminado", f"Producto '{nombre}' eliminado correctamente.")
    else:
        messagebox.showerror("Error", "El producto no existe.")
    limpiar_campos()

def mostrar_inventario():
    inventario_data = inventario.cargar_inventario()
    lista_productos.delete(0, tk.END)  # Limpiar la lista
    for nombre, datos in inventario_data.items():
        lista_productos.insert(tk.END, f"{nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Inventario")

# Campos de entrada
tk.Label(ventana, text="Nombre del producto:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Cantidad:").grid(row=1, column=0)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(row=1, column=1)

tk.Label(ventana, text="Precio:").grid(row=2, column=0)
entry_precio = tk.Entry(ventana)
entry_precio.grid(row=2, column=1)

# Botones de acción
tk.Button(ventana, text="Añadir Producto", command=añadir_producto).grid(row=3, column=0)
tk.Button(ventana, text="Actualizar Producto", command=actualizar_producto).grid(row=3, column=1)
tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto).grid(row=4, column=0)
tk.Button(ventana, text="Mostrar Inventario", command=mostrar_inventario).grid(row=4, column=1)

# Lista para mostrar los productos
lista_productos = tk.Listbox(ventana, width=50)
lista_productos.grid(row=5, column=0, columnspan=2)

# Iniciar la interfaz gráfica
ventana.mainloop()
