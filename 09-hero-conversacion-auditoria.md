# 09 — Auditoría y propuesta: hero del sitio bajo el principio "marketing como conversación"

Fecha: 2026-06-20
Fuente del principio: nota "El mejor marketing no parece marketing" (atención → interés → valor → oferta)
Alcance: `index.html` (hero y primeras secciones). No implementado. Requiere aprobación antes de tocar producción.

---

## Resumen ejecutivo

El hero actual ya cumple lo más difícil del principio: abre con una verdad del lector ("Eres el cuello de botella de tu propio negocio"), no con la marca. El microcopy del CTA ("Sin venta. Te llevas un diagnóstico real") es texto de manual de "conversación, no anuncio".

Donde sí vende demasiado pronto: el eyebrow abre nombrando la categoría de la firma ("Consultoría de IA Operativa"), el subheadline es un volcado de mecanismo ("auditamos, construimos, implementamos") antes de entregar una sola idea de valor, y el precio aparece en el primer frame. Esos tres puntos son los que "huelen a anuncio".

Nota de encuadre: el principio nació para orgánico y pauta (top of funnel, interrumpes a alguien que no te buscó). El sitio es bottom of funnel (llegan con intención). Por eso no se aplica literal "no vendas": se aplica como "que el primer frame continúe la conversación que el prospecto ya trae en la cabeza antes de saltar al pitch".

---

## Diagnóstico: dónde aplica el principio en el sitio

| Contexto | Intención del visitante | Cómo aplica el principio |
|----------|-------------------------|--------------------------|
| Anuncio / orgánico que trae tráfico | Ninguna, estaba entreteniéndose | Fuerte: atención → interés → valor antes de oferta |
| Hero del sitio (llega desde ad) | Tibia, viene de un hook | El hero debe continuar el tono del ad, no cambiar a modo folleto |
| Hero del sitio (llega directo o referido) | Alta, busca resolver | Puede ir más directo a oferta, pero sigue ganando si abre con su problema |

Conclusión: el hero debe abrir conversacional (problema del lector + micro-idea de valor) y recién después ofertar. El resto del sitio (deliverables, proceso, precio, FAQ) sí puede ser directo porque el visitante ya bajó con intención.

---

## Auditoría por elemento del hero

| Elemento | Copy actual | Diagnóstico "conversación" | Veredicto |
|----------|-------------|----------------------------|-----------|
| Eyebrow | "Consultoría de IA Operativa · México · Despachos, Clínicas y Firmas de Alto Valor" | Abre nombrando qué es la firma, no al lector. Suena a etiqueta de empresa. | Ajustar |
| H1 | "Eres el cuello de botella de tu propio negocio. Lo arreglamos con IA." | Abre con verdad del lector. Primera mitad pura conversación, segunda mitad pitch corto. Balance correcto. | Conservar |
| Subheadline | "Auditamos tu operación, construimos tu Base de Conocimiento centralizada e implementamos asistentes de IA..." | Volcado de mecanismo. Vende el proceso antes de dar una idea útil. Es lo que más "huele a anuncio". | Reescribir |
| CTA primario | "Agenda tu diagnóstico operativo" | Oferta clara. Correcta en su posición. | Conservar |
| Microcopy CTA | "30 minutos. Sin venta. Te llevas un diagnóstico real de tu operación." | Ejemplo perfecto del principio: valor aunque no compre, cero presión. | Conservar |
| Proof bar | "CAIO International / Certificación institucional / Sin contrato anual" | Prueba, no pitch. Correcto. | Conservar |
| Stat de precio | "Desde $33,000 MXN · Retainer mensual" en el primer frame | Mostrar precio arriba es vender pronto. Trade-off: también filtra. | Testear mover |

---

## Qué conservar (ya cumple el principio)

- H1: abre con el lector, no con la marca. Es el activo conversacional más fuerte del sitio.
- Microcopy del CTA: "Sin venta. Te llevas un diagnóstico real." Mantener textual.
- Sección Problema (H2 "No es falta de esfuerzo. Eres tú el sistema."): agita el problema del lector antes de ofertar. Correcto.
- FAQ y filtro negativo ("IA System no es para ti si..."): honestidad que baja la sensación de venta forzada.

No romper nada de esto. El objetivo es afinar la entrada, no rehacer un sitio que ya está bien armado.

---

## Propuesta de reescritura

### 1. Eyebrow (abrir con el lector, no con la categoría)

Actual:
"Consultoría de IA Operativa · México · Despachos, Clínicas y Firmas de Alto Valor"

Opción A (recomendada, mantiene el filtro de ICP pero conversacional):
"Para despachos, clínicas y firmas donde todo pasa por el dueño"

Opción B (tensión):
"Si tu negocio se detiene cuando tú no estás, esto es para ti"

Opción C (mínimo cambio, solo reordena para que el lector vaya primero):
"Despachos, clínicas y firmas de alto valor · Consultoría de IA operativa · México"

Nota: A y B mueven el foco de "qué somos" a "quién eres". Conservan la función de filtro de ICP.

### 2. Subheadline (cambiar volcado de mecanismo por outcome + micro-idea de valor)

Actual:
"Auditamos tu operación, construimos tu Base de Conocimiento centralizada e implementamos asistentes de IA que trabajan mientras tú atiendes lo que realmente importa. Sin tecnicismos. Sin fricciones. Con resultados medibles desde el primer mes."

