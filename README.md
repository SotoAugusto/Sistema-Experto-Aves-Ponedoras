
## Demostración



## Abstracto

Los sistemas expertos suelen utilizar conocimientos para razonar sobre los datos de entrada y producir resultados significativos. En la mayoría de los casos, estos conocimientos consisten en reglas simples del tipo "si-entonces", como por ejemplo, si los valores del sensor de temperatura son superiores a 100ºC, se apaga el hervidor eléctrico. 

Las bases de conocimiento y los gráficos siguen desempeñando un papel fundamental en muchos sistemas inteligentes. La gente recorre largas distancias hasta las clínicas o centros médicos, y en la mayoría de ellos escasean los médicos expertos. El resultado es un servicio lento, y los pacientes acaban esperando largas horas sin recibir atención. Por eso, los sistemas médicos expertos pueden desempeñar un papel importante en los casos en los que no se dispone de expertos médicos. Un sistema experto en diagnóstico puede ayudar mucho a identificar esas enfermedades y describir los métodos de tratamiento que deben llevarse a cabo.


#### Características:

- Experta (*antes pyknow*), es la libreria de Python que se utiliza como núcleo del proyecto.
- El motor de inferencias pregunta al usuario síntomas diferentes.
- El usuario escribe *sí* o *no* para cada síntoma.
- El motor intenta determinar la enfermedad basándose en las respuestas del usuario y en reglas predefinidas.
- Una vez encontrada la enfermedad, se muestra al usuario una explicación detallada sobre la enfermedad y los tratamientos.
- Si el síntoma no coincide con una enfermedad concreta, se muestra al usuario la enfermedad que coincida con el mayor número de síntomas.
- La base de conocimiento de enfermedades puede mostrarse como un gráfico bipartito, con las enfermedades en un lado y los síntomas en el otro, que puede visualizarse ejecutando el archivo *knowledge_graph.py*.




## Instalación

Python3 tiene que estar instalado en tu sistema.
Experta solo es compatible con las versiones 3.5 - 3.8 de python.

**Para instalar _experta_:**
```bash
$ sudo pip3 install experta
```



**Para correr el programa principal:**

```bash
$ python3 main.py
```


**Para generar el gráfico de la base de conocimientos:**

```
$ python3 knowledge_graph.py
```



## Referencias
- [Experta](https://pypi.org/project/experta/)

Este proyecto esta enormemente basado en el proyecto de:
**[Smit Shah](https://github.com/smit-1999)**