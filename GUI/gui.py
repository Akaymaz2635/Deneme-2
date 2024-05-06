from pathlib import Path
from tkinter import filedialog, messagebox
from Function_Service import process_csv_files, apply_inverse_transformation
from Word_Filler import fill_inspection, generate_inspection_result_from_merged_values
import sys
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to handle button1 click event
def select_folder():
    folder_path = filedialog.askdirectory()  # Open folder selection dialog
    if folder_path:  # Check if a folder is selected
        print("Selected folder:", folder_path)


# Function to handle button2 click event
def select_word_document():
    file_path = filedialog.askopenfilename(
        filetypes=[("Word Documents", "*.docx;*.doc")])  # Open file selection dialog for Word documents
    if file_path:  # Check if a file is selected
        print("Selected Word document:", file_path)
        # Here you can save the file_path to use later
        # Display a warning message
        messagebox.showwarning("Uyarı", "Lütfen, en son revizyon IRS dokümanını seçtiğinizden emin olunuz!")

# Function to handle button3 click event
def select_output_folder():
    folder_path = filedialog.askdirectory()  # Open folder selection dialog
    if folder_path:  # Check if a folder is selected
        print("Selected output folder:", folder_path)
        # Assign the folder_path to a variable for later use
        # Example: output_folder_path = folder_path

window = Tk()
window.title("Atos Rapor Birleştirici")
window.iconbitmap("C:/Users/PC/Desktop/Reporter_Project_r2/GUI/assets/frame0/icons8-create-100.ico")  # Set the icon for the window

window.geometry("1288x625")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 625,
    width = 1288,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    632.0,
    792.0,
    fill="#1E275C",
    outline="")

canvas.create_rectangle(
    634.0,
    0.0,
    1288.0,
    792.0,
    fill="#A7A9AC",
    outline="")

canvas.create_text(
    11.0,
    61.0,
    anchor="nw",
    text="Atos Rapor Birleştirici' ye \nHoş Geldiniz!",
    fill="#FFFFFF",
    font=("CourierPrime Regular", 32 * -1)
)

canvas.create_text(
    11.0,
    190.0,
    anchor="nw",
    text="Atos rapor birleştiricisi\nbirden fazla parçaya ait ölçümleri\ntek bir veri setine dönüştürür ve\nIRS doldurmak için kullanır.",
    fill="#FFFFFF",
    font=("CourierPrime Regular", 32 * -1)
)

canvas.create_text(
    769.0,
    61.0,
    anchor="nw",
    text="Detayları belirtiniz.",
    fill="#FFFFFF",
    font=("CourierPrime Regular", 32 * -1)
)

canvas.create_rectangle(
    749.0,
    126.0,
    1204.0,
    216.0,
    fill="#CAC9C9",
    outline="")

canvas.create_rectangle(
    749.0,
    256.0,
    1204.0,
    346.0,
    fill="#CAC9C9",
    outline="")

canvas.create_rectangle(
    749.0,
    386.0,
    1204.0,
    476.0,
    fill="#CAC9C9",
    outline="")

canvas.create_text(
    769.0,
    122.0,
    anchor="nw",
    text="Atos Rapor Dosyaları",
    fill="#FFFFFF",
    font=("CourierPrime Regular", 32 * -1)
)

canvas.create_text(
    769.0,
    252.0,
    anchor="nw",
    text="IRS Dosyaları",
    fill="#FFFFFF",
    font=("CourierPrime Regular", 32 * -1)
)

canvas.create_text(
    769.0,
    386.0,
    anchor="nw",
    text="Çıktı Yolu",
    fill="#FFFFFF",
    font=("CourierPrime Regular", 32 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=select_folder,   # Assign the function
    relief="flat"

)
button_1.place(
    x=1109.0,
    y=158.0,
    width=73.0,
    height=58.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=927.0,
    y=518.0,
    width=80.0,
    height=80.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=select_output_folder,  # Assign the function
    relief="flat"
)
button_3.place(
    x=1109.0,
    y=416.0,
    width=68.0,
    height=60.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=select_word_document,  # Assign the function
    relief="flat"
)
button_4.place(
    x=1109.0,
    y=286.0,
    width=68.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()
