# Mapa de contexto del proyecto IA System

Este directorio es el punto de entrada para cualquier LLM o persona que necesite entender el proyecto sin contexto previo.

## Orden de lectura obligatorio para un LLM

1. `docs/ESTADO.md` para saber en qué punto está el proyecto, qué se hizo y qué sigue
2. `docs/DECISIONES.md` para saber qué se decidió y por qué
3. `CLAUDE.md` y `AGENTS.md` en la raíz para reglas de operación y estilo
4. Los documentos estratégicos numerados (`01-` a `07-`) para el detalle de homepage v2

## Qué es este proyecto

Sitio web estático de marketing y conversión, HTML autocontenido con Tailwind y GSAP, desplegado en Vercel. El objetivo es generar leads B2B calificados en México.

## Regla de oro

Ninguna sesión de trabajo termina sin actualizar `ESTADO.md`. Si hubo una decisión relevante, también se registra en `DECISIONES.md`. Ese es el mecanismo que evita perder contexto entre sesiones, herramientas y modelos.

## Dónde vive cada tipo de conocimiento

| Tipo de contenido | Dónde vive | Por qué |
|---|---|---|
| Estado del proyecto y pendientes | `docs/ESTADO.md` en este repo | Viaja con el código, cualquier LLM con acceso al repo lo lee |
| Decisiones y su razón | `docs/DECISIONES.md` en este repo | Trazabilidad, evita re-discutir lo ya decidido |
| Reglas para agentes | `CLAUDE.md` y `AGENTS.md` en raíz | Los agentes los leen automáticamente |
| Estrategia, negocio, clientes, ideas | Vault de Obsidian | Es conocimiento personal y de negocio, no del código |
| Notas de sesiones con Claude u otro LLM | Vault de Obsidian, carpeta de sesiones | Se acumula como memoria de largo plazo |
| Código y assets del sitio | Este repo | Source of truth técnico |

Ver `docs/arquitectura-de-contexto.md` para la guía completa.
