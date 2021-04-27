Programación Imperativa / programación Procedural

Problema: preparar empanadas
Paradigma: enfoque posible para resolver el problema

Paradigma de Cocinar en Casa (PCC):
    Necesitamos:
        - Ingredientes
        - Horno
        - Tiempo
        - Conocimiento (receta)
        - Heladera (guardar ingredientes)

Paradigma de Pedir Afuera (PPA):
    Necesitamos:
        - Plata
        - Aplicación/Teléfono
        - Heladera (repositorio de teléfonos/imanes)
    Ventajas:
        - Más fácil
    Desventajas:
        - Tenemos menos control (para lo que queremos en la empanada)

Golondrinas
Se le llama ambiente al conjunto de objetos disponibles para usar. En el caso de Anastasia y Pepita, ambos son objetos distintos (tienen distinto "DNI") pero se encuentran en el mismo ambiente: "Golondrinas". Ambos objetos tienen un estado propio, en este caso la energia.
Nos damos cuenta que al volar_en_circulos tanto Anastasia como Pepita pierden 10 de energia, y al comer_alpiste, su energia aumenta en 4 unidades por cada gramo que consume. De esta forma vemos que los dos objetos del ambiente, por mas que sean diferentes, tiene igual comportamiento para ciertas actividades.
El conjunto de mensajes que los objetos entieneden se llama interfaz, es decir todo aquello que le puedo decir que haga.
Con esta nueva golondrina, Roberta, la interfaz paraciera ser la misma ya que entiende los mismos comandos que Anastasia y pepita (volar_en_circulos y volar) pero tiene un comportamiento distinto ya que la energia que requiere para hacer dichas acciones es distinta. Pero ademas de eso, Roberta no come alpiste y escupe fuego, lo que la difernecia de las golondrinas. De esta forma nos damos cuenta que Roberta pertenece a otro ambiente, es un dragon.
                volar_en_circulos   volar   comer_alpiste
Pepita                  x             x           x
Anastasia               x             x           x
Roberta                 x             x           -

Pepita es un objeto, el cual pertenece a la clase Golondrina, es decir, es una instancia de Golondrina.

La principal diferencia entre un metodo y una funcion es que las funciones se invocan como funcion(argumento) mientras que los metodos se evaluan a traves del envio de mensajes objeto.mensaje(argumentos). Por otro lado, los metodos tienen siempre como primer parametro un self, las funciones no. Ademas, los metodos siempre van dentro de una clase pero las funciones van por fuera.