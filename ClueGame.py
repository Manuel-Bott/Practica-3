import random
import tkinter as tk
from tkinter import messagebox

class ClueSimulator:
    def __init__(self):
        self.personajes = {
            "Profesor Plum": "El Profesor Plum estaba en la biblioteca estudiando hasta tarde.",
            "Señorita Scarlet": "La Señorita Scarlet estaba en el jardín cuidando sus rosas.",
            "Coronel Mustard": "El Coronel Mustard estaba en el estudio revisando documentos confidenciales.",
            "Señor Green": "El Señor Green estaba en la cocina preparando la cena.",
            "Doctor Orchid": "La Doctora Orchid estaba en el laboratorio realizando experimentos."
        }
        self.locaciones = ["Casa", "Hotel", "Cuarto", "Cocina", "Jardin"]
        self.armas = ["Candelabro", "Cuerda", "Cuchillo", "Llave Inglesa", "Revolver"]

    def mostrar_historias(self):
        historia_window = tk.Toplevel()
        historia_window.title("Historias de los Personajes")

        historia_label = tk.Label(historia_window, text="Historias de los Personajes:")
        historia_label.pack()

        for personaje, historia in self.personajes.items():
            historia_text = f"{personaje}: {historia}"
            historia_label = tk.Label(historia_window, text=historia_text)
            historia_label.pack()

    def iniciar_partida(self):
        self.root = tk.Tk()
        self.root.title("Simulador de Clue")
        # Establecer el tamaño de la ventana principal
        self.root.geometry("600x400")  # Cambia las dimensiones según lo necesites

        self.mostrar_historias_button = tk.Button(self.root, text="Ver Historias de Personajes", command=self.mostrar_historias)
        self.mostrar_historias_button.pack()

        culpable = {
            "personaje": random.choice(list(self.personajes.keys())),
            "locacion": random.choice(self.locaciones),
            "arma": random.choice(self.armas)
        }

        self.label = tk.Label(self.root, text="Se ha cometido un crimen en la mansión. Debes encontrar al culpable.")
        self.label.pack()

        self.button = tk.Button(self.root, text="Iniciar investigación", command=lambda: self.WHILE_REp(culpable))
        self.button.pack()

        self.root.mainloop()

    def WHILE_REp(self, culpable):
        self.label.config(text="Investiga las pistas y descubre quién lo hizo, dónde y con qué arma.")
        self.label.pack()

        self.button.config(text="Investigar pista", command=lambda: self.investigar_pista(culpable))
        self.button.pack()

        self.button2 = tk.Button(self.root, text="Acusar", command=lambda: self.acusar(culpable))
        self.button2.pack()

        self.button3 = tk.Button(self.root, text="Abandonar la investigación", command=self.root.quit)
        self.button3.pack()

    def investigar_pista(self, culpable):
        pista = random.choice(["personaje", "locacion", "arma"])
        messagebox.showinfo("Pista", f"Has encontrado una pista sobre {pista}: {culpable[pista]}")

    def acusar(self, culpable):
        acusacion_window = tk.Toplevel()
        acusacion_window.title("Hacer Acusación")

        personaje_label = tk.Label(acusacion_window, text="Ingresa el nombre del personaje:")
        personaje_label.pack()
        personaje_entry = tk.Entry(acusacion_window)
        personaje_entry.pack()

        locacion_label = tk.Label(acusacion_window, text="Ingresa el nombre de la locación:")
        locacion_label.pack()
        locacion_entry = tk.Entry(acusacion_window)
        locacion_entry.pack()

        arma_label = tk.Label(acusacion_window, text="Ingresa el nombre del arma:")
        arma_label.pack()
        arma_entry = tk.Entry(acusacion_window)
        arma_entry.pack()

        acusar_button = tk.Button(acusacion_window, text="Acusar", command=lambda: self.verificar_acusacion(acusacion_window, culpable, personaje_entry.get(), locacion_entry.get(), arma_entry.get()))
        acusar_button.pack()

    def verificar_acusacion(self, acusacion_window, culpable, personaje, locacion, arma):
        acusacion = {
            "personaje": personaje,
            "locacion": locacion,
            "arma": arma
        }

        if acusacion == culpable:
            messagebox.showinfo("Resultado", "¡Felicidades! Has atrapado al culpable. ¡Ganaste!")
            
        else:
            messagebox.showinfo("Resultado", "¡Oh no! Tu acusación fue incorrecta. El verdadero culpable sigue suelto.")

        acusacion_window.destroy()
        self.root.quit()

# Iniciar el simulador de Clue
simulador = ClueSimulator()
simulador.iniciar_partida()


