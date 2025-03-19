
def tarea_asincrona(callback):
    print("Realizando tarea...")
    import time
    time.sleep(2) 
    resultado = "Tarea completada"
    callback(resultado) 

def mi_callback(resultado):
    print("Callback ejecutado:", resultado)

tarea_asincrona(mi_callback)