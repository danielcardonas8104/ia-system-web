# 05 — Direccion UI v2 — IA System

Fecha: 2026-04-13

---

## Resumen ejecutivo

La direccion visual v2 mantiene el sistema de diseno existente (paleta, tipografia, componentes) y lo densifica: mas contraste, mas jerarquia, mas tension visual, mas espacio usado para transmitir valor comercial en lugar de espacio usado para respirar elegancia. El objetivo es pasar de "landing page premium" a "hard-offer page con caracter".

La regla maestra: cada decision visual debe servir a la conversion, no al esteticismo.

---

## Lo que se conserva exactamente

### Paleta de color
- Fondo: #0d0d0d (negro profundo)
- Texto primario: #f0ebe0 (crema)
- Texto secundario: #c4bdb1 (crema opaco)
- Texto terciario: #7a7067 (crema apagado)
- Acento principal: #c9a962 (gold)
- Acento secundario: #dfc07e (gold claro, hover)
- Borde sutil: #1c1c1c
- Card background: #141414
- Card highlight border: rgba(201,169,98,0.19)

### Tipografia
- Display/serif: Playfair Display — mantener para H1, H2 y citas
- Cuerpo/sans: Inter — mantener para labels, parrafos, botones, UI
- No agregar fuentes nuevas

