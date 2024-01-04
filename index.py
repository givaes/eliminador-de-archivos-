import subprocess

def listar_aplicaciones():
    # mdfind para buscar aplicacion
    comando_mdfind = "mdfind kMDItemContentType == 'com.apple.application-bundle'"
    resultado = subprocess.run(comando_mdfind, shell=True, stdout=subprocess.PIPE, text=True)
    
    # lista
    lista_de_aplicaciones = resultado.stdout.splitlines()
    
    # nombre sin ruta completa
    nombres_de_aplicaciones = [aplicacion.split('/')[-1] for aplicacion in lista_de_aplicaciones]
    nombres_de_aplicaciones.sort()
    
    return nombres_de_aplicaciones

def desinstalar_aplicacion(nombre_aplicacion):
    try:
        #comando sudo para eliminar
        comando_eliminar = f"sudo rm -rf '/Applications/{nombre_aplicacion}'"
        subprocess.run(comando_eliminar, shell=True, check=True)
        print(f"Se ha desinstalado {nombre_aplicacion}.")
    except subprocess.CalledProcessError:
        print(f"No se pudo desinstalar {nombre_aplicacion}. Asegúrate de tener permisos de administrador.")

if __name__ == "__main__":
    aplicaciones_instaladas = listar_aplicaciones()
    
    print("Aplicaciones instaladas en tu Mac (ordenadas alfabéticamente):")
    for i, nombre_aplicacion in enumerate(aplicaciones_instaladas):
        print(f"{i + 1}. {nombre_aplicacion}")
    
    nombre_a_desinstalar = input("Ingresa el nombre exacto de la aplicación que deseas desinstalar (o 'salir' para salir): ")
    
    if nombre_a_desinstalar.lower() != "salir":
        if nombre_a_desinstalar in aplicaciones_instaladas:
            desinstalar_aplicacion(nombre_a_desinstalar)
        else:
            print("La aplicación no está instalada en tu Mac.")

