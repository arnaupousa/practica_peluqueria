import tkinter as tk

def enviar_pregunta():
    pregunta = entrada_texto.get()
    area_salida.insert(tk.END, f"Tú: {pregunta}\n")
    area_salida.insert(tk.END, "Esperando al Asistente...)\n\n")
    entrada_texto.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Asistente de Peluquería")
ventana.geometry("500x500")

area_salida = tk.Text(ventana, height=20, width=50)
area_salida.pack(pady=10)
area_salida.insert(tk.END, "Bienvenido al Asistente de Peluquería.\nEscribe tu pregunta abajo y presiona 'Enviar'.\n\n")

entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack(pady=10)

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_pregunta)
boton_enviar.pack()

ventana.mainloop()