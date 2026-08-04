# SOP: dar contexto de Obsidian / BUNKER a cualquier LLM

Version 1.0
Owner: Salvador Villarreal
Objetivo: que ChatGPT, Claude, Gemini y NotebookLM respondan con el mismo
contexto operativo sin intervencion manual por conversacion.

## Principio rector

Hay dos mecanismos distintos y se confunden todo el tiempo:

1. **Contexto forzado**: texto que se inyecta en cada turno sin que el modelo
   decida nada. Ejemplos: instrucciones de sistema, instrucciones de Project,
   instrucciones de Custom GPT, `CLAUDE.md`.
2. **Retrieval**: el modelo busca en una fuente conectada solo si lo considera
   necesario. Ejemplos: connectors de Drive o GitHub, archivos de knowledge,
   busqueda en Projects.

Si dependes solo de retrieval, vas a tener respuestas sin contexto de forma
intermitente. La solucion es combinar: nucleo forzado corto y fuente amplia
consultable.

---

## Fase 1: Compilar el vault

### Precheck
- Ubicar la ruta real del vault. Ejemplo: `~/Obsidian/EVIA-Brain`
- Confirmar que no hay informacion de clientes que no deba salir del equipo
- Confirmar espacio en disco para la salida

### Comandos macOS / zsh

```bash
cd ~/ia-system-web
chmod +x docs/llm-context/compile-context.sh
docs/llm-context/compile-context.sh ~/Obsidian/EVIA-Brain ~/Desktop/evia-context
open ~/Desktop/evia-context
```

### Postcheck
- `EVIA-CORE.md` existe y no supera 6000 palabras
- `INDEX.md` lista las notas esperadas
- `pack/` contiene entre 3 y 15 archivos

---

## Fase 2: Editar el nucleo

El script produce un borrador. El nucleo real se escribe a mano usando
`CONTEXT-PACK.template.md`.

Reglas del nucleo:
- Entre 2000 y 4000 palabras. Mas alla de eso pierde efectividad y encarece cada turno.
- Solo informacion estable. Nada que cambie cada semana.
- Sin narrativa. Bullets, tablas y definiciones.
- Debe incluir: identidad, ICP, lineas de servicio, pricing de referencia,
  stack, tono, reglas de salida, y que hacer cuando falte informacion.
- Debe incluir la instruccion explicita de consultar la fuente conectada antes
  de responder sobre proyectos, clientes o historial.

---

## Fase 3: Configurar por plataforma

### ChatGPT, opcion recomendada: Projects

1. Crear Project `EVIA Brain`
2. Instrucciones del Project: pegar `EVIA-CORE.md` completo
3. Archivos del Project: subir todo `pack/*.md` y `INDEX.md`
4. Trabajar siempre dentro del Project. Fuera del Project no hay contexto.

Ventaja: instrucciones largas, archivos persistentes, memoria acotada al Project.

### ChatGPT, opcion secundaria: Custom GPT

1. Crear GPT `EVIA Brain`
2. Instructions: version comprimida del nucleo. El campo tiene limite cercano a
   8000 caracteres, por eso la version corta.
3. Knowledge: subir `pack/*.md`
4. Capabilities: dejar solo lo necesario

Ventaja: reutilizable y compartible con el equipo.
Desventaja: actualizar knowledge es manual.

### ChatGPT, capa L3: connectors

En Settings, seccion de connectors o fuentes, conectar segun disponibilidad del
plan: Google Drive, GitHub, Dropbox, OneDrive, SharePoint. Verificar que el
connector aparezca disponible en la cuenta antes de disenar el flujo alrededor
de el.

Para connectors personalizados via MCP se requiere modo desarrollador y un
endpoint HTTPS publico. Un servidor MCP en localhost no es alcanzable.

### Claude web y desktop

1. Crear Project `EVIA Brain`
2. Project knowledge: pegar el nucleo y subir el pack
3. Connectors: GitHub y Google Drive segun plan
4. Para el vault local, usar servidor MCP de filesystem en Claude Desktop

### Claude Code

Ya resuelto. `CLAUDE.md` global y de proyecto mas MCP de Obsidian.
Este SOP no cambia nada ahi.

### NotebookLM

Subir el pack como fuentes. Sirve como capa de consulta y sintesis sobre el
vault, no como copiloto operativo.

### Gemini y Perplexity

Pegar el nucleo al inicio de cada hilo largo, o usar Gems en Gemini con el
nucleo en instrucciones. Menor prioridad.

---

## Fase 4: Espejar el vault en Git

Recomendado sobre Google Drive por versionado y por compatibilidad uniforme.

### Setup

```bash
cd ~/Obsidian/EVIA-Brain
git init
printf '.obsidian/workspace*\n.trash/\n.DS_Store\n' > .gitignore
git add -A
git commit -m "Inicializa vault EVIA-Brain como source of truth"
git branch -M main
git remote add origin git@github.com:USUARIO/evia-brain.git
git push -u origin main
```

Repo **privado**. Despues instalar el plugin Obsidian Git y configurar
auto-commit cada 10 minutos y auto-push.

### Conectar
- ChatGPT: connector de GitHub sobre el repo `evia-brain`
- Claude: connector de GitHub sobre el mismo repo
- Claude Code: `git clone` local, lectura directa

### Alternativa Google Drive
Mover el vault dentro del folder sincronizado de Drive. Excluir `.obsidian` del
sync para evitar conflictos entre maquinas. Riesgo real de corrupcion si dos
equipos escriben a la vez. Con dos MacBooks activas, este riesgo es concreto.

---

## Fase 5: Verificacion

Ver `checklist-verificacion.md`. No declarar terminado sin pasar las 6 pruebas.

---

## Riesgos y trade-offs

| Riesgo | Impacto | Mitigacion |
|---|---|---|
| Vault privado espejado en la nube | Fuga de informacion de clientes | Repo privado, carpeta `99-Confidencial` excluida del pack |
| Nucleo crece sin control | Costo por turno y perdida de foco | Poda mensual, tope de 4000 palabras |
| Pack desactualizado | Respuestas con datos viejos | Recompilar semanal, incluir fecha en cada archivo |
| Dependencia de un connector | Cambia el plan o el proveedor y se rompe | L1 no depende de connectors |
| Conflictos de sync Drive con dos equipos | Corrupcion del vault | Usar Git en lugar de Drive |

## Supuestos

- El vault BUNKER es local en la MacBook Air M5 y esta en formato markdown plano
- No hay informacion regulada de terceros que impida espejar en la nube
- Los planes de ChatGPT y Claude son de pago con Projects habilitado

## Pendiente por validar

- Disponibilidad exacta de connectors en el plan actual de ChatGPT
- Tamano total del vault en MB y numero de notas
- Si existe carpeta con datos confidenciales de cliente que deba excluirse
