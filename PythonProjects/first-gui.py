

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import datetime as dt


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    192.0,
    251.0,
    image=image_image_1
)

canvas.create_text(
    411.0,
    26.0,
    anchor="nw",
    text="VOGUE",
    fill="#000000",
    font=("Quattrocento", 96 * -1)
)

canvas.create_text(
    444.0,
    112.0,
    anchor="nw",
    text="Innovate. Design. Inspire.",
    fill="#000000",
    font=("Quattrocento", 23 * -1)
)

canvas.create_rectangle(
    432.0,
    204.0,
    732.0,
    249.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    432.0,
    313.0,
    732.0,
    358.0,
    fill="#000000",
    outline="")


window.resizable(False, False)
window.mainloop()
