#El constructor es un método especial que se ejecuta automáticamente cuando creas un objeto (una instancia)
#  de una clase. En Python, el constructor es __init__.
#Analogía simple

#Imagina que una clase es como un molde para hacer galletas:

#    El molde define la forma (la clase)

 #   El constructor es el proceso de hornear una galleta específica con sus características únicas
class Galleta:
    def __init__(self, sabor, tamaño):  # ← Este es el CONSTRUCTOR
        self.sabor = sabor
        self.tamaño = tamaño
        print(f"¡Galleta de {sabor} creada!")

# Cuando ejecutas esta línea, se llama AUTOMÁTICAMENTE al constructor
mi_galleta = Galleta("chocolate", "grande")  # Imprime: ¡Galleta de chocolate creada!


#¿Qué hace el constructor?

#    Crea el objeto en memoria

#    Inicializa sus atributos con valores específicos

#    Prepara el objeto para ser usado
#¿Por qué se llama "constructor"?

#Porque construye el objeto, estableciendo su estado inicial. Sin constructor, 
# tendrías que construir el objeto manualmente:En resumen

#El constructor es:

 #   Un método que se llama automáticamente al crear un objeto

  #  Su propósito es inicializar los atributos del objeto

   # En Python se llama __init__

    #Garantiza que cada objeto tenga sus datos básicos desde el momento de su creación