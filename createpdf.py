from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def scan_directory(directory_path):
    files = []
    try:
        # Liste alle Einträge im Verzeichnis
        with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(entry.name)
    except FileNotFoundError:
        print(f"Das Verzeichnis '{directory_path}' existiert nicht.")
    except PermissionError:
        print(f"Keine Berechtigung, das Verzeichnis '{directory_path}' zu lesen.")


def create_pdf_with_image(image_folder, pdf_path="output.pdf"):
    # Erstelle ein Canvas-Objekt mit der gewünschten Seitengröße (z.B. letter)
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Füge ein Bild hinzu
    try:
        for image in scan_directory(directory_path="frames"):
            c.drawImage("{image_folder}", 100, height - 300, width=200, height=150)
    except:
        pass

    # Speichere das PDF
    c.save()


# Pfade zum PDF und Bild

# Erstelle das PDF
create_pdf_with_image(image_folder="frames")
