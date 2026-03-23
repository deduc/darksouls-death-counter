import tkinter as tk
import threading
import keyboard
import os

contador = 0
fichero = "muertes.txt"

def cargar_contador():
    global contador
    if os.path.exists(fichero):
        try:
            with open(fichero, "r", encoding="utf-8") as f:
                contador = int(f.read().strip())
        except:
            contador = 0
    else:
        contador = 0
    etiqueta.config(text=str(contador))

def guardar_contador():
    with open(fichero, "w", encoding="utf-8") as f:
        f.write(str(contador))

def actualizar_etiqueta():
    etiqueta.config(text=str(contador))
    guardar_contador()

def incrementar():
    global contador
    contador += 1
    actualizar_etiqueta()

def decrementar():
    global contador
    contador -= 1
    actualizar_etiqueta()

def sobreescribir():
    global contador
    try:
        valor = entry.get()
        contador = int(valor)
        actualizar_etiqueta()
    except ValueError:
        pass  # Ignorar si no es un número válido
    entry.delete(0, tk.END)   # Limpiar el input
    root.focus()              # Quitar el foco del Entry

def escuchar_teclas():
    keyboard.add_hotkey("alt+f1", lambda: incrementar())
    keyboard.add_hotkey("alt+f2", lambda: decrementar())
    keyboard.wait()

root = tk.Tk()
root.title("Muertes Dark Souls Cabesit4")
root.geometry("400x450")

# === Texto al principio ===
saludo = tk.Label(root, text="Muertes Dark Souls", font=("Arial", 20))
saludo.pack(pady=10)

# === Contador ===
etiqueta = tk.Label(root, text="0", font=("Arial", 50))
etiqueta.pack(pady=20)

# === Botones de incremento/decremento ===
frame_botones = tk.Frame(root)
frame_botones.pack()

btn_menos = tk.Button(frame_botones, text="-1", font=("Arial", 20), command=decrementar)
btn_menos.pack(side="left", padx=10)

btn_mas = tk.Button(frame_botones, text="+1", font=("Arial", 20), command=incrementar)
btn_mas.pack(side="left", padx=10)

# === Entrada para sobrescribir ===
ayuda_text = tk.Label(root, text="Escribir nuevo número de muertes", font=("Arial", 12), fg="grey")
ayuda_text.pack(pady=8)

entry = tk.Entry(root, font=("Arial", 20), justify="center")
entry.pack(pady=4)

btn_set = tk.Button(root, text="Sobreescribir", font=("Arial", 15), command=sobreescribir)
btn_set.pack(pady=10)

# === Texto de ayuda de teclas ===
ayuda_teclas = tk.Label(root, text="Alt + F1 sumar 1\nAlt + F2 restar 1", font=("Arial", 12), fg="black")
ayuda_teclas.pack(pady=10)

# Cargar contador inicial
cargar_contador()

# Listener global
hilo = threading.Thread(target=escuchar_teclas, daemon=True)
hilo.start()

root.mainloop()
