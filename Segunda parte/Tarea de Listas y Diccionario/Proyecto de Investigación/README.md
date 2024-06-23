# INFORMACIÓN GENERAL
# UNIVERSIDAD NACIONAL DE SAN ANTONIO ABAD DEL CUSCO

## ESCUELA PROFESIONAL DE INGENIERÍA INFORMÁTICA Y DE SISTEMAS

* ABSTRACCIÓN DE DATOS Y OBJETOS

**Proyecto de investigación formativa**

 - profesora: **Mgt. Nila Zonia Acurio Usca**
 - Alumno: **Efrain Vitorino Marin** cod: **160337**
 # Tema: Introducción a Numpy
   ![numpy](numpy.png)
- **La clase de objetos array**
Un array es una estructura de datos de un mismo tipo organizada en forma de tabla o cuadrícula de distintas dimensiones.Las dimensiones de un array también se conocen como ejes. ![array](array.png)
- **Creación de arrays**

    Para crear un array se utiliza la siguiente función de NumPy

 - `np.array(lista)` : Crea un array a partir de la lista o tupla lista y devuelve una referencia a él. El número de dimensiones del array dependerá de las listas o tuplas anidadas en lista:

- Para una lista de valores se crea un array de una dimensión, también conocido como **vector**.

- Para una lista de listas de valores se crea un array de dos dimensiones, también conocido como **matriz**.

- Para una lista de listas de listas de valores se crea un array de tres dimensiones, también conocido como **cubo**.

- Y así sucesivamente. **No hay límite en el número de dimensiones del array** más allá de la memoria disponible en el sistema.