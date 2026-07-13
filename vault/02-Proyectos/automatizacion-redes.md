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
- [x] Conector meta_daniel autorizado y verificado (2026-07-13): Meta Ads completo desde Claude
- [ ] Definir campaña piloto en Meta Ads con tope de presupuesto
- [ ] Definir calendario semanal de contenido
- [ ] Primer post programado vía Claude + Metricool como prueba piloto
- [ ] SOP de publicación documentado (ver 04-SOPs/sop-publicacion-redes-metricool.md)

## Meta Ads (verificado 2026-07-13)

- Business Manager: Daniel Cardona Coach (751460993955143)
- Página para anuncios: Daniel Cardona Finanzas (679228925271437)
- Cuentas publicitarias activas en MXN:
  - act_1735587487315956 (con método de pago, la vinculada en Metricool)
  - act_3640744789561033 "Daniel Cardona" (con método de pago)
  - act_2060563824885192 (sin método de pago, no usar)
- Capacidades desde Claude: crear campañas, ad sets, anuncios y creativos, públicos personalizados, boost de posts de Instagram, A/B tests, pixel, catálogos, insights y benchmarks
- Presupuesto mínimo diario de Meta: 17.57 MXN

## Regla de gobernanza

Ninguna publicación, campaña, cobranza o aviso sale sin aprobación explícita de Daniel. El agente propone, Daniel aprueba, el agente ejecuta.
