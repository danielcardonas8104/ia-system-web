# Proyecto: cerebro digital

## Objetivo

Memoria persistente en markdown para trabajar con cualquier LLM sin repetir contexto: qué tengo, qué hago, por qué, dónde me quedé.

## Arquitectura (decidida 2026-07-13)

- Capa 1: vault Obsidian + repo privado GitHub (este vault) = cerebro
- Capa 2: Google Drive = distribución y binarios (estructura en estructura-drive.md)
- Capa 3: repos por proyecto con docs/ESTADO.md = estado técnico
- Los chats de LLMs no son memoria: se destila lo valioso al cerrar cada sesión

## Estado

- [x] Estructura docs/ creada en repo del sitio
- [x] Vault completo creado con contexto maestro e inventario
- [ ] Migrar vault a repo privado ia-system-brain (instrucciones en README.md del vault)
- [ ] Conectar carpeta como vault en Obsidian + plugin Obsidian Git
- [ ] Cargar CONTEXTO-MAESTRO.md en Project de ChatGPT, Project de Claude y Gem de Gemini
- [ ] Crear estructura de carpetas en Drive
- [ ] Primer ciclo completo de ritual de apertura y cierre de sesión
