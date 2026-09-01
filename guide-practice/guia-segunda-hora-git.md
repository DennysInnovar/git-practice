# Guía — Segunda sesión de práctica
Esta sesión asume que ya completaron los ejercicios generales de la
primera guía (`guia-ejercicios-git.md`). Aquí el foco cambia: menos
comandos sueltos, más flujo de trabajo real en equipo.
---

## Actividad 1: Revisión de Pull Request en parejas
**Objetivo:** experimentar el flujo real de colaboración, no solo el técnico.

1. Formen parejas. Cada quien ya tiene un PR abierto desde la tarea anterior (o abran uno nuevo con un cambio pequeño en `notas.txt`).
2. Intercambien PRs: revisen el de su compañero/a, no el propio.
3. Dejen al menos **3 comentarios** en líneas específicas del código (usen el ícono `+` al pasar el mouse sobre una línea en la pestaña "Files changed"). Al menos uno debe ser una pregunta, no solo una observación.
4. Si algo se puede mejorar, usen **"Request changes"**; si está bien, usen **"Approve"**.
5. El autor del PR responde los comentarios y, si aplica, hace un nuevo commit para atender el feedback.
6. **Segunda ronda:** el revisor vuelve a mirar el PR actualizado y confirma si aprueba o pide más cambios.
7. Mergeen el PR usando **"Squash and merge"** y observen cómo queda el historial en `main` (un solo commit, en vez de varios).

**Preguntas para reflexionar:**
- ¿Qué comentario hizo tu compañero/a que no habías considerado?
- ¿Notas diferencia entre el historial con "Squash and merge" y un merge normal?

---

## Actividad 2: Simulacro de incidente
**Objetivo:** practicar diagnóstico y respuesta bajo un escenario realista.

> Una persona introduce un bug a propósito en la rama `main` y avisa: "algo se rompió en producción".

1. En parejas, usen `git log` para ubicarse en el historial reciente:
   ```bash
   git log --oneline -15
   ```
2. Inicien la búsqueda con `git bisect`:
   ```bash
   git bisect start
   git bisect bad HEAD
   git bisect good <commit-anterior-conocido-bueno>
   ```
3. En cada paso, revisen el código o corran el script indicado por el instructor, y marquen:
   ```bash
   git bisect good
   # o
   git bisect bad
   ```
4. Una vez identificado el commit responsable, decidan la estrategia de arreglo:
   - **Opción A:** `git revert <hash>` — deshace el cambio con un commit nuevo, sin alterar el historial existente.
   - **Opción B:** arreglar manualmente el bug y hacer un commit de fix, dejando el commit original intacto en el historial.
5. Terminen la búsqueda:
   ```bash
   git bisect reset
   ```
6. Abran un PR con el arreglo. En la descripción, expliquen: **qué pasó, cómo lo encontraron (el commit exacto) y por qué eligieron esa estrategia de arreglo.**

**Preguntas para reflexionar:**
- ¿En qué casos preferirías `revert` sobre un fix manual, y viceversa?
- Si el bug llevara semanas en producción, ¿cambiaría tu estrategia?

---

## Actividad 3: Rebase vs. merge — mismo escenario
**Objetivo:** ver en la práctica cómo cada estrategia deja un historial distinto.

1. Cada pareja crea dos copias de la misma situación: una rama `feature/x` con 3 commits, divergente de `main` (que también avanzó con 2 commits propios).
   - Persona A resuelve la integración con:
     ```bash
     git checkout feature/x
     git merge main
     ```
   - Persona B resuelve la **misma** integración (en su propia copia) con:
     ```bash
     git checkout feature/x
     git rebase main
     ```
2. Comparen ambos resultados con `git log --oneline --graph --all`.
3. Anoten las diferencias: ¿cuántos commits hay en cada historial? ¿aparece un commit de merge? ¿el orden de los commits es el mismo?

**Pregunta para reflexionar:** ¿en qué tipo de equipo o proyecto preferirías cada estrategia como política por defecto?

---

## Actividad 4: Issues vinculados a un Pull Request
**Objetivo:** conectar el trabajo de código con el tracking de tareas.

1. Creen un Issue en GitHub describiendo una mejora pequeña (ej. "Agregar sección de contacto a notas.txt"). Incluyan una descripción de 2-3 líneas y, si aplica, un checklist de sub-tareas.
2. Asignen el Issue a sí mismos y agréguenle una etiqueta (label), como `enhancement` o `documentation`.
3. Anoten el número del Issue (ej. `#12`).
4. Creen una rama con un nombre descriptivo (ej. `feature/12-seccion-contacto`), hagan el cambio, y en el commit o en la descripción del PR incluyan:
   ```
   Closes #12
   ```
