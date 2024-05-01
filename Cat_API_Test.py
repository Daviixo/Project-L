import tkinter as tk
from PIL import ImageTk, Image
import requests
import io

def abrir_popup(url):
    response = requests.get(url)
    imagen_bytes = response.content

    popup = tk.Toplevel()
    popup.title("Imagen de Gato")

    imagen = Image.open(io.BytesIO(imagen_bytes))
    imagen = imagen.resize((300, 300), Image.BILINEAR)
    imagen_tk = ImageTk.PhotoImage(imagen)

    etiqueta_imagen = tk.Label(popup, image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    etiqueta_imagen.pack()

def main():
    breed = input("Por favor, ingresa la raza de gato: ")

    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed}"

    response = requests.get(url)
    data = response.json()
    url_imagen = data[0]['url']

    abrir_popup(url_imagen)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    main()
    root.mainloop()