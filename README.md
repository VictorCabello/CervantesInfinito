# CervantesInfinito

En este repo pretendo documentar la creacion de mi primer GPT.

Este tendra la intencion de generar texto infinito basado en la forma de escibir 
de cervates en el Quijote.

## Como correr el codigo

- Clonar repo
- Crear virutalenv
- Instalar dependencias
- Correr el archivo `cervantesinfinito/main.py`

## Honor a quie merece

Me estoy basando en el video 
[ Let's Build GPT: from scratch, in code spelled out ]( https://www.youtube.com/watch?v=kCc8FmEb1nY&ab_channel=AndrejKarpathy ).

## Manage dependencies

I use [pip-tools](https://github.com/jazzband/pip-tools), therefore to install the cerrect dependencies just run the next command:

``` sh
$ pip-sync
```

### To add a dependencies

Upudate the requirements.in and then run:

``` sh
$ pip-compile -o requirements.txt pyproject.toml
```
