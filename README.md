## ST0263, Topicos especiales en Telematica
##
## Estudiante(s): Tomas Atehortua Ceferino, tatehortuc@eafit.edu.co
##
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
##

## MoM and gRPC challenge 02
##
## 1. Breve descripción de la actividad
Realizar el diseño e implementación de mínimo 2 microservicios básicos que ofrecen ambos un servicio al API Gateway y que se deben comunicar por un middleware RPC y por un middleware MOM. Cada uno de los microservicios debe soportar concurrencia, es decir, permitir a más de un proceso remoto comunicarse simultáneamente.

Para la comunicación RPC se debe utilizar el middleware gRPC y para la comunicación MOM utilizará RabbitMQ o Apache Kafka.
A nivel de lógica de negocio, se debe implementar una o más consultas acerca de los recursos que tiene el otro proceso. Se recomienda que a nivel de recursos sean los archivos que cada uno de los procesos representa. Por ahora, solo se compartirá el índice o listado de los archivos que posee, no se trata de transferencia ni de sincronización de archivos. 

Implementará al menos
- Dos (2) servicios: serv1: listar archivos y serv2: buscar uno o más archivos.
- Cada uno de los procesos tendrá un archivo de configuración que leerá dinámicamente cuando suba el proceso. En el archivo de configuración mínimo contendrá:
    - IP sobre la que hará listening (ej: 0.0.0.0)
    - Port sobre el que hará listening (depende del middleware)
    - Directorio sobre el que listará o buscará archivos.
    - Para probar las funcionalidades de cada uno de los procesos, se implementará un API Gateway que expondrá API REST en una tecnología y servidor tradicional de su preferencia (ej: NodeJS-express, Python-Flask).
    - Realice todas las adecuaciones o variantes que desee de acuerdo con sus intereses académicos o profesionales, o impleméntelo como dice el enunciado.

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Todos los servicios fueron implementados. Un cliente puede consumir la API rest para buscar y listar archivos con la ayuda de nuestros servicos, el balanceador de carga funciona correctamente tanto para MOM y GRPC, dando estos respuesta en formato JSON siempre que se les hace request.

### 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
El archivo de configuracion si fue realizado, se hicieron pruebas en amazon aws EC2 corriendo el servicio. Mas sin embargo el script para hacer el Bootstrap cada que la aplicacion se quiere correr en una instancia no esta configurado por el momento. 

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
La arquitectura implentada es la siguiente:
![image](./architecture.png)

El servidor principal es una API REST con los servicios de list_files and find_files, este servidor balancea las peticiones a dos microservicios segun su middleware (MOM y GRPC). El balanceo se hizo mediande round-robin, es decir, una peticion ira al microservicio01 (MOM) y la siguiente al microservicio02 (GRPC) y asi sucesivamente.

En cuanto a buenas practicas se realizaron las siguientes:
- Separacion de depencias
- Nombres significativos
- Evitar duplicacion
- Codigo simple

## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
El ambiente utilizado fue python, por lo que, para la API rest se utilizo Flask y para el middleware MOM, rabbitMQ. 

**Como se compila y ejecuta.**


**Detalles del desarrollo.**


**Detalles técnicos**

**Descripción y como se configuracion**
 los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

**Detalles de la organización del código por carpetas**
 o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
 
**Resultados**
pantallazos 

## 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

<!-- ## IP o nombres de dominio en nube o en la máquina servidor.

### descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

### como se lanza el servidor.

### una mini guia de como un usuario utilizaría el software o la aplicación

### opcionalmente - si quiere mostrar resultados o pantallazos  -->

## 5. otra información que considere relevante para esta actividad.

## Referencias:
Algunos sitios que me fueron de ayuda fueron:
- [RabbitMQ Tutorial](https://www.rabbitmq.com/tutorials/tutorial-six-python.html)
- [Protobufs tutorial](https://www.tutorialspoint.com/protobuf/index.htm)
- [Flask documentation](https://flask.palletsprojects.com/en/2.2.x/tutorial/)
- [Currying](https://en.wikipedia.org/wiki/Currying)