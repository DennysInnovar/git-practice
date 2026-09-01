# Guía de Ejercicios — Práctica de Git

Bienvenido/a a la práctica de Git. Esta guía tiene dos partes:

- **Ejercicios generales**: para que todos completen durante el día.
- **Ejercicios desafiantes**: opcionales, para quienes terminen antes o quieran ir más allá.

> Antes de empezar, asegúrate de tener Git configurado:
> ```bash
> git config --global user.name "Tu Nombre"
> git config --global user.email "tu@email.com"
> ```

---

## Preparación

1. Clona el repositorio de práctica:
   ```bash
   git clone https://github.com/DennysInnovar/git-practice
   cd git-practice
   ```
2. Crea tu propia rama de trabajo:
   ```bash
   git checkout -b practica/tu-nombre
   ```

---

## Parte 1 — Ejercicios generales

### Ejercicio 1: Primeros commits
**Objetivo:** familiarizarte con el ciclo `add → commit → log`.

1. Abre `ejercicios/01-basico/notas.txt`.
2. Agrega una línea con tu nombre y la fecha de hoy.
3. Guarda y ejecuta:
   ```bash
   git status
   git add ejercicios/01-basico/notas.txt
   git commit -m "Agrega presentación de [tu nombre]"
   ```
4. Repite el proceso 2 veces más, agregando otra línea cada vez (ej. algo que aprendiste hoy).
5. Al final deberías tener **3 commits nuevos** en tu rama.

**Verifica:**
```bash
git log --oneline
```
Deberías ver tus 3 commits con mensajes claros y descriptivos.

---

### Ejercicio 2: Explorar el historial
**Objetivo:** entender cómo leer el historial de un repositorio.

1. Ejecuta:
   ```bash
   git log --oneline --graph --all
   ```
2. Responde (puedes anotarlo en un archivo `respuestas.md`):
   - ¿Cuántas ramas existen en el repo?
   - ¿Cuál fue el primer commit del repositorio?
   - ¿Quién hizo el commit más reciente antes que el tuyo?

---

### Ejercicio 3: Subir tu trabajo
**Objetivo:** practicar `push` y abrir tu primer Pull Request.

1. Sube tu rama al repositorio remoto:
   ```bash
   git push origin practica/tu-nombre
   ```
2. Ve a GitHub y abre un Pull Request de tu rama hacia `main`.
3. Escribe una descripción breve de qué hiciste.

---

## Parte 2 — Ejercicios desafiantes

Estos ejercicios requieren un poco más de investigación. Se recomienda hacerlos **en orden**.

### Reto 1: Resolver un conflicto real
**Ubicación:** `ejercicios/02-conflicto/config.txt`

Este archivo tiene versiones diferentes en dos ramas: `feature/config-a` y `feature/config-b`.

1. Haz checkout a `feature/config-a`.
2. Intenta mergear `feature/config-b`:
   ```bash
   git checkout feature/config-a
   git merge feature/config-b
   ```
3. Git te avisará que hay un conflicto. Abre el archivo, busca las marcas `<<<<<<<`, `=======`, `>>>>>>>`.
4. Decide cómo combinar ambos cambios, edita el archivo a mano, y luego:
   ```bash
   git add ejercicios/02-conflicto/config.txt
   git commit
   ```

**Pregunta para reflexionar:** ¿por qué Git no pudo resolver este conflicto automáticamente?

---

### Reto 2: Cherry-pick
**Objetivo:** traer un commit específico de otra rama sin mergear todo.

1. Ubica el hash de un commit en la rama `feature/config-b` que **no** quieras mergear por completo:
   ```bash
   git log feature/config-b --oneline
   ```
2. Desde tu rama, aplica solo ese commit:
   ```bash
   git cherry-pick <hash-del-commit>
   ```
3. Verifica con `git log` que el commit se aplicó, pero que el resto del historial de `feature/config-b` no llegó a tu rama.

---

### Reto 3: Deshacer cambios
**Objetivo:** distinguir entre revertir un commit público y borrar uno local.

**Parte A — revert (para commits ya subidos):**
```bash
git revert <hash-del-commit>
```
Esto crea un commit nuevo que deshace los cambios, sin alterar el historial.

**Parte B — reset (solo para commits locales, no pusheados):**
1. Haz un commit de prueba local.
2. Prueba:
   ```bash
   git reset --soft HEAD~1   # deshace el commit, mantiene los cambios en staging
   ```
3. Vuelve a hacer commit, y ahora prueba:
   ```bash
   git reset --hard HEAD~1   # deshace el commit Y los cambios
   ```

**Pregunta:** ¿por qué nunca deberías usar `reset --hard` sobre commits que ya hiciste `push`?

---

### Reto 4: Rebase interactivo (squash)
**Objetivo:** limpiar historial combinando varios commits en uno.

1. Asegúrate de tener al menos 3 commits en tu rama (los del Ejercicio 1 sirven).
2. Ejecuta:
   ```bash
   git rebase -i HEAD~3
   ```
3. En el editor que se abre, cambia `pick` por `squash` (o `s`) en los últimos dos commits.
4. Guarda, y luego edita el mensaje final combinado.
5. Verifica con `git log --oneline` que ahora tienes un solo commit en vez de tres.

---

### Reto 5: Git Bisect
**Ubicación:** `ejercicios/03-historial/app.py`

Este archivo tiene varios commits en su historial, y en algún punto se introdujo un bug.

1. Inicia la búsqueda:
   ```bash
   git bisect start
   git bisect bad HEAD
   git bisect good <hash-de-un-commit-viejo-que-funcionaba>
   ```
2. Git irá saltando entre commits. En cada uno, revisa `app.py` (o corre el script) y marca:
   ```bash
   git bisect good
   # o
   git bisect bad
   ```
3. Repite hasta que Git identifique el commit exacto que introdujo el problema.
4. Termina con:
   ```bash
   git bisect reset
   ```

---

### Reto 6: Stash
**Objetivo:** guardar trabajo a medias sin hacer commit.

1. Modifica cualquier archivo, pero **no** hagas commit.
2. Guarda tus cambios temporalmente:
   ```bash
   git stash
   ```
3. Cambia a otra rama, verifica que tu archivo modificado ya no aparece.
4. Vuelve a tu rama original y recupera tus cambios:
   ```bash
   git stash pop
   ```

---

## Checklist final

- [X] Ejercicio 1 — 3 commits en mi rama
- [X] Ejercicio 2 — respondí las preguntas del historial
- [X] Ejercicio 3 — abrí mi Pull Request
- [X] Reto 1 — resolví el conflicto
- [ ] Reto 2 — cherry-pick exitoso
- [ ] Reto 3 — probé revert y reset
- [ ] Reto 4 — rebase interactivo con squash
- [ ] Reto 5 — encontré el commit con bisect
- [ ] Reto 6 — usé stash correctamente

¡Cualquier duda, pregúntale a tu instructor o revisa `git help <comando>`!