### Componentes existentes reutilizables
- .btn-primary (gold solido)
- .btn-ghost (borde crema)
- .card (borde sutil #1c1c1c)
- .card-highlight (borde gold transparente)
- .label-caps (caps dorado)
- .gold-line (linea decorativa 2rem)
- .step-number (numero grande Playfair)
- .fade-in (animacion scroll)
- .heading-display, .heading-serif

---

## Lo que cambia — direccion visual v2

### 1. Hero — de poetico a declarativo

**v1:** Hero limpio, mucho espacio, headline elegante, CTA suave.
**v2:** Hero con mayor contraste y jerarquia. El H1 debe golpear desde el primer vistazo.

Cambios especificos:
- H1 size: mantener clamp(2.5rem, 6vw, 5rem) pero aumentar font-weight a 600 para mas impacto
- Agregar una linea horizontal gold (#c9a962) de 1px arriba del label-caps como marcador de entrada
- Proof bar: reemplazar los 4 datos descriptivos por datos verificables. Si hay logotipos de clientes, usarlos en gris muy sutil (#2a2a2a) con hover a crema.
- Aumentar contraste del subheadline: de font-weight 300 a font-weight 400 para mejor legibilidad en mobile

### 2. Seccion problema — mas densidad, menos espacio

**v1:** Grid 2 columnas con bastante espacio blanco (negro).
**v2:** Mantener grid pero aumentar densidad informacional. Cada punto de dolor ahora tiene 2 capas (sintoma + costo).

Cambios especificos:
- Agregar segunda linea de texto en cada item de la lista — el "consecuencia" en text-crema-faint
- Sintoma en text-crema-muted, costo en text-crema-faint (mas oscuro para crear jerarquia de escaneo)
- Al final de la seccion: bloque de tension en una sola linea — fondo ligeramente diferente (#111111) o borde izquierdo gold de 2px

### 3. Cards del sistema — de abstractas a productizadas

**v1:** 3 cards con gold-line y texto descriptivo suave.
**v2:** 3 cards con numero de pilar visible, titulos declarativos y una "prueba" de diferenciacion debajo del titulo.

Cambios especificos:
- Agregar numero de pilar (01, 02, 03) en Playfair Display, font-size 0.75rem, color gold, sobre el titulo
- Titulos mas cortos y declarativos (no descriptivos)
- Agregar 1 linea de "contraste" en cada card: lo que hacen otros vs lo que hace IA System
- Mantener gold-line decorativa

### 4. Tabla comparativa — nueva seccion, alta densidad

Nueva seccion entre Proceso y Para quien.

Especificaciones:
- Tabla responsive: 4 columnas en desktop, 2 columnas (IA System vs [alternativa]) en mobile con tabs o scroll horizontal
- Header de columna: IA System en gold, resto en crema-faint
- Columna IA System: fondo ligeramente diferenciado (card-highlight con borde gold) para destacarla visualmente
- Check icon en gold (#c9a962) para los SI de IA System
- X icon en #3a3a3a (gris oscuro) para los NO de alternativas
- No usar rojo: mantiene la estetica premium, no genera alarma

Especificacion del X icon:
```
<svg width="14" height="14" viewBox="0 0 14 14" fill="none">
  <path d="M3 3l8 8M11 3l-8 8" stroke="#3a3a3a" stroke-width="1.5" stroke-linecap="round"/>
</svg>
```

### 5. Seccion deliverables — de checklist a grid de valor

**v1:** Lista vertical de 5 items con check dorado y descripcion.
**v2:** Grid 2 columnas (desktop) / 1 columna (mobile) de cards mas visuales.

Cambios especificos:
- Cada deliverable en su propia card-highlight
- Estructura de card: [Nombre del deliverable] / [Frecuencia] / [Para que sirve]
- Frecuencia en label-caps (dorado, caps) encima del nombre
- Descripcion en text-crema-faint
- Al final: bloque resumen "Todo esto en un solo retainer mensual" con linea horizontal gold

### 6. Seccion autoridad — de anonima a personal

**v1:** Dos columnas: texto a la izquierda (muy generico), 3 cards a la derecha (certificaciones).
**v2:** Misma estructura pero con nombre visible, bio directa y credenciales bien jerarquizadas.

Cambios especificos:
- H2 reemplaza "Experiencia real en negocios reales" por el nombre real + cargo
- Agregar foto si esta disponible (circular, 80px de diametro, con border gold de 1px)
- Bio en 2 parrafos: quien es + que hace con IA System
- Certificaciones en lista ordenada con nombre exacto de la certificacion (no solo "Certificacion en IA")
- LinkedIn como validacion externa visible con icono

### 7. Proof bar en hero — logos de clientes

Si hay logotipos disponibles de clientes actuales:
- Mostrarlos en gris muy claro (#252525) con hover a crema (#f0ebe0 a 40% de opacidad)
- Tamano: max 120px de ancho, 24px de alto
- Separados por puntos dorados (·) o dividers verticales de 1px
- Label caps encima: "Negocios que operan con el sistema"

Si no hay logotipos: usar alternativa de credenciales (ver proof bar de hero en copy deck).

### 8. Filtro negativo — bloque de exclusion visual

Nueva subseccion dentro de "Para quien".

Especificaciones:
- Fondo #111111 (ligeramente diferente al negro base)
- Borde izquierdo de 2px en color #3a3a3a (no gold — el gold es para lo positivo)
- Label caps en #7a7067 (no en gold): "IA System NO es para ti si:"
- Lista con X icon en #3a3a3a para cada exclusion
- Padding 1.5rem, borde completo sutil #1c1c1c

### 9. CTA Final — de suave a declarativo

**v1:** Texto en centro, fondo negro, boton gold.
**v2:** Misma estructura pero con mayor densidad de valor en el copy y una linea de friccin-reduccion explicita.

Cambios especificos:
- Bloque de valor del diagnostico: 3 bullets de lo que recibe el prospecto en la sesion (incluso si no contrata)
- Micro-copy adicional debajo del CTA: "Diagnostico sin costo. Sin presentacion de ventas. Sin compromiso."
- Mantener gold-line decorativa en top de seccion

---

## Animaciones GSAP — reglas v2

### Conservar
- Fade-in en scroll para todas las secciones (ya implementado, funciona bien)
- Fallback a visible si GSAP no carga
- Respeto a prefers-reduced-motion

### Agregar en v2
- Counter animation en las metricas del hero proof bar (si hay numeros reales): contar de 0 a N en 1.2 segundos al entrar en viewport
- Gold-line entrance: scale de 0 a 1 desde la izquierda (transform-origin: left center) — ya esta en el CSS pero agregar en GSAP para que sea consistente con el resto
- Tabla comparativa: fade-in de filas en secuencia con stagger de 0.08s (sutil, no llamativo)

### NO agregar
- Parallax en textos (afecta legibilidad)
- Animaciones en CTAs (distrae del clic)
- Hover states animados complejos en botones (el actual transform: translateY(-1px) es suficiente)
- Cualquier animacion que dure mas de 0.7 segundos en elementos inline de conversion

---

## Mobile-first — especificaciones criticas

### Breakpoints (mantener existentes)
- Base: 375px (iPhone SE — minimo de verificacion)
- sm: 640px
- md: 768px

### Ajustes mobile especificos v2

Hero mobile:
- H1 size: clamp(2rem, 8vw, 2.5rem) — ligeramente menor que v1 para que quepa en 375px sin overflow
- CTA stack: ambos botones full-width en mobile, stacked verticalmente
- Proof bar: 2 columnas de 2 en mobile (grid 2x2), no 1 columna vertical (demasiado alto)

Tabla comparativa mobile:
- Mostrar solo 2 columnas: IA System + una alternativa a la vez
- Selector de alternativa: 3 botones pill (Agencia / Freelancer / Tu mismo) encima de la tabla
- Cambio de columna con fade transition de 0.2s

Deliverables mobile:
- 1 columna full-width en lugar de grid 2 columnas
- Cards mas compactas: reducir padding de 1.25rem a 1rem en mobile

---

## Jerarquia visual de pagina completa

Nivel 1 — Impacto inmediato (H1, CTA primario): Playfair 500, gold en acento, btn-primary gold
Nivel 2 — Orientacion (H2, label-caps): Playfair 400, crema, gold en label
Nivel 3 — Contenido (H3, parrafos): Inter 400-500, crema-muted
Nivel 4 — Soporte (descripciones, microcopy): Inter 300, crema-faint

Regla: nunca usar font-weight 300 en texto de mas de 40 caracteres en mobile. La legibilidad se degrada en pantallas pequenas con fonts muy delgadas.

---

## Checklist de inspeccion visual antes de build

- [ ] H1 se lee completo en 375px sin overflow horizontal
- [ ] btn-primary tiene al menos 44px de altura (touch target accesible)
- [ ] Contraste de texto: todos los textos pasan WCAG AA (4.5:1 minimo para texto normal)
- [ ] La tabla comparativa no desborda en 375px
- [ ] El filtro negativo no parece alarma — tono neutro, no rojo
- [ ] Las certificaciones tienen nombre exacto y verificable
- [ ] Las animaciones no interfieren con la lectura en scroll rapido
- [ ] El CTA de WhatsApp esta visible sin scroll en mobile (above the fold o muy cerca)
- [ ] No hay placeholders vacios visibles en produccion (testimonios, nombres, etc.)
- [ ] Todos los links externos tienen target="_blank" rel="noopener noreferrer"
