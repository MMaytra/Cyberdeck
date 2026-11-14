import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import platform
import subprocess


# COLORES #####################################################################

FONDO = "#081010"
PANEL = "#0D1818"
CYAN = "#4DD8D8"
CYAN_OSCURO = "#173A3A"
ROJO = "#E85B5B"
BLANCO = "#D7FFFF"

FUENTE = "OCR A Extended"


# FUNCIONES ###################################################################

def actualizar_hora(label_hora):
    hora = datetime.now().strftime("%H:%M:%S")
    label_hora.config(text=hora)

    #volver a ejecutar dentro de 1 segundo
    ventana.after(1000, actualizar_hora)


def apagar():
    respuesta = messagebox.askyesno(
        "Apagar",
        "¿Quieres apagar el cyberdeck?"
    )

    if respuesta:

        #Raspberry Pi/Linux
        if platform.system() == "Linux":
            subprocess.run(["sudo", "shutdown", "-h", "now"])

        #pruebas en pc
        else:
            ventana.destroy()


def abrir_codigo():
    print("Abrir menú de código")


def abrir_terminal():
    print("Abrir terminal")


def abrir_robot():
    print("Abrir interfaz del robot")


def abrir_archivos():
    print("Abrir archivos")


def abrir_conexiones():
    print("Abrir conexiones")


def abrir_sistema():
    print("Abrir sistema")


# VENTANA #####################################################################

ventana = tk.Tk()

ventana.title("Cyberdeck")
ventana.attributes("-fullscreen", True)    #para que haga pantalla completa
ventana.geometry("800x480")
#ventana.resizable(False, False)

ventana.configure(bg=FONDO)

#Para salir de fullscreen con ESC
ventana.bind(
    "<Escape>",
    lambda event: ventana.attributes("-fullscreen", False)
)


# BARRA SUPERIOR ##############################################################


# CYBERDECK -------------------------------------------------------------------


# HORA ------------------------------------------------------------------------


# WIFI ------------------------------------------------------------------------


# BOTÓN APAGAR ----------------------------------------------------------------


# CONFIGURACIÓN DE LA CUADRÍCULA ---------------------------------------------



# BOTONES PRINCIPALES #########################################################

# FUNCIÓN PARA CREAR BOTONES --------------------------------------------------



# INICIAR HORA ################################################################

#actualizar_hora()


# BUCLE PRINCIPAL #############################################################

ventana.mainloop()