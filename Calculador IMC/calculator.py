import tkinter as tk
from tkinter import ttk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        edad = int(entry_edad.get())  
        
        
        sexo = combo_sexo.get()
        
        if peso <= 0 or altura <= 0 or edad <= 0:
            resultado.config(text="Error: ingrese valores válidos.")
            return
        
        imc = peso / (altura ** 2)
        
        if sexo == "Hombre": 
            if edad < 18:
                rango_imc = [(16.5, "Peso bajo"), (22.0, "Peso normal"), (27.0, "Sobrepeso"), (30.0, "Obesidad")]
            else:
                rango_imc = [(18.5, "Peso bajo"), (25.0, "Peso normal"), (30.0, "Sobrepeso"), (35.0, "Obesidad")]
        elif sexo == "Mujer":
            if edad < 18:
                rango_imc = [(16.0, "Peso bajo"), (21.0, "Peso normal"), (26.0, "Sobrepeso"), (29.0, "Obesidad")]
            else:
                rango_imc = [(18.0, "Peso bajo"), (24.0, "Peso normal"), (29.0, "Sobrepeso"), (34.0, "Obesidad")]
        else:
            resultado.config(text="Error: seleccione un sexo válido.")
            return
        
        mensaje = ""
        for valor, texto in rango_imc:
            if imc < valor:
                mensaje = texto
                break
        
        if mensaje:
            resultado.config(text=f"Su IMC es {imc:.2f} - {mensaje}")
        else:
            resultado.config(text=f"Su IMC es {imc:.2f} - Obesidad extrema")
    except ValueError:
        resultado.config(text="Error: ingrese números válidos.")

ventana = tk.Tk()
ventana.title("Calculador de IMC")

# Crear fondo de imagen
imagen_fondo = tk.PhotoImage(file="C:/Users/fricb/Downloads/OIP-_3_.png")
canvas = tk.Canvas(ventana, width=imagen_fondo.width(), height=imagen_fondo.height())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=imagen_fondo, anchor="nw")

marco_principal = tk.Frame(ventana, bg="#f4f4f4")
marco_principal.place(relx=0.5, rely=0.5, anchor="center") 

etiqueta_peso = tk.Label(marco_principal, text="Peso (kg):")
etiqueta_peso.grid(row=0, column=0, padx=10, pady=5)

entry_peso = tk.Entry(marco_principal)
entry_peso.grid(row=0, column=1, padx=10, pady=5)

etiqueta_altura = tk.Label(marco_principal, text="Altura (m):")
etiqueta_altura.grid(row=1, column=0, padx=10, pady=5)

entry_altura = tk.Entry(marco_principal)
entry_altura.grid(row=1, column=1, padx=10, pady=5)

etiqueta_edad = tk.Label(marco_principal, text="Edad:")
etiqueta_edad.grid(row=2, column=0, padx=10, pady=5)

entry_edad = tk.Entry(marco_principal)
entry_edad.grid(row=2, column=1, padx=10, pady=5)

etiqueta_sexo = tk.Label(marco_principal, text="Sexo:")
etiqueta_sexo.grid(row=3, column=0, padx=10, pady=5)

combo_sexo = ttk.Combobox(marco_principal, values=["Hombre", "Mujer"])
combo_sexo.current(0)
combo_sexo.grid(row=3, column=1, padx=10, pady=5)

boton_calcular = tk.Button(marco_principal, text="Calcular IMC", command=calcular_imc)
boton_calcular.grid(row=4, columnspan=2, pady=10)

resultado = tk.Label(marco_principal, text="")
resultado.grid(row=5, columnspan=2, pady=5)
# No permitir pantalla completa de la interfaz
ventana.resizable(False, False)

ventana.mainloop()
