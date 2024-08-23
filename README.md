## Desafío - Métodos y Atributos
Este proyecto es un desafío para demostrar el uso de clases, métodos, y atributos en Python, aplicando conceptos de Programación Orientada a Objetos (POO). El objetivo es desarrollar un prototipo para que los clientes de una cadena de pizzerías puedan autogestionar sus pedidos, permitiendo la selección de ingredientes y tipo de masa para una pizza.

### Descripción del Proyecto
El proyecto permite a los usuarios:

- Seleccionar un ingrediente proteico y dos ingredientes vegetales para su pizza.
- Escoger entre dos tipos de masa: tradicional o delgada.
- Validar si los ingredientes seleccionados están disponibles.
- Confirmar si la pizza creada es válida o no, basándose en las reglas de negocio.
- Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- pizza.py: Contiene la clase Pizza con métodos para la creación y validación de pizzas.
- ingredientes.py: Incluye listas de ingredientes proteicos, vegetales y tipos de masa disponibles.
- evaluaciones.py: Script para realizar pruebas y demostraciones de la clase Pizza y sus funcionalidades.


### Requerimientos
Python 3.6 o superior


### Instalación
1. Clona este repositorio:

git clone https://github.com/tu_usuario/nombre_del_repositorio.git

2. Ve al directorio del proyecto:

cd nombre_del_repositorio


### Estructura del proyecto

El proyecto se puede organizar de la siguiente manera:


bash
/pizza_project
│
├── pizza.py           # Contiene la clase Pizza con métodos y atributos necesarios
├── ingredientes.py    # Contiene las listas de ingredientes y tipos de masa
└── evaluaciones.py    # Realiza evaluaciones y pruebas usando la clase Pizza


### Uso

-Crear una Pizza:

Ejecuta el script evaluaciones.py para interactuar con el programa.
Se te pedirá ingresar un ingrediente proteico, dos ingredientes vegetales y el tipo de masa.

-Validar la Pizza:

El programa validará si la combinación de ingredientes y masa es válida según las reglas predefinidas.
Se mostrará en pantalla si la pizza es válida o no.

-Errores Intencionados:

El script contiene un error intencionado al intentar validar la clase Pizza en lugar de una instancia, lo cual demostrará la diferencia entre atributos de clase y de instancia.

### Autor
Bárbara HA.