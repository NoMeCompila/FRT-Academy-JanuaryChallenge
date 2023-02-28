# Free Range Testers Academy January Challenge

En este proyecto se pone en práctica selenium webdriver junto con la libreria pytest para realizar la automatización de pruebas de busquedas en wikipedia.

## Descripción del proyecto

Este proyecto surge como primer desafío mensual para la academia de free range testers en el cual el objetivo es ingresar a wikipedia.org y verificar que una busqueda 
sobre un tema en especifico de los resultados esperados.

## Lenguajes y librerías utilizadas
- python 3.10
- selenium
- pytest
- webdriver-manager
- pytest-xdist
- pytest-html

## Requisitos

- Python 3.x o superior
- Conexión a internet
- Cambiar las rutas absolutas (todavia no descubrí como hacer que funcione en pytest con relative paths)

## Funcionamiento

1) navega a wikipedia.org y verifica el título correcto
2) Se situa en la barra de busqueda y escribe el tema a buscar (Selenium, Appium)
3) Hace click en el boton de la lupa para buscar 
4) Verifica que el título sea el correspondiente al tema buscado
5) Vielve al Homepage y verifica el título

## Instrucciones de uso

Una vez que tenemos todo instalado y configurado podemos setear las opciones de busqueda (archivo data/search_Data.json) y también el navegador (archivo Browsers/config.json) 
simplemente cambiamos el valor de la propiedad browser que por defecto viene con Chrome por las demas que acepta ("Edge", "HEadless Chome", "Firefox").
parP ejecutar la búsqueda en paralelo de las 3 opciones y generar un reporte html ejecutamos el siguiente script en el entorno virtual de la terminal de python:
py.test -m search -n 3 --html=wikireport.html

## Contribuciones

me pueden contactar por el discord de freerangetester aparezco como Fer Caballero o por linkedin que esta en mi inicio de perfil de github y la foto de nirvana de perfil, soy Jr TAE y recien estoy aprendiendo, 
acepto cualquier sugerencia o critica constructiva que crean necesario hacerme saber, así como tambien si quieren preguntarme algo que no sepan de python o selenium 
me pueden contactar  

## Autor

Fernando Caballero 2023 Corrientes Argentina

## Licencia

Usenla como quieran no me importa xd
