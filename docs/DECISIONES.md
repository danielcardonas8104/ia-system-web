# DECISIONES.md

Registro de decisiones del proyecto. Una decisión registrada no se vuelve a discutir salvo que cambie el contexto. Formato: ID, fecha, decisión, razón, estado.

## D-001 | 2026-07-13 | Arquitectura de contexto en markdown

**Decisión:** Todo el contexto operativo del proyecto vive en markdown dentro del repo (`docs/`) y el conocimiento de negocio vive en un vault de Obsidian. `ESTADO.md` es el source of truth del avance.

**Razón:** Permite que cualquier LLM (Claude, ChatGPT, Gemini, Perplexity) entre al proyecto y sepa qué hay, qué se hace, por qué y dónde quedó, sin depender de la memoria de una sola herramienta.

**Estado:** Activa.

## D-002 | 2026-07-13 | Exposición de documentos internos en producción

**Hallazgo:** Los archivos `01-` a `07-*.md`, `CLAUDE.md`, `AGENTS.md` y `guion.txt` están en la raíz del proyecto y Vercel los sirve públicamente como archivos estáticos (por ejemplo `/04-copy-deck-v2.md` con estrategia de pricing es accesible desde internet).

**Decisión (2026-07-13, con luz verde del dueño):** Se agregó `.vercelignore` excluyendo del deploy: todos los `.md`, `docs/`, `vault/`, `guion.txt`, el pipeline de Python y los HTML de backup. El sitio público no cambia; solo dejan de servirse archivos internos.

**Estado:** Aplicada en branch, activa al hacer merge y deploy.

## D-003 | 2026-07-13 | Inconsistencia de identidad en instrucciones de agentes

**Hallazgo:** `CLAUDE.md` describe a Salvador Villarreal, Estrategias Vitales IA y el dominio `iaconsultoresvitales.mx`, mientras que `AGENTS.md` y el repo describen IA System / `ia-system.pro` y el material visual es de Daniel. Dos sources of truth contradictorios producen exactamente el divague que se quiere evitar.

**Decisión propuesta (pendiente de aprobación):** Reescribir `CLAUDE.md` con la identidad real del proyecto (marca, dominio, fundador, oferta) y dejar `AGENTS.md` alineado, o eliminar uno de los dos.

**Estado:** Pendiente de validar por el dueño del proyecto.

## Plantilla para nuevas decisiones

## D-XXX | AAAA-MM-DD | Título corto

**Decisión:** qué se decidió.

**Razón:** por qué, con qué trade-off.

**Estado:** Activa / Reemplazada por D-YYY / Pendiente.

## D-004 | 2026-07-13 | Cerebro digital: Metricool por API en lugar de navegador, vault staged en el repo

**Decisión:** La publicación y programación en redes sociales se hace vía el conector MCP de Metricool (verificado: marca coach_financiero_ con 6 redes conectadas), no con automatización de navegador Chrome. El vault de Obsidian se construyó completo en `vault/` de este repo porque la integración de GitHub no tiene permiso para crear repos nuevos; el destino final es el repo privado `ia-system-brain` y después se borra `vault/` de aquí.

**Razón:** La API de Metricool es más confiable, trazable y rápida que controlar un navegador; el navegador queda solo para lo que no tenga API. El vault en repo privado separa el conocimiento de negocio del código público del sitio.

**Estado:** Activa; migración del vault pendiente de ejecutar en la Mac.
