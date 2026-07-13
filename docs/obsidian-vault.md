# Estructura recomendada del vault de Obsidian

Estructura mínima viable. Crear estas carpetas y el archivo `00-INICIO.md`. No agregar más estructura hasta que el volumen real lo pida.

```
EVIA-Brain/                      (o el nombre de tu vault)
├── 00-INICIO.md                 Punto de entrada para ti y para cualquier LLM
├── 01-Inbox/                    Todo lo nuevo cae aquí, se procesa después
├── 02-Proyectos/
│   ├── ia-system-web.md         Ficha del proyecto, linkea al repo y a docs/ESTADO.md
│   └── (un .md por proyecto activo)
├── 03-Clientes/
│   └── (una carpeta o .md por cliente: contexto, propuestas, acuerdos)
├── 04-SOPs/                     Procesos reutilizables paso a paso
├── 05-Prompts/                  Prompts y plantillas reutilizables
├── 06-Sesiones/                 Notas destiladas de sesiones con LLMs
│   └── 2026-07-13-ejemplo.md    Formato: AAAA-MM-DD-tema.md
└── 07-Conocimiento/             Aprendizajes, referencias, ideas maduradas
```

## Contenido de 00-INICIO.md

Este archivo es lo primero que lee cualquier LLM que entre al vault. Debe contener:

```markdown
# INICIO

## Quién soy
Nombre, negocio, oferta principal, ICP, en 5 líneas.

## Qué hay en este vault
Mapa de carpetas de arriba, una línea por carpeta.

## Proyectos activos
- [[02-Proyectos/ia-system-web]] : sitio de marketing, estado en el repo en docs/ESTADO.md
- (resto de proyectos)

## Reglas para el LLM que lee esto
1. El estado de cada proyecto técnico vive en su repo, no aquí
2. Antes de proponer algo, revisar la ficha del proyecto y su última sesión en 06-Sesiones
3. Al terminar, generar nota de sesión con la plantilla
```

## Ficha de proyecto (02-Proyectos/ia-system-web.md)

```markdown
# ia-system-web

- Repo: github.com/danielcardonas8104/ia-system-web
- Producción: (dominio del sitio)
- Estado detallado: docs/ESTADO.md dentro del repo
- Objetivo: leads B2B calificados en México

## Resumen ejecutivo del proyecto
3 a 5 líneas.

## Última sesión
Link a la nota más reciente en 06-Sesiones.
```

## Cómo conectan las piezas

- El vault apunta al repo (ficha de proyecto), el repo no apunta al vault: el repo es público para colaboradores, el vault es privado
- La nota de sesión vive en el vault; el avance técnico vive en `docs/ESTADO.md` del repo
- Con el MCP de Obsidian conectado a Claude, Claude puede leer y escribir estas notas directamente; con otros LLMs, se copia y pega `00-INICIO.md` más la ficha relevante

## Respaldo

El vault debe tener sync o respaldo: Obsidian Sync, iCloud, o un repositorio git privado. Un vault local sin respaldo es un single point of failure de toda la memoria del negocio.
