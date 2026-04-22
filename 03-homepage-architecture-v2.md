# 03 — Arquitectura Homepage v2 — IA System

Fecha: 2026-04-13

---

## Resumen ejecutivo

La arquitectura v2 reordena y reescribe las secciones para que el visitante pase por una secuencia persuasiva clara: tension > credibilidad > oferta concreta > diferenciacion > prueba > ruta de accion. Cada seccion tiene un trabajo especifico. Si no hace ese trabajo, no tiene razon de existir.

---

## Principio de diseno arquitectonico

La homepage no es un brochure. Es una conversacion de venta en silencio.

Cada seccion debe responder a una pregunta implicita del prospecto:
1. "Esto es para mi?" — Hero
2. "Por que deberia cambiar lo que hago hoy?" — Problema
3. "Que es esto exactamente?" — Oferta
4. "Que recibo y cuando?" — Deliverables
5. "Como funciona?" — Proceso
6. "Por que esto y no una agencia o freelancer?" — Comparativa
7. "Esto es para mi, especificamente?" — ICP + filtro negativo
8. "Quien esta detras de esto?" — Autoridad
9. "Funciona para otros?" — Prueba social
10. "Que pasa si entro?" — CTA especifico
11. "Que preguntas tengo antes de decidir?" — FAQ

---

## Arquitectura de secciones v2

### Seccion 0 — Nav
**Trabajo:** Orientacion rapida + CTA siempre visible
**Cambios vs v1:**
- Mantener estructura fija
- Reemplazar "Experiencia" en nav por "Resultados" o "Sistema"
- CTA nav: cambiar "Escribir por WhatsApp" a "Diagnostico gratuito" — mas especifico, mas valor

**Links de nav v2:** Sistema / Proceso / Para quien / Resultados / [CTA: Diagnostico gratuito]

---

### Seccion 1 — Hero
**Trabajo:** Crear tension inmediata y hacer que el prospecto correcto diga "esto es exactamente lo que necesito"
**Tiempo de atencion disponible:** 5 segundos

**Estructura:**
- Label caps: etiqueta que contextualiza la categoria
- H1: headline de maximo impacto, orientado a outcome, con tension
- Subheadline: 2 lineas que especifican el modelo y lo que lo diferencia
- CTA primario: btn-primary gold — "Agenda tu diagnostico gratuito"
- CTA secundario: btn-ghost — "Ver como funciona"
- Proof bar: 3-4 datos verificables o logos (no descriptivos)

**Proof bar v2 (reemplaza trust bar actual):**
- Dato 1: "Negocios de servicios en Mexico" (con numero si hay)
- Dato 2: "Desde [ciudad o sector] — con resultado medible"
- Dato 3: Certificacion real (CAIO, CONOCER, etc.)
- Dato 4: Modelo claro — "Retainer mensual. Sin contrato anual."

**Nota:** Si no hay numeros reales disponibles, usar los 3-4 certificaciones/credenciales como proof bar, no datos descriptivos de la empresa.

---

### Seccion 2 — Problema (agitacion)
**Trabajo:** Hacer que el prospecto reconozca su situacion actual como inaceptable y urgente
**Diferencia vs v1:** La version actual enumera sintomas. La v2 debe conectar sintomas con costo de negocio.

**Estructura:**
- Label caps: "Por que no funciona lo que hiciste hasta hoy"
- H2: headline que nombra el estado actual con precision
- Lista de 4-5 sintomas — cada uno con su costo de negocio implicito
- Elemento de tension final: cuanto le cuesta cada mes no tener sistema

**Formato:** Lista numerada con dos capas:
- Sintoma (lo que ve el cliente)
- Costo (lo que pierde por eso, aunque no lo sepa)

---

### Seccion 3 — Que es IA System (definicion de la oferta)
**Trabajo:** Definir con exactitud que es el producto, que no es, y por que existe
**Diferencia vs v1:** Menos abstracto, mas productizado

**Estructura:**
- Label caps: "Que es IA System"
- H2: definicion directa de lo que es
- Parrafo de una sola oracion: la promesa central
- Bloque de 3 columnas: los 3 pilares del sistema (reescritos con diferenciacion real)
- Mini-tabla o bloque: "IA System es / No es" — claridad absoluta sobre la categoria

**Los 3 pilares v2 (reemplaza Claridad / Consistencia / Optimizacion):**
1. Operacion completa (no solo estrategia) — "Definimos, ejecutamos, medimos y ajustamos. Tu no briefeas ni supervisas."
2. IA en cada capa — "Produccion, analisis, seguimiento y optimizacion con inteligencia artificial. Velocidad sin inflacion de equipo."
3. Orientado a conversion B2B — "No construimos audiencias. Construimos sistemas de adquisicion para servicios de alto valor."

