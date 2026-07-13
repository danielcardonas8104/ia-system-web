# Arquitectura de contexto: qué guardar, dónde y por qué

Guía para decidir dónde vive cada tipo de conocimiento generado con Claude u otros LLMs, de forma que nunca se pierda contexto entre sesiones, herramientas y modelos.

## Principio central

Un solo source of truth por tipo de conocimiento. El problema de "el sistema divaga" casi siempre es que el mismo dato vive en dos lugares con versiones distintas, o no vive en ninguno y solo existió en un chat.

## Las tres capas

### Capa 1: Repo (este repositorio)

Vive aquí todo lo que un agente necesita para trabajar sobre el sitio:

- `docs/ESTADO.md`: avance, pendientes, dónde quedé
- `docs/DECISIONES.md`: decisiones con su razón
- `CLAUDE.md` y `AGENTS.md`: reglas de operación para agentes
- Documentos de trabajo del sitio (auditorías, copy decks, planes de build)
- El código y assets

Por qué: viaja con el código, tiene control de versiones vía git, y cualquier LLM con acceso al repo lo lee sin configurar nada.

### Capa 2: Vault de Obsidian

Vive ahí el conocimiento de negocio y personal que trasciende a este sitio:

- Estrategia de negocio, ofertas, pricing, ICP
- Notas de clientes y prospectos
- Notas de sesiones con LLMs (resúmenes, no transcripciones completas)
- SOPs y procesos reutilizables
- Ideas, contenido, aprendizajes
- Índice maestro que apunta a cada repo y proyecto

Por qué: es markdown plano en el filesystem, propiedad tuya, legible por cualquier LLM vía MCP o copy-paste, y no contamina el repo del sitio con información privada.

Ver `docs/obsidian-vault.md` para la estructura recomendada.

### Capa 3: Los chats (ChatGPT, Claude.ai, etc.)

No son memoria. Son espacio de trabajo desechable. Regla: si algo de un chat vale la pena, se destila a la capa 1 o 2 antes de cerrar la sesión. Lo que no se destila, se pierde por diseño.

## Matriz de decisión rápida

| Contenido generado | Destino |
|---|---|
| Cambio de código o copy del sitio | Repo (commit) |
| Avance o pendiente del proyecto | `docs/ESTADO.md` |
| Decisión con trade-off | `docs/DECISIONES.md` |
| Propuesta comercial para un cliente | Obsidian, carpeta del cliente |
| SOP o proceso reutilizable | Obsidian, carpeta SOPs |
| Idea de contenido o negocio | Obsidian, inbox |
| Prompt reutilizable | Obsidian, carpeta prompts |
| Regla nueva de cómo debe trabajar el agente | `CLAUDE.md` |
| Borrador exploratorio sin valor futuro | Ningún lado, se descarta |

## El ritual de cierre de sesión (lo que hace que todo funcione)

Al final de cada sesión de trabajo con cualquier LLM, ejecutar estos tres pasos:

1. **Destilar:** pedir al LLM "Resume esta sesión: qué se hizo, qué se decidió, qué quedó pendiente, en formato markdown con la plantilla de docs/plantillas/nota-sesion.md"
2. **Guardar:** la nota va al vault de Obsidian; si tocó este proyecto, actualizar también `docs/ESTADO.md` y hacer commit
3. **Verificar:** el ESTADO.md debe permitir retomar mañana sin releer el chat

Costo: 3 a 5 minutos por sesión. Es el precio de nunca perder contexto.

## El ritual de apertura de sesión

Al iniciar sesión con cualquier LLM sobre este proyecto:

1. Darle a leer `docs/README.md` y `docs/ESTADO.md` (o pegarlos si el LLM no tiene acceso al repo)
2. Indicar el objetivo de la sesión en una línea
3. Trabajar

Con Claude Code esto es automático si `CLAUDE.md` instruye leer `docs/ESTADO.md` al inicio.

## Qué NO hacer

- No guardar transcripciones completas de chats: ruido que ningún LLM va a leer bien después
- No duplicar el mismo documento en repo y Obsidian: elegir un dueño y en el otro poner solo un link
- No crear más de un nivel extra de carpetas hasta que el volumen lo exija
- No dejar documentos internos en la raíz de un sitio estático público (ver D-002 en DECISIONES.md)

## Riesgos y trade-offs

- El sistema depende de la disciplina del ritual de cierre; sin eso, ninguna estructura salva el contexto
- Markdown en repo es público para cualquiera con acceso al repo; información sensible de clientes va a Obsidian, no aquí
- Obsidian local no es respaldo; activar sync (Obsidian Sync, iCloud o un repo git privado del vault)
