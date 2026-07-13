# ESTADO.md

Source of truth del estado del proyecto. Se actualiza al final de cada sesión de trabajo.

Última actualización: 2026-07-13

## Estado actual

- Sitio en producción en Vercel, HTML estático autocontenido
- Homepage con reposicionamiento completo a "Consultoría IA Operativa" (commit 3b11325)
- Hero visual con video de luces, shader dorado y glass UI (commits 15ee41c y b5fe44a)
- Pipeline TTS con ElevenLabs agregado y teléfono corregido en schema (commit c9311a5)
- Documentos estratégicos de homepage v2 completos (01 a 07 en raíz)
- Existe branch `feature/hero-video-shader-redesign` además de main

## En progreso

- Arquitectura de contexto en markdown para memoria persistente entre sesiones y LLMs (branch `claude/obsidian-markdown-context-jfhg2k`)
- Conexión del vault de Obsidian como memoria de largo plazo

## Pendientes conocidos

- [ ] Validar copy deck v2 (todas las marcas [VALIDAR] y [CONFIRMAR] en `04-copy-deck-v2.md`)
- [ ] Decidir H1 definitivo (opciones A, B o C del copy deck)
- [ ] Confirmar deliverables exactos del retainer y rango de precio en FAQ
- [ ] Confirmar testimonios y logotipos reales disponibles
- [ ] Resolver exposición pública de documentos internos .md en la raíz (ver DECISIONES.md, D-002)
- [ ] Unificar identidad del proyecto en CLAUDE.md y AGENTS.md (ver DECISIONES.md, D-003)

## Dónde me quedé

Se creó la estructura `docs/` con ESTADO, DECISIONES, plantillas y guía de arquitectura de contexto. Falta que el dueño del proyecto cree el vault de Obsidian siguiendo `docs/obsidian-vault.md` y adopte el ritual de cierre de sesión.

## Cómo actualizar este archivo

Al cerrar cada sesión de trabajo con Claude o cualquier LLM, pedir literalmente:

"Actualiza docs/ESTADO.md: resume qué se hizo hoy, qué quedó en progreso, qué pendientes se agregaron o cerraron, y dónde me quedé. Haz commit con mensaje descriptivo en español."
