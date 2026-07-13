# DECISIONES.md

Registro de decisiones del proyecto. Una decisión registrada no se vuelve a discutir salvo que cambie el contexto. Formato: ID, fecha, decisión, razón, estado.

## D-001 | 2026-07-13 | Arquitectura de contexto en markdown

**Decisión:** Todo el contexto operativo del proyecto vive en markdown dentro del repo (`docs/`) y el conocimiento de negocio vive en un vault de Obsidian. `ESTADO.md` es el source of truth del avance.

**Razón:** Permite que cualquier LLM (Claude, ChatGPT, Gemini, Perplexity) entre al proyecto y sepa qué hay, qué se hace, por qué y dónde quedó, sin depender de la memoria de una sola herramienta.

**Estado:** Activa.

## D-002 | 2026-07-13 | Exposición de documentos internos en producción

**Hallazgo:** Los archivos `01-` a `07-*.md`, `CLAUDE.md`, `AGENTS.md` y `guion.txt` están en la raíz del proyecto y Vercel los sirve públicamente como archivos estáticos (por ejemplo `/04-copy-deck-v2.md` con estrategia de pricing es accesible desde internet).

**Decisión propuesta (pendiente de aprobación):** Bloquear el servido de `.md` y `.txt` internos vía `vercel.json` o moverlos a `docs/` y excluir `docs/` del deploy. No se aplicó porque implica modificar archivos existentes de producción.

**Estado:** Pendiente de validar por el dueño del proyecto.

## D-003 | 2026-07-13 | Inconsistencia de identidad en instrucciones de agentes

**Hallazgo:** `CLAUDE.md` describe a Salvador Villarreal, Estrategias Vitales IA y el dominio `iaconsultoresvitales.mx`, mientras que `AGENTS.md` y el repo describen IA System / `ia-system.pro` y el material visual es de Daniel. Dos sources of truth contradictorios producen exactamente el divague que se quiere evitar.

**Decisión propuesta (pendiente de aprobación):** Reescribir `CLAUDE.md` con la identidad real del proyecto (marca, dominio, fundador, oferta) y dejar `AGENTS.md` alineado, o eliminar uno de los dos.

**Estado:** Pendiente de validar por el dueño del proyecto.

## Plantilla para nuevas decisiones

## D-XXX | AAAA-MM-DD | Título corto

**Decisión:** qué se decidió.

**Razón:** por qué, con qué trade-off.

**Estado:** Activa / Reemplazada por D-YYY / Pendiente.
