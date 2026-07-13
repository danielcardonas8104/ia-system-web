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
- Vault de Obsidian completo creado en `vault/` con contexto maestro, inventario, fichas de proyecto y SOPs; pendiente migrarlo a repo privado `ia-system-brain` (instrucciones en `vault/README.md`)
- Se agregó `.vercelignore` para dejar de servir documentos internos (.md, docs/, vault/, backups) en el sitio público; aplica al hacer merge y deploy
- Metricool verificado por MCP: marca `coach_financiero_` con Instagram, Threads, TikTok, Facebook, Facebook Ads y YouTube conectados

## Pendientes conocidos

- [ ] Validar copy deck v2 (todas las marcas [VALIDAR] y [CONFIRMAR] en `04-copy-deck-v2.md`)
- [ ] Decidir H1 definitivo (opciones A, B o C del copy deck)
- [ ] Confirmar deliverables exactos del retainer y rango de precio en FAQ
- [ ] Confirmar testimonios y logotipos reales disponibles
- [ ] Hacer merge de esta branch para activar `.vercelignore` en producción (resuelve D-002)
- [ ] Unificar identidad del proyecto en CLAUDE.md y AGENTS.md (ver DECISIONES.md, D-003)
- [ ] Migrar `vault/` a repo privado `ia-system-brain` y borrarlo de este repo (ver D-004)
- [ ] Cargar CONTEXTO-MAESTRO.md en Projects de ChatGPT y Claude, y Gem de Gemini
- [ ] Piloto: primer post programado vía Claude + Metricool (SOP en el vault)

## Dónde me quedé

El vault completo está en `vault/` de esta branch, listo para copiar a la Mac, abrir en Obsidian y subir a su repo privado (5 minutos siguiendo `vault/README.md`). El siguiente hito es el piloto de publicación en redes con Metricool.

## Cómo actualizar este archivo

Al cerrar cada sesión de trabajo con Claude o cualquier LLM, pedir literalmente:

"Actualiza docs/ESTADO.md: resume qué se hizo hoy, qué quedó en progreso, qué pendientes se agregaron o cerraron, y dónde me quedé. Haz commit con mensaje descriptivo en español."