5. Al mergear el PR, verifiquen que el Issue se cerró automáticamente y quedó vinculado en su historial.

**Pregunta para reflexionar:** ¿qué ventaja tiene usar Issues en vez de solo coordinar tareas por chat?

---

## Actividad 5: Tags y releases
**Objetivo:** marcar versiones significativas del historial.

1. Desde `main`, creen un tag anotado:
   ```bash
   git tag -a v1.0.0 -m "Primera versión estable de práctica"
   git push origin v1.0.0
   ```
2. Creen un segundo tag más adelante en el historial, después de fusionar al menos un PR más:
   ```bash
   git tag -a v1.1.0 -m "Agrega sección de contacto"
   git push origin v1.1.0
   ```
3. En GitHub, vayan a la sección **Releases** y creen una release a partir de cada tag.
4. Escriban notas breves de cada release (2-3 líneas: qué incluye esta versión).
5. Comparen ambos tags con:
   ```bash
   git log v1.0.0..v1.1.0 --oneline
   ```

**Pregunta para reflexionar:** ¿en qué momento del ciclo de vida de un proyecto real crearían un tag?

---

## Actividad 6: Proteger la rama `main`
**Objetivo:** entender por qué los equipos restringen los cambios directos a la rama principal.

1. En GitHub, vayan a **Settings → Branches → Add branch protection rule** sobre `main`.
2. Activen al menos estas reglas:
   - Require a pull request before merging
   - Require approvals (mínimo 1)
   - Require status checks to pass (si tienen algún check configurado)
3. Intenten hacer push directo a `main` desde la terminal:
   ```bash
   git checkout main
   echo "cambio directo" >> ejercicios/01-basico/notas.txt
   git add . && git commit -m "Cambio directo de prueba"
   git push origin main
   ```
4. Observen el mensaje de rechazo de GitHub.
5. Deshagan el commit local (`git reset --soft HEAD~1`) y hagan el cambio correctamente vía rama + PR.

**Pregunta para reflexionar:** ¿qué problema real previene esta protección en un equipo de varias personas?

---

## Actividad 7: Aliases + taller de mensajes de commit

### Parte A — Git aliases (5 min)
Configuren al menos 3 atajos propios:
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"
```
Prueben usarlos: `git st`, `git lg`.

### Parte B — Taller de mensajes de commit (5 min)
Reescriban estos mensajes de commit reales (y malos) a un formato claro:

| Mensaje original | Tu reescritura |
|---|---|
| `fix` | |
| `cambios` | |
| `asdasd` | |
| `arreglo el bug que rompia todo ayer` | |
| `Update index.js` | |

**Regla rápida:** el mensaje debe completar la frase "Si se aplica, este commit va a ___".

---

## Actividad 8: `git blame` y `git log -p`
**Objetivo:** practicar cómo investigar el "por qué" detrás de una línea de código.

1. Elijan un archivo con varios commits en su historial (ej. `ejercicios/03-historial/app.py`).
2. Ejecuten:
   ```bash
   git blame ejercicios/03-historial/app.py
   ```
   Identifiquen qué commit modificó por última vez cada línea.
3. Investiguen ese commit específico:
   ```bash
   git show <hash-del-commit>
   ```
4. Ahora vean la evolución completa de una función a través del tiempo:
   ```bash
   git log -p --follow ejercicios/03-historial/app.py
   ```
5. Respondan: si encontraran una línea rara en este archivo en un proyecto real, ¿qué harían primero: preguntar en el chat del equipo o correr `git blame`?

---

## Checklist final

- [ ] Actividad 1 — dejé feedback en el PR de mi compañero/a y lo mergeamos
- [ ] Actividad 2 — encontré el commit con bisect y decidí una estrategia de arreglo
- [ ] Actividad 3 — comparé el historial resultante de merge vs. rebase
- [ ] Actividad 4 — mi PR cerró un Issue automáticamente
- [ ] Actividad 5 — creé dos tags y sus releases
- [ ] Actividad 6 — probé (y fallé a propósito) un push directo a `main` protegida
- [ ] Actividad 7 — configuré mis aliases y reescribí los mensajes de commit
- [ ] Actividad 8 — usé `git blame` y `git log -p` para investigar un archivo

¡Cualquier duda, pregúntale a tu instructor!
