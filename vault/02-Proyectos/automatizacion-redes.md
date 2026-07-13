# Proyecto: automatización de redes sociales

- Herramienta central: Metricool (conectada a Claude por MCP)
- Marca: coach_financiero_
- Redes: Instagram, Threads, TikTok, Facebook, Facebook Ads, YouTube

## Objetivo

Programar y publicar contenido en todas las redes sin automatización de navegador, con aprobación humana antes de cada publicación.

## Arquitectura del flujo

1. Ideas y calendario de contenido: markdown en este vault (07-Conocimiento o carpeta propia cuando crezca)
2. Assets (videos, imágenes): Google Drive, linkeados desde el calendario
3. Programación: Claude redacta el copy, propone fecha/hora óptima (Metricool tiene datos de best time to post) y programa vía MCP tras aprobación
4. Analítica: Claude consulta métricas de Metricool y resume qué funcionó

## Estado

- [x] Metricool conectado y verificado (2026-07-13); incluye cuenta de Facebook Ads vinculada
- [ ] Autorizar el conector meta_daniel en claude.ai (Configuración > Conectores) para campañas de Meta Ads directas; hoy está creado pero sin autenticar
- [ ] Definir calendario semanal de contenido
- [ ] Primer post programado vía Claude + Metricool como prueba piloto
- [ ] SOP de publicación documentado (ver 04-SOPs/sop-publicacion-redes-metricool.md)

## Regla de gobernanza

Ninguna publicación, campaña, cobranza o aviso sale sin aprobación explícita de Daniel. El agente propone, Daniel aprueba, el agente ejecuta.
