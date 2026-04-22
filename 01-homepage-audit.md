# 01 — Auditoria Homepage IA System (version actual)

Fecha de auditoria: 2026-04-13
Base: index.html actual desplegado en iamarketing.mx

---

## Resumen ejecutivo

El sitio tiene base tecnica solida y estetica coherente black/gold. El problema no es visual: es de posicionamiento y densidad comercial. La homepage comunica "consultoria elegante disponible para ti" en lugar de "sistema productizado con entregables concretos y resultados verificables". Un prospecto que llega no sabe exactamente que recibe, cuanto cuesta, ni por que IA System es claramente superior a contratar un freelancer o una agencia. Eso frena la conversion.

---

## Inventario de secciones actuales

| N | Seccion | Estado |
|---|---|---|
| 1 | Nav fija + CTA WhatsApp | Conservar |
| 2 | Hero | Reescribir |
| 3 | Problema (Lo que suele pasar) | Reescribir parcialmente |
| 4 | Que es IA System (3 cards) | Reescribir con tangibles |
| 5 | Proceso (4 fases) | Reescribir con outputs concretos |
| 6 | Que incluye el retainer (checklist) | Ampliar y reescribir |
| 7 | Para quien (grid 5 ICPs) | Conservar estructura, reescribir copy |
| 8 | Fundador / Autoridad | Reescribir con nombre y credenciales reales |
| 9 | Lo que cambia (3 numeros) | Eliminar o reemplazar con metricas reales |
| 10 | Prueba social (3 testimonios placeholder) | Eliminar hasta tener testimonios reales |
| 11 | FAQ (6 preguntas) | Conservar, agregar 2 preguntas, reescribir 2 respuestas |
| 12 | CTA Final / Diagnostico | Reescribir con mas especificidad de valor |
| 13 | Footer | Conservar estructura, unificar WhatsApp |

---

## Lo que funciona — conservar sin cambios

### Tecnico
- Stack autocontenido HTML + CSS custom + GSAP: no requiere cambio de framework
- SEO: title, meta description, canonical, Open Graph, JSON-LD schema completo
- Accesibilidad: skip-link, aria-labels, roles semanticos
- Favicon, manifest, robots, sitemap: completos
- FAQ accordion con GSAP fallback y prefers-reduced-motion

### Visual / marca
- Paleta: #0d0d0d (negro), #f0ebe0 (crema), #c9a962 (gold) — mantener exactamente
- Tipografia: Playfair Display (display/serif) + Inter (cuerpo) — mantener
- Componentes: btn-primary gold, btn-ghost, card, card-highlight, label-caps, gold-line

### Copy rescatable
- "No una agencia. No un freelancer." — potente, ampliar como seccion comparativa
- "No prometemos viralidad. Prometemos conversion." — subir a near-hero o hero
- FAQ respuesta sobre diferencia con agencias: la mejor del sitio, ampliar
- "Tienes valor real. Tu presencia no lo comunica." — conservar como headline de problema
- FAQ respuesta sobre ICP: "No. IA System esta disenado especificamente para..." — llevar a seccion para-quien como criterio de filtro explicito

---

## Lo que hay que eliminar

### 1. Trust bar del hero con datos descriptivos
Copy actual: "Guadalajara, Mexico / B2B y MiPyMEs / Retainer mensual / Consultores certificados en IA"
Problema: es descripcion de la empresa, no social proof. No genera confianza ni urgencia. Un prospecto nuevo no sabe si eso es relevante para el.
Reemplazar por: cifra de impacto real, logotipos de clientes, o un diferenciador cuantificado.

### 2. Seccion de testimonios con nombres vacios
Problema critico: tres testimonios sin nombre, sin empresa, sin foto. Eso es peor que no tener testimonios: activa la desconfianza del visitante.
Accion: eliminar completamente de la build v2. Reemplazar con seccion de comparativa o entregables hasta tener testimonios reales verificados.

### 3. Metricas debiles en "Lo que cambia"
Cifras actuales: "3-6 meses para un sistema solido", "100% orientado a tu modelo", "1 retainer todo incluido"
Problema: no son metricas de resultado para el cliente. Son caracteristicas del servicio disfrazadas de numeros. "100%" no dice nada.
Reemplazar por: metricas reales orientadas al negocio del cliente (leads generados, llamadas agendadas, reduccion de tiempo operativo).

