# Estado actual del proyecto

Handoff vivo entre sesiones de Claude Code. Se actualiza al cerrar cada bloque
de trabajo. Una sesion nueva lee este archivo y sabe donde quedamos sin que
haya que reexplicar nada.

Ultima actualizacion: 2026-08-08
Rama activa: `claude/llm-context-obsidian-bunker-e0my65`

---

## En que estamos trabajando

Sistema de contexto multi-LLM. Objetivo: que ChatGPT, Claude chat, Gemini y
NotebookLM operen con el mismo contexto operativo de Estrategias Vitales IA,
sin pegar texto manualmente en cada conversacion.

## Hallazgos clave

- `CLAUDE.md` lo lee Claude Code, no el chat de Claude. Superficies distintas,
  configuracion independiente, sin herencia.
- El problema de fondo no son los connectors. Es que los connectors hacen
  retrieval opcional. La solucion es nucleo forzado en instrucciones mas
  fuente amplia consultable.
- BUNKER.md ya vive en Google Drive y Gemini lo lee de forma nativa, por ser
  first-party de Workspace.
- El connector de Drive de ChatGPT es de terceros, mantiene indice propio y
  devuelve fragmentos, no el archivo completo.

## Entregado

Carpeta `docs/llm-context/`:

| Archivo | Contenido |
|---|---|
| `README.md` | Arquitectura de 3 capas |
| `SOP-contexto-multi-llm.md` | Procedimiento por plataforma |
| `compile-context.sh` | Compila vault en pack e indice, soporta EXT y MAX_KB |
| `CONTEXT-PACK.template.md` | Plantilla de EVIA-CORE, 13 secciones |
| `instrucciones-claude.md` | Configuracion de claude.ai web, movil y Desktop |
| `instrucciones-chatgpt.md` | Textos para Project y Custom GPT |
| `checklist-verificacion.md` | 6 pruebas y tabla de diagnostico |
| `trabajar-desde-movil.md` | Operar Claude Code desde el Pixel |

## Pendientes

| Pendiente | Owner | Bloquea |
|---|---|---|
| Correr sonda de BUNKER.md en ChatGPT, reportar puntos 1 y 4 | Salva | Decidir si hay que partir el archivo |
| Configurar preferencias personales en claude.ai, Nivel 1 | Salva | Contexto en Claude movil |
| Crear Project EVIA Brain en ChatGPT y en Claude | Salva | Contexto persistente |
| Definir si BUNKER es archivo unico o carpeta | Salva | Redaccion de los prompts |
| Espejar vault a repo privado de GitHub | Salva | Capa L3 para Claude |

## Decisiones tomadas

- Source of truth: el vault de Obsidian. Drive y GitHub son canales de
  distribucion, no originales.
- Drive es el canal para ChatGPT y Gemini. GitHub es el canal para Claude y
  Claude Code.
- No sincronizar el vault completo a Drive. Solo el pack compilado, para
  evitar conflictos de `.obsidian` entre las dos MacBooks.

## Siguiente accion

Correr la sonda de diagnostico de BUNKER.md en ChatGPT y reportar si lee el
archivo completo o solo fragmentos.

---

## Como mantener este archivo

Al cerrar cada bloque de trabajo, pedir:

```
Actualiza ESTADO.md con lo que hicimos, los pendientes nuevos y la siguiente
accion. Commit y push.
```
