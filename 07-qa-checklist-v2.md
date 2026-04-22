# 07 — QA Checklist v2 — IA System

Fecha: 2026-04-13
Ejecutar despues de completar la implementacion de index-v2.html y antes del deploy a produccion.

---

## Como usar este checklist

- Marcar cada item como [x] cuando este verificado
- Marcar como [!] cuando haya un problema que requiera correccion
- No pasar al deploy hasta que todos los items criticos esten [x]
- Items marcados como CRITICO son bloqueantes — no deployar si fallan
- Items marcados como IMPORTANTE son recomendados — deployar con seguimiento inmediato
- Items marcados como OPCIONAL son mejoras que pueden ir en un ciclo posterior

---

## 1. Contenido — Ausencia de placeholders

CRITICO
- [ ] No hay texto "[IA SYSTEM: ...]" visible en ninguna seccion
- [ ] No hay nombres vacios en testimonios (si se mantiene la seccion)
- [ ] No hay campos "<!-- [IA SYSTEM: Nombre] -->" en el HTML renderizado
- [ ] Todos los [VALIDAR] del copy deck fueron resueltos y el texto final esta en el HTML
- [ ] Todos los [CONFIRMAR] del copy deck fueron decididos y el texto final esta en el HTML
- [ ] El rango de precio en FAQ tiene contenido real o la pregunta fue eliminada/ajustada

---

## 2. Links y CTAs

CRITICO
- [ ] El CTA principal de WhatsApp abre el chat correcto con el mensaje pre-cargado
- [ ] El numero de WhatsApp en todos los CTAs es el mismo (un solo numero principal)
- [ ] El link de LinkedIn abre el perfil de Salvador Villarreal correctamente
- [ ] Todos los links externos tienen target="_blank" y rel="noopener noreferrer"
- [ ] No hay links rotos o 404 en ninguna seccion

IMPORTANTE
- [ ] El mensaje pre-cargado en WhatsApp tiene sentido en el contexto del CTA que lo activa
- [ ] El CTA de nav es visible y clicable en mobile sin que se superponga con otro elemento

---

## 3. Responsive — Mobile first

CRITICO (verificar en DevTools con 375px de ancho y tambien en un iPhone real si es posible)
- [ ] El H1 del hero se lee completo sin overflow horizontal en 375px
- [ ] Los botones CTA tienen al menos 44px de altura (touch target accesible)
- [ ] No hay texto cortado ni desbordado en ninguna seccion en 375px
- [ ] La tabla comparativa no desborda horizontalmente en 375px
- [ ] Las cards de deliverables son de 1 columna en mobile y se leen bien

IMPORTANTE
- [ ] Verificado en 390px (iPhone 14 Pro)
- [ ] Verificado en 768px (tablet)
- [ ] Verificado en 1280px (desktop estandar)
- [ ] Verificado en 1440px (desktop amplio)

OPCIONAL
- [ ] Verificado en iPhone SE fisica (375px real)
- [ ] Verificado en Android de tamano medio (360px)

---

## 4. Performance

IMPORTANTE
- [ ] Lighthouse Mobile Score > 85 en Performance
- [ ] Lighthouse Desktop Score > 90 en Performance
- [ ] PageSpeed Insights no reporta LCP > 4 segundos en mobile
- [ ] Las fuentes de Google Fonts tienen preconnect y preload correctos
- [ ] GSAP se carga con defer (no bloqueante)
- [ ] Las imagenes (si hay) tienen atributo loading="lazy" salvo el logo en nav

OPCIONAL
- [ ] Core Web Vitals: LCP < 2.5s, CLS < 0.1, FID < 100ms

---

## 5. SEO tecnico