### 4. Dos numeros de WhatsApp en CTA
Problema: genera confusion. El prospecto no sabe a quien escribir ni si son distintos equipos.
Accion: usar solo +52 333 337 1696 como CTA principal. El segundo puede ir en footer como dato de contacto secundario con contexto.

### 5. Seccion "Fundador / Autoridad" sin identidad
"Experiencia real en negocios reales" — cliche sin dato especifico.
"System es operado por consultores certificados en Inteligencia Artificial (IA) y Fractional CAIO..." — no dice quien es Salvador.
Reescribir con: nombre (Salvador Villarreal), rol exacto (Fundador, Fractional CAIO), certificaciones por nombre, un dato de impacto concreto.

### 6. Cards de sistema sin diferenciacion
"Claridad estrategica", "Consistencia operada", "Optimizacion continua" — podrian ser el tagline de cualquier agencia de marketing del pais.
Reemplazar por: los 3 diferenciadores reales y verificables de IA System vs alternativas.

---

## Lo que hay que reescribir

### Hero
H1 actual: "Tu expertise merece un sistema que convierta."
Problema: poetico pero vago. No hay outcome especifico, no hay deliverable, no hay diferenciador.
Nuevo angulo: debe mencionar el problema especifico del ICP (no tener leads sin referidos), el outcome concreto (conversaciones agendadas), y el modelo unico (sistema operado, no solo estrategia).

Subheadline actual: "No es cuestion de publicar mas. Es cuestion de tener un sistema..."
Rescatable parcialmente pero necesita mas especificidad: que hace el sistema exactamente y que produce.

CTA actual: "Escribir por WhatsApp" — correcto. Conservar texto y destino. Agregar micro-copy debajo: "Diagnostico gratuito, sin compromiso."

### Proceso (4 fases)
Problema: los pasos son correctos en logica pero no dicen que produce cada fase.
- Fase 1 Diagnostico: agregar output — "Recibe un mapa de brechas y oportunidades de conversion especifico para tu negocio."
- Fase 2 Arquitectura: agregar output — "Defines con nosotros canales, mensajes clave, landing page y flujo de contacto."
- Fase 3 Operacion: agregar output — "Contenido publicado, seguimiento activo y oportunidades activadas cada mes."
- Fase 4 Optimizacion: agregar output — "Reporte mensual con metricas reales: alcance, leads, llamadas. Ajustes basados en datos."

### Que incluye el retainer
La lista actual es correcta en estructura pero los items son vagos. Cada item necesita:
- Nombre del deliverable (especifico)
- Frecuencia o cantidad (mensual, semanal, por ciclo)
- Resultado esperado

### FAQ — agregar 2 preguntas
- "Como es el proceso de onboarding? Que pasa en los primeros 30 dias?" — es la pregunta que todo prospecto tiene antes de firmar.
- "Hay un rango de precio?" — aunque no se publique precio exacto, dar referencia para filtrar prospectos que no califican por presupuesto.

---

## Brechas criticas vs hard-offer page

| Elemento | Estado actual | Estado requerido para v2 |
|---|---|---|
| Oferta especifica con deliverables | Abstracta | Lista exacta de lo que incluye el sistema, con frecuencia |
| Precio o ancla de precio | Oculto | Rango minimo o modelo de acceso para filtrar |
| Comparativa directa vs alternativas | Solo una respuesta de FAQ | Seccion visual dedicada: IA System vs agencia vs freelancer vs DIY |
| Social proof verificable | Placeholders vacios | Logos de clientes o eliminar la seccion |
| Urgencia o escasez | Ninguna | Cupos limitados, proceso de admision o fecha de inicio de siguiente ciclo |
| Garantia o risk reversal | Ninguna mencionada | "Diagnostico sin costo, sin compromiso" como CTA primario con valor explicito |
| Case study o resultado especifico | Ninguno | Al menos un mini caso con contexto, problema, accion y resultado |
| Identidad del operador | Oculto | Salvador Villarreal visible, con cargo, certificaciones y un dato de impacto |
| Filtro de ICP negativo | Ausente | "IA System NO es para ti si..." — mejora calidad de leads |
