import time
import os

def iniciar_app():
    print("------------------------------------------------")
    print("   BIENVENIDO A MI APLICACIÓN AUTOMATIZADA      ")
    print("------------------------------------------------")
    print("Cargando módulos...")
    time.sleep(1) # Simulamos carga
    
    # Aquí iría la lógica real de tu programa
    usuario = input("Por favor, introduce tu nombre: ")
    print(f"Hola, {usuario}. La aplicación se ha lanzado con éxito.")
    
    # Pausa para que la ventana no se cierre inmediatamente
    input("\nPresiona ENTER para cerrar...")

if __name__ == "__main__":
    iniciar_app()