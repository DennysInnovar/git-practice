# git-practice

Repositorio de práctica para la sesión de Git de los nuevos practicantes.

Cada carpeta dentro de `ejercicios/` corresponde a un ejercicio de la guía
que les compartió su instructor. No necesitan crear nada desde cero: el
contenido ya está preparado, solo tienen que seguir las instrucciones de
la guía sobre estos archivos.

## Estructura

```
git-practice/
├── README.md
├── .gitignore
└── ejercicios/
    ├── 01-basico/
    │   └── notas.txt        → Ejercicio 1: primeros commits
    ├── 02-conflicto/
    │   └── config.txt       → Reto 1: resolver un conflicto real
    │                           (ver ramas feature/config-a y feature/config-b)
    └── 03-historial/
        └── app.py           → Reto 5: git bisect
                                (el bug fue introducido en algún commit
                                del historial de este archivo)
```

## Antes de empezar

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

## Cómo usar este repo

1. Clónalo y crea tu propia rama:
   ```bash
   git checkout -b practica/tu-nombre
   ```
2. Sigue la guía de ejercicios que te compartió tu instructor.
3. Sube tu rama y abre un Pull Request cuando termines:
   ```bash
   git push origin practica/tu-nombre
   ```

## Ramas del repositorio

- `main` — historial base con todos los ejercicios
- `feature/config-a` / `feature/config-b` — versiones divergentes de
  `config.txt`, listas para generar un conflicto de merge (Reto 1)