---

### Seccion 4 — Que incluye (deliverables concretos)
**Trabajo:** Convertir la oferta abstracta en una lista concreta de lo que recibe el cliente cada mes
**Diferencia vs v1:** Version actual tiene 5 items vagos. V2 tiene items con frecuencia, formato y resultado esperado.

**Estructura:**
- Label caps: "Que recibes cada mes"
- H2: headline orientado a tangibles
- Lista de 6-8 deliverables con formato: [Nombre] / [Frecuencia] / [Para que sirve]
- Nota de cierre: "Todo en un solo retainer. Sin proveedores adicionales."
- CTA inline: btn-ghost — "Ver planes por WhatsApp"

**Deliverables v2 propuestos:**
1. Estrategia de contenido mensual — 1 por mes — Define que publicar, cuando y con que objetivo de conversion
2. Contenido producido y publicado — 8-16 piezas/mes segun plan — LinkedIn, Instagram u otros segun ICP
3. Landing page o pagina de conversion — 1 por ciclo inicial — Disenada para convertir visitas en leads
4. Flujos de seguimiento automatizados — Setup en primer mes + optimizacion mensual — Nurturing y activacion de oportunidades sin esfuerzo manual
5. Reporte mensual de performance — 1 por mes — Metricas reales: alcance, leads generados, llamadas agendadas, ajustes del siguiente ciclo
6. Sesion de estrategia mensual — 1 call de 45-60 min — Revision de resultados, ajustes de sistema y prioridades del siguiente mes
7. Actualizaciones de sistema con IA — Continuo — Optimizacion de prompts, automatizaciones y flujos segun datos del mes

**Nota:** Validar con Salvador los deliverables exactos antes de publicar. Estos son propuestos como version v2.

---

### Seccion 5 — Proceso (como funciona)
**Trabajo:** Reducir el riesgo percibido mostrando que hay una metodologia clara y predecible
**Diferencia vs v1:** Agregar output concreto al final de cada fase

**Estructura:**
- Label caps: "Como funciona"
- H2: "De cero a sistema en 90 dias."
- 4 pasos con: numero, nombre, descripcion y OUTPUT concreto
- Timeline visual simple: Mes 1 / Mes 2 / Mes 3+

**Pasos v2:**
1. Diagnostico (Semana 1-2) — Mapeamos tu negocio, ICP, canales y brechas. OUTPUT: Mapa de conversion especifico para tu negocio.
2. Arquitectura (Semana 3-4) — Definimos sistema, mensajes, canales y landing page. OUTPUT: Sistema de conversion disenado y documentado.
3. Activacion (Mes 2) — Publicamos, automatizamos y activamos el primer ciclo de contacto. OUTPUT: Primeras piezas publicadas, flujos activos y primeras oportunidades identificadas.
4. Operacion continua (Mes 3+) — Operamos, medimos y optimizamos cada mes. OUTPUT: Reporte mensual con metricas reales y ajustes de sistema.

---

### Seccion 6 — Comparativa (diferenciacion explicita)
**Trabajo:** Eliminar la comparacion implicita con agencias y hacerla explicita para favorecer a IA System
**Nueva seccion — no existia en v1**

**Estructura:**
- Label caps: "Por que no una agencia"
- H2: headline de tension directo
- Tabla comparativa 4 columnas: IA System / Agencia / Freelancer / Tu mismo
- Filas: Estrategia / Ejecucion / Datos / Costo / Tiempo que consume / Resultado orientado a

**Nota:** La tabla debe ser honesta, no soberbia. Reconocer donde las alternativas son mejores y donde IA System gana claramente.

---

### Seccion 7 — Para quien
**Trabajo:** Filtrar prospectos antes del diagnostico para mejorar calidad de leads
**Diferencia vs v1:** Agregar filtro negativo explicito

**Estructura:**
- Label caps: "Para quien es IA System"
- H2: headline de filtro positivo
- Grid de ICPs (conservar los 5 actuales, reescribir copy)
- Bloque separado: "IA System NO es para ti si..." — 3-4 criterios de exclusion
- CTA inline despues del filtro negativo

**Filtro negativo propuesto:**
- Vendes productos fisicos o tienes e-commerce
- Buscas solo alguien que "te lleve las redes" sin sistema
- Tu ticket de servicio es menor a $10,000 MXN por cliente
- No tienes presupuesto para invertir en sistema de marketing (mas de $X,XXX MXN/mes)
- Quieres resultados en menos de 30 dias sin construccion de base

---

### Seccion 8 — Autoridad
**Trabajo:** Generar confianza personal en quien opera el sistema
**Diferencia vs v1:** Poner nombre, foto, cargo especifico y un dato de impacto real