Opción A (recomendada, valor antes de mecanismo):
"El problema no es cuánto trabajas. Es que el negocio no sabe operar sin ti. Construimos el sistema que responde, da seguimiento y resuelve lo repetitivo con tu criterio, para que recuperes tus horas desde el primer mes."

Opción B (outcome directo, mecanismo al final):
"Recupera entre 10 y 20 horas a la semana sin contratar a nadie más. Convertimos tu forma de operar en un sistema con IA que trabaja mientras tú atiendes lo que sí requiere tu criterio."

Opción C (mantiene mecanismo pero lo suaviza y agrega la idea de valor primero):
"Lo que te frena no es falta de esfuerzo, es que todo el conocimiento vive en tu cabeza. Lo convertimos en un sistema con IA que opera sin ti. Sin tecnicismos, con resultados medibles desde el primer mes."

Por qué: la versión actual lista tres verbos de proceso (auditamos, construimos, implementamos) antes de que el lector reciba algo. Las tres opciones entregan primero una idea que resuena ("el negocio no sabe operar sin ti") y dejan el mecanismo después.

### 3. H1 (conservar, variante opcional)

Recomendación: conservar el actual. Si se quiere testear una variante que abra aún más conversacional:

Variante test:
"Tu equipo te pregunta lo mismo 10 veces al día. Y el negocio se para cuando tú no estás."
(subtítulo asume el "lo arreglamos con IA")

Trade-off: la variante es más conversacional pero pierde la palabra "cuello de botella" que ancla todo el sitio. Solo testear, no reemplazar en firme.

### 4. Precio en el primer frame (testear)

Recomendación: mover "Desde $33,000 MXN" fuera del bloque de proof bar del hero y dejarlo en la sección de diagnóstico/CTA final, donde ya aparece. Mantener en el hero solo prueba de autoridad y modelo ("Sin contrato anual").

Trade-off: el precio arriba filtra prospectos sin presupuesto (lo que el posicionamiento v2 busca). Por eso es un test A/B, no un cambio directo. Métrica de decisión: tasa de clic a WhatsApp y calidad de lead en diagnóstico.

---

## Antes / después (vista rápida del hero)

```
ANTES
Eyebrow:   Consultoría de IA Operativa · México · Despachos...
H1:        Eres el cuello de botella de tu propio negocio. Lo arreglamos con IA.
Subhead:   Auditamos tu operación, construimos tu Base de Conocimiento...
CTA:       Agenda tu diagnóstico operativo
Micro:     30 minutos. Sin venta. Te llevas un diagnóstico real.

DESPUÉS (recomendado)
Eyebrow:   Para despachos, clínicas y firmas donde todo pasa por el dueño
H1:        Eres el cuello de botella de tu propio negocio. Lo arreglamos con IA.  (igual)
Subhead:   El problema no es cuánto trabajas. Es que el negocio no sabe operar
           sin ti. Construimos el sistema que responde, da seguimiento y resuelve
           lo repetitivo con tu criterio, para que recuperes tus horas desde el
           primer mes.
CTA:       Agenda tu diagnóstico operativo  (igual)
Micro:     30 minutos. Sin venta. Te llevas un diagnóstico real.  (igual)
```

---

## Riesgos y trade-offs

- Riesgo: sobrecorregir hacia "conversación" y diluir la claridad de oferta que hoy convierte. Mitigación: cambios acotados a eyebrow y subhead; H1, CTA y microcopy se conservan.
- Trade-off precio en hero: quitarlo baja fricción pero deja pasar prospectos sin presupuesto al diagnóstico. Resolver por A/B, no por opinión.
- Riesgo SEO/metadata: si cambia el H1 (no recomendado ahora) hay que revisar title y meta description. Con los cambios propuestos (eyebrow y subhead) no hay impacto en H1, así que el riesgo es bajo.
- El principio aplica con más fuerza a los anuncios que traen el tráfico que al hero. El mayor ROI está en que el creativo del ad sea conversacional y el hero continúe ese tono, no en rehacer el hero.

---

## Supuestos

- El objetivo del hero sigue siendo agendar diagnóstico por WhatsApp.
- "dcf" (de la nota original) es el mismo negocio o uno donde aplica este sitio. Validar.
- Hay tráfico suficiente para correr un A/B con lectura en 2 a 4 semanas. Si no, aplicar la opción recomendada directo y medir contra el histórico.

---

## Plan de implementación (cuando se apruebe)

1. Aprobar opciones de eyebrow y subheadline (A, B o C de cada uno).
2. Editar solo esos dos bloques en `index.html`. No tocar H1, CTA, proof bar ni estructura.
3. Revisar responsive en 375px y 390px (el subhead nuevo es más largo, verificar que no rompa el hero móvil).
4. Decidir el test de precio en hero por separado.
5. Deploy y medir tasa de clic a WhatsApp y calidad de lead a 2-4 semanas.

---

## Siguiente acción recomendada

Elige eyebrow (A/B/C) y subheadline (A/B/C). Con eso implemento el cambio acotado en `index.html`, verifico móvil y lo dejo listo para deploy. El test de precio y la variante de H1 los dejamos como pruebas separadas para no mover dos variables a la vez.
