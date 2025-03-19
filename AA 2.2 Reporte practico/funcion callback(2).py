
def descargar_archivo(url, callback):
    print(f"Descargando archivo desde {url}...")

    import time
    time.sleep(3)
    
    archivo_descargado = "contenido_del_archivo.txt"

    callback(archivo_descargado)

def manejar_archivo(archivo):
    print("Callback ejecutado. Archivo descargado:", archivo)

descargar_archivo("http://cimapat.com/archivo.txt", manejar_archivo)