**Estructura:**
- Label caps: "Quien opera el sistema"
- Foto (si disponible) o avatar de marca
- Nombre completo: Salvador Villarreal
- Cargo: Fundador de IA System / Fractional CAIO
- 2-3 oraciones de bio orientadas a resultado, no a curriculum
- Credenciales: listado de certificaciones con nombre especifico
- Link a LinkedIn como verificacion

---

### Seccion 9 — Prueba social
**Trabajo:** Validar que el sistema funciona para otros como el prospecto
**Diferencia vs v1:** Eliminar placeholders vacios. Usar solo prueba verificable.

**Opciones por prioridad:**
1. Testimonios reales con nombre + empresa + foto — ideal
2. Logos de clientes actuales — si hay permiso
3. Mini caso de uso con contexto + resultado + cargo (sin nombre si no hay permiso) — minimo viable
4. Si no hay nada verificable: eliminar la seccion y cubrir el espacio con la seccion comparativa o FAQ

**Formato de testimonio ideal:**
- Cita entre comillas
- Nombre completo
- Cargo y empresa o sector
- Resultado especifico si lo autorizan ("En 60 dias tenia 3 llamadas agendadas por semana de LinkedIn")

---

### Seccion 10 — CTA Final
**Trabajo:** Convertir la intencion en accion con la menor friccion posible
**Diferencia vs v1:** Especificar que recibe el prospecto en el diagnostico. Eliminar ambiguedad.

**Estructura:**
- gold-line decorativa
- Label caps: "Siguiente paso"
- H2: headline de accion con claridad de valor
- Descripcion del diagnostico: que pasa en la llamada, cuanto dura, que se lleva el prospecto
- CTA primario: "Agenda tu diagnostico gratuito por WhatsApp"
- Micro-copy: "30 minutos. Sin venta. Sin compromiso."
- Link secundario a LinkedIn como alternativa

---

### Seccion 11 — FAQ
**Trabajo:** Eliminar las ultimas objeciones antes de la decision
**Diferencia vs v1:** Agregar 2 preguntas criticas faltantes

**Preguntas actuales (conservar y mejorar respuestas):**
1. En que es diferente a contratar una agencia de marketing?
2. Cuanto cuesta el retainer mensual?
3. En cuanto tiempo se ven resultados reales?
4. Que pasa si ya tengo alguien haciendo mis redes?
5. Trabajan con cualquier tipo de negocio?
6. Tengo que firmar un contrato largo?

**Preguntas nuevas a agregar:**
7. Como es el proceso de onboarding? Que pasa en los primeros 30 dias?
8. Como garantizan los resultados? Que pasa si no funcionan?

---

### Seccion 12 — Footer
**Trabajo:** Navegacion secundaria + links legales + contacto
**Cambios vs v1:**
- Unificar a un solo numero de WhatsApp en CTA
- El segundo numero puede ir en footer como "Contacto alternativo: +52 477 144 9904"
- Mantener links: privacidad, terminos
- Mantener credito: "Una propuesta de Estrategias Vitales IA"

---

## Flujo de conversion esperado

```
Visita -> Hero (5 seg) -> Reconoce problema -> Lee oferta -> Ve deliverables -> Evalua proceso
-> Compara alternativas -> Confirma que es su perfil -> Valida autoridad -> Lee testimonios
-> Lee FAQ -> Hace clic en CTA -> WhatsApp
```

Punto de salida mas probable sin conversion: entre Seccion 1 y Seccion 3.
Por eso: el hero y la definicion de oferta son las dos secciones de mayor prioridad en v2.

---

## Orden final de secciones v2

| # | Seccion | Prioridad | Estado |
|---|---|---|---|
| 0 | Nav | Alta | Conservar + ajustar CTA |
| 1 | Hero | Critica | Reescribir completo |
| 2 | Problema | Alta | Reescribir con costo de negocio |
| 3 | Que es IA System | Critica | Reescribir con diferenciadores reales |
| 4 | Deliverables (Que incluye) | Alta | Reescribir con especificidad |
| 5 | Proceso | Media | Reescribir con outputs por fase |
| 6 | Comparativa | Nueva | Crear desde cero |
| 7 | Para quien + filtro negativo | Alta | Reescribir con exclusion explicita |
| 8 | Autoridad | Media | Reescribir con nombre y datos reales |
| 9 | Prueba social | Alta | Reemplazar o eliminar placeholders |
| 10 | CTA Final | Alta | Reescribir con valor del diagnostico |
| 11 | FAQ | Media | Conservar + agregar 2 preguntas |
| 12 | Footer | Baja | Conservar + unificar WhatsApp |
