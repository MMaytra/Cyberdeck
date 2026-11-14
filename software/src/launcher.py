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

def actualizar_fecha_hora():

    ahora = datetime.now()

    hora = ahora.strftime("%H:%M:%S")
    fecha = ahora.strftime("%d/%m/%Y")

    label_hora.config(text=hora)
    label_fecha.config(text=fecha)

    # Volver a ejecutar dentro de 1 segundo
    ventana.after(1000, actualizar_fecha_hora)


def apagar():

    respuesta = messagebox.askyesno(
        "Apagar",
        "¿Quieres apagar el cyberdeck?"
    )

    if respuesta:

        # Raspberry Pi / Linux
        if platform.system() == "Linux":
            subprocess.run(
                ["sudo", "shutdown", "-h", "now"]
            )

        # Pruebas en Windows
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
ventana.geometry("800x480")

ventana.configure(
    bg=FONDO
)

# Pantalla completa
ventana.attributes(
    "-fullscreen",
    True
)

# Salir de pantalla completa con ESC
ventana.bind(
    "<Escape>",
    lambda event: ventana.attributes(
        "-fullscreen",
        False
    )
)


# BARRA SUPERIOR ##############################################################

barra_superior = tk.Frame(
    ventana,
    bg=PANEL,
    height=65
)

barra_superior.pack(
    fill="x"
)

barra_superior.pack_propagate(False)


# Usamos GRID para controlar mejor la barra superior

barra_superior.columnconfigure(
    0,
    weight=1
)

barra_superior.columnconfigure(
    1,
    weight=1
)

barra_superior.columnconfigure(
    2,
    weight=1
)


# CYBERDECK -------------------------------------------------------------------

label_titulo = tk.Label(
    barra_superior,
    text="CYBERDECK",
    font=(FUENTE, 20),
    fg=CYAN,
    bg=PANEL
)

label_titulo.grid(
    row=0,
    column=0,
    rowspan=2,
    sticky="w",
    padx=20
)


# FECHA -----------------------------------------------------------------------

label_fecha = tk.Label(
    barra_superior,
    text="00/00/0000",
    font=(FUENTE, 10),
    fg=CYAN,
    bg=PANEL
)

label_fecha.grid(
    row=0,
    column=1,
    sticky="s"
)


# HORA ------------------------------------------------------------------------

label_hora = tk.Label(
    barra_superior,
    text="00:00:00",
    font=(FUENTE, 14),
    fg=BLANCO,
    bg=PANEL
)

label_hora.grid(
    row=1,
    column=1,
    sticky="n"
)


# BOTÓN APAGAR ----------------------------------------------------------------

boton_apagar = tk.Button(
    barra_superior,

    # Símbolo universal de encendido/apagado
    text="⏻",

    # Mejor usar una fuente con soporte para este símbolo
    font=("DejaVu Sans", 22),

    fg=ROJO,
    bg=PANEL,

    activebackground="#301414",
    activeforeground=ROJO,

    relief="flat",
    bd=0,

    command=apagar
)

boton_apagar.grid(
    row=0,
    column=2,
    rowspan=2,

    sticky="e",

    padx=20,
    ipadx=8,
    ipady=4
)


# ZONA PRINCIPAL ##############################################################

frame_principal = tk.Frame(
    ventana,
    bg=FONDO
)

frame_principal.pack(
    fill="both",
    expand=True,
    padx=18,
    pady=18
)


# CONFIGURACIÓN DE LA CUADRÍCULA ##############################################

# "uniform" obliga a que las tres columnas tengan el MISMO tamaño

frame_principal.columnconfigure(
    0,
    weight=1,
    uniform="columnas"
)

frame_principal.columnconfigure(
    1,
    weight=1,
    uniform="columnas"
)

frame_principal.columnconfigure(
    2,
    weight=1,
    uniform="columnas"
)


# Lo mismo con las dos filas

frame_principal.rowconfigure(
    0,
    weight=1,
    uniform="filas"
)

frame_principal.rowconfigure(
    1,
    weight=1,
    uniform="filas"
)


# FUNCIÓN PARA CREAR BOTONES ##################################################

def crear_boton(texto, fila, columna, comando):

    boton = tk.Button(
        frame_principal,

        text=texto,

        # 25 era demasiado grande para 800x480
        font=(FUENTE, 18),

        fg=CYAN,
        bg=PANEL,

        activebackground=CYAN_OSCURO,
        activeforeground=BLANCO,

        relief="solid",
        bd=1,

        command=comando
    )

    boton.grid(
        row=fila,
        column=columna,

        # Ocupa toda la celda
        sticky="nsew",

        padx=7,
        pady=7
    )


# BOTONES PRINCIPALES #########################################################

crear_boton(
    "CÓDIGO",
    0,
    0,
    abrir_codigo
)

crear_boton(
    "TERMINAL",
    0,
    1,
    abrir_terminal
)

crear_boton(
    "ROBOT",
    0,
    2,
    abrir_robot
)

crear_boton(
    "ARCHIVOS",
    1,
    0,
    abrir_archivos
)

crear_boton(
    "CONEXIONES",
    1,
    1,
    abrir_conexiones
)

crear_boton(
    "SISTEMA",
    1,
    2,
    abrir_sistema
)


# INICIAR FECHA Y HORA ########################################################

actualizar_fecha_hora()


# BUCLE PRINCIPAL #############################################################

ventana.mainloop()