CRITICO
- [ ] meta title tiene entre 50 y 60 caracteres
- [ ] meta description tiene entre 140 y 160 caracteres
- [ ] canonical apunta a https://iamarketing.mx/
- [ ] JSON-LD schema incluye las 2 nuevas preguntas de FAQ
- [ ] JSON-LD schema es valido (verificar en https://search.google.com/test/rich-results)
- [ ] No hay errores de estructura en el HTML (verificar con validador W3C)

IMPORTANTE
- [ ] og:title y og:description reflejan el nuevo posicionamiento v2
- [ ] og:image sigue siendo accesible y es 1200x630
- [ ] robots.txt sigue siendo accesible en /robots.txt
- [ ] sitemap.xml sigue siendo accesible en /sitemap.xml

---

## 6. Accesibilidad

IMPORTANTE
- [ ] Skip link funciona (Tab en el teclado despues de cargar la pagina)
- [ ] Todos los H1, H2, H3 siguen una jerarquia logica (no saltar de H1 a H3)
- [ ] Las imagenes decorativas tienen aria-hidden="true"
- [ ] Las imagenes de contenido tienen alt text descriptivo
- [ ] Los botones y links tienen texto descriptivo o aria-label
- [ ] El FAQ accordion actualiza correctamente aria-expanded al abrir/cerrar
- [ ] El contraste de texto vs fondo pasa WCAG AA:
  - [ ] text-crema (#f0ebe0) sobre #0d0d0d: pasa (ratio ~14:1)
  - [ ] text-crema-muted (#c4bdb1) sobre #0d0d0d: pasa (ratio ~9:1)
  - [ ] text-crema-faint (#7a7067) sobre #0d0d0d: verificar (puede estar en el limite)
  - [ ] text-oro (#c9a962) sobre #0d0d0d: verificar (gold oscuro puede fallar en texto pequeno)

OPCIONAL
- [ ] Navegacion completa con teclado funciona correctamente
- [ ] Screen reader anuncia correctamente el estado del FAQ accordion

---

## 7. Funcionalidad JavaScript

CRITICO
- [ ] FAQ accordion funciona en todos los breakpoints
- [ ] Al abrir un item del FAQ, los demas se cierran correctamente
- [ ] Las animaciones fade-in de scroll funcionan al hacer scroll hacia abajo

IMPORTANTE
- [ ] Si GSAP no carga (desconectar red y recargar), todos los elementos son visibles (fallback funciona)
- [ ] prefers-reduced-motion: con la preferencia activada en el OS, los elementos aparecen sin animacion
- [ ] Si hay tabla comparativa con tabs en mobile: los tabs cambian la columna visible correctamente
- [ ] Si hay counter animation: los contadores parten desde 0 y llegan al valor final en ~1.2 segundos

---

## 8. Validacion comercial

IMPORTANTE (validar con Salvador antes de deploy)
- [ ] El copy del hero refleja exactamente el posicionamiento v2 aprobado
- [ ] Los deliverables listados coinciden con lo que realmente se entrega en el retainer
- [ ] El proceso descrito (fases y outputs) coincide con el proceso real de onboarding
- [ ] El rango de precio en FAQ (si se incluye) es el rango real aprobado
- [ ] Las certificaciones listadas en la seccion de autoridad son exactas y verificables
- [ ] El filtro negativo de ICP no excluye a prospectos que si califican
- [ ] El mensaje de WhatsApp pre-cargado tiene el tono correcto y no genera confusion

---

## 9. Seccion de testimonios

CRITICO
- [ ] Si la seccion de testimonios existe en v2: tiene CERO placeholders vacios
- [ ] Si la seccion de testimonios existe: cada testimonio tiene nombre real, cargo y cita verificable
- [ ] Si no hay testimonios reales disponibles: la seccion fue eliminada o reemplazada con otra de valor

---

## 10. Consistencia de marca

IMPORTANTE
- [ ] El logo "IA System" con registered mark aparece en nav y footer
- [ ] El acento dorado (#c9a962) se usa solo en: label-caps, CTAs primarios, gold-line, iconos de check, numeros de pilar. No en texto de cuerpo.
- [ ] La tipografia Playfair Display se usa solo en H1, H2, H3 y step-numbers. No en parrafos.
- [ ] Inter se usa en todos los parrafos, labels, botones y UI.
- [ ] Font-weight 300 no se usa en textos de mas de 40 caracteres en mobile.
- [ ] No hay texto con font-weight 300 en elementos de conversion (CTAs, headlines de oferta).

---

## 11. Pre-deploy final

CRITICO (ejecutar justo antes de hacer deploy)
- [ ] `index-v2.html` fue revisado visualmente en browser local (no solo en editor)
- [ ] No hay errores de consola JavaScript en DevTools
- [ ] No hay errores de consola Network en DevTools (recursos que no cargan)
- [ ] El archivo `index-v1-backup.html` esta guardado y es el index.html original sin modificar
- [ ] El comando de rollback esta documentado y disponible (ver build-plan-v2.md)
- [ ] Salvador aprobo visualmente la preview antes del deploy a produccion

---

## Firma de aprobacion pre-deploy

| Item | Estado | Fecha |
|---|---|---|
| Copy aprobado por Salvador | [ ] | |
| Deliverables confirmados | [ ] | |
| Preview revisada en mobile | [ ] | |
| Preview revisada en desktop | [ ] | |
| QA checklist completado | [ ] | |
| Autorizado para deploy | [ ] | |
