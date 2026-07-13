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

## Campaña piloto creada (2026-07-13, aprobada por Daniel)

Todo en estado PAUSED hasta activación manual:
- Campaña: "Piloto Ventas WhatsApp - Coach Financiero - Jul 2026" (ID 120248625002790331), objetivo OUTCOME_SALES, 100 MXN diarios, del 14 al 19 de julio (5 días, tope efectivo ~500 MXN por fechas)
- Ad set: "Conversaciones Messenger - Mexico Abierto" (ID 120248625105790331), optimizado a conversaciones, público México abierto
- Anuncio: "Anuncio Piloto Conversaciones - Julio 2026" (ID 120248625188890331), imagen lámina 1 del carrusel 6, CTA enviar mensaje, copy con palabra clave PLAN
- Nota: la página NO tiene WhatsApp Business conectado; el piloto salió por Messenger. Conectar WhatsApp en Meta Business Suite > Configuración > WhatsApp y pedir al agente cambiar el destino
- Para activar: Ads Manager > activar campaña 120248625002790331, o pedirlo al agente

## Calendario orgánico

Ver calendario-contenido-jul-2026.md: 10 piezas en borrador en Metricool del 14 al 19 de julio, pendientes de aprobar en el planner.

## Regla de gobernanza

Ninguna publicación, campaña, cobranza o aviso sale sin aprobación explícita de Daniel. El agente propone, Daniel aprueba, el agente ejecuta.
