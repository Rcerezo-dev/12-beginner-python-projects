import time

def countdown_timer(seconds):
    """Cuenta regresiva desde el número de segundos especificado."""
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("¡Tiempo terminado!")

countdown_timer(10)  # Inicia una cuenta regresiva de 10 segundos