import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pytube import YouTube
from threading import Thread

# Función para seleccionar la ubicación de descarga
def seleccionar_directorio():
    global carpeta_destino
    carpeta_destino = filedialog.askdirectory()
    destino_label.config(text=f"Ubicación de descarga: {carpeta_destino}")

# Función para descargar el video
def descargar_video():
    video_url = url_entry.get()

    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        destino = carpeta_destino if carpeta_destino else None

        if not destino:
            messagebox.showerror("Error", "Selecciona una ubicación de descarga.")
            return

        def download_thread():
            video_stream.download(output_path=destino)
            messagebox.showinfo("Éxito", "El video se ha descargado correctamente.")
            progress_bar.stop()

        download_thread = Thread(target=download_thread)
        download_thread.start()
        progress_bar.start()

    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
        progress_bar.stop()

# Configuración de la ventana principal
window = tk.Tk()
window.title("Descargador de Videos de YouTube")

# Etiqueta y entrada para la URL del video
url_label = tk.Label(window, text="URL del video de YouTube:")
url_label.pack()
url_entry = tk.Entry(window, width=40)
url_entry.pack()

# Botón para seleccionar la ubicación de descarga
select_dir_button = tk.Button(window, text="Seleccionar Ubicación", command=seleccionar_directorio)
select_dir_button.pack()

# Etiqueta para mostrar la ubicación de descarga seleccionada
carpeta_destino = ""
destino_label = tk.Label(window, text="")
destino_label.pack()

# Botón para iniciar la descarga
download_button = tk.Button(window, text="Descargar", command=descargar_video)
download_button.pack()

# Barra de progreso de descarga
progress_bar = ttk.Progressbar(window, mode="indeterminate")
progress_bar.pack()

# Ejecutar la ventana principal
window.mainloop()
