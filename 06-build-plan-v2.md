# 06 — Build Plan v2 — IA System

Fecha: 2026-04-13

---

## Resumen ejecutivo

La implementacion de homepage v2 se hace en un solo archivo index.html autocontenido, sobre la base tecnica existente (CSS custom + GSAP). No se cambia el framework ni el stack de deploy (Vercel). El plan esta dividido en 3 fases: validacion de contenido, implementacion tecnica y deploy. La fase de validacion es obligatoria antes de tocar el index.html de produccion.

---

## Precondiciones antes de iniciar build

Estos items deben estar resueltos antes de escribir una sola linea de codigo:

- [ ] Salvador revisa y aprueba el copy deck v2 (04-copy-deck-v2.md)
- [ ] Salvador confirma los deliverables exactos del retainer (cantidades, frecuencias)
- [ ] Salvador decide el rango de precio a publicar en FAQ (o confirma que no se publica)
- [ ] Salvador decide entre las opciones de H1 (A, B o C del copy deck)
- [ ] Salvador decide entre las opciones de H2 del CTA final (A o B)
- [ ] Salvador confirma si hay logotipos de clientes disponibles para proof bar
- [ ] Salvador confirma si hay foto disponible para la seccion de autoridad
- [ ] Salvador confirma cuales testimonios reales estan disponibles (si hay) o si se elimina la seccion
- [ ] Salvador confirma el numero de WhatsApp principal a usar en todos los CTAs

---

## Fase 1 — Validacion de contenido (antes de tocar index.html)

**Objetivo:** Tener el copy 100% validado antes de implementar para no hacer doble trabajo de reescritura en el codigo.

**Acciones:**
1. Salvador revisa 04-copy-deck-v2.md y marca o responde cada [VALIDAR] y [CONFIRMAR]
2. Salvador confirma los datos de proof bar del hero
3. Si hay testimonios reales: Salvador los entrega con formato (cita, nombre, cargo, empresa)
4. Si hay logotipos: Salvador los entrega en formato SVG o PNG transparente
5. Se genera version final de copy deck sin marcas [VALIDAR] ni [CONFIRMAR]

**Duracion estimada:** 1 sesion de trabajo con Salvador (30-60 min de revision + ajustes)

---

## Fase 2 — Implementacion tecnica

### Estrategia de implementacion

No modificar index.html directamente en produccion.

Flujo de trabajo:
1. Crear `index-v2.html` en la raiz del proyecto (copia del index.html actual como base)
2. Implementar todos los cambios en `index-v2.html`
3. Revisar y aprobar en preview de Vercel
4. Renombrar: `index.html` -> `index-v1-backup.html`, `index-v2.html` -> `index.html`
5. Deploy final

### Orden de implementacion por seccion

Prioridad critica (implementar primero, mayor impacto en conversion):
1. Hero — H1, subheadline, proof bar, CTAs
2. Que es IA System — 3 pilares reescritos + bloque ES/NO ES
3. Deliverables — grid con frecuencias y outputs

Prioridad alta (implementar en segunda ronda):
4. Problema — sintomas + costos de negocio
5. Comparativa — tabla nueva
6. CTA Final — con descripcion de valor del diagnostico

Prioridad media (implementar en tercera ronda):
7. Proceso — con outputs por fase
8. Para quien — con filtro negativo
9. Autoridad — con nombre, bio y certificaciones exactas
10. FAQ — agregar 2 preguntas nuevas, mejorar respuestas

Prioridad baja (implementar al final):
11. Nav — cambiar CTA a "Diagnostico gratuito"
12. Footer — unificar WhatsApp
13. Eliminar seccion de testimonios placeholder (o reemplazar)
14. Eliminar seccion "Lo que cambia" con metricas vacias

### Cambios tecnicos adicionales

Tabla comparativa mobile (nueva logica):
- HTML: tabla con clase `comparison-table`
- JS: 3 botones pill que filtran que columna mostrar en mobile (show/hide via clase)
- Sin dependencias nuevas — puro JS vanilla

Counter animation en proof bar (si hay numeros reales):
- GSAP: `gsap.from(counter, { textContent: 0, duration: 1.2, snap: { textContent: 1 } })` al entrar en viewport con ScrollTrigger
- Solo activar si hay datos numericos reales

SEO updates para v2:
- Actualizar meta description con nuevo positioning
- Actualizar og:description
- Actualizar JSON-LD schema FAQPage con las 2 preguntas nuevas
- Verificar canonical sigue siendo https://iamarketing.mx/

### Estimacion de trabajo tecnico

| Seccion | Tiempo estimado |
|---|---|
| Hero completo | 45 min |
| Sistema / pilares | 30 min |
| Deliverables grid | 45 min |
| Problema reescrito | 20 min |
| Tabla comparativa | 60 min |
| CTA final | 20 min |
| Proceso con outputs | 25 min |
| Para quien + filtro negativo | 30 min |
| Autoridad | 20 min |
| FAQ + 2 nuevas | 20 min |
| Nav + footer | 15 min |
| Limpieza y QA tecnico | 30 min |
| **Total estimado** | **~6 horas** |

---

## Fase 3 — Deploy y verificacion

### Pre-deploy checklist
- [ ] Verificar responsive en 375px (iPhone SE)
- [ ] Verificar responsive en 390px (iPhone 14)
- [ ] Verificar responsive en 768px (tablet)
- [ ] Verificar responsive en 1280px (desktop)
- [ ] Verificar que GSAP carga correctamente (no CDN bloqueado)
- [ ] Verificar fallback de animaciones si GSAP no carga
- [ ] Verificar FAQ accordion funciona en mobile
- [ ] Verificar tabla comparativa en mobile (si aplica tabs)
- [ ] Verificar todos los links de WhatsApp (URL encode correcto)
- [ ] Verificar links externos con target="_blank" rel="noopener noreferrer"
- [ ] Verificar que NO hay placeholders vacios visibles ([IA SYSTEM: ...])
- [ ] Verificar velocidad en PageSpeed Insights (objetivo > 85 mobile)
- [ ] Verificar que JSON-LD schema es valido (Google Rich Results Test)
- [ ] Verificar meta tags Open Graph en opengraph.xyz

### Deploy en Vercel (comandos exactos)

```bash
# Desde la raiz del proyecto
cd /Users/salvadorvillarreal/iamarketing-site

# Verificar que index-v2.html es el correcto
# Renombrar para produccion
mv index.html index-v1-backup.html
mv index-v2.html index.html

# Deploy
vercel --prod

# Verificar URL de produccion
# Revertir si hay problema critico:
# mv index.html index-v2.html && mv index-v1-backup.html index.html && vercel --prod
```

### Post-deploy verificacion

- [ ] Abrir iamarketing.mx en incognito y verificar carga correcta
- [ ] Verificar en mobile real (no solo DevTools)
- [ ] Hacer clic en CTA de WhatsApp y confirmar que abre chat con mensaje correcto
- [ ] Verificar que Google Search Console no reporta errores de cobertura
- [ ] Verificar que sitemap.xml sigue siendo accesible

---

## Rollback plan

Si hay un problema critico en produccion despues del deploy:

```bash
mv index.html index-v2-broken.html
mv index-v1-backup.html index.html
vercel --prod
```

Tiempo estimado de rollback: 2 minutos.

---

## Dependencias y riesgos

| Riesgo | Probabilidad | Impacto | Mitigacion |
|---|---|---|---|
| Copy no validado antes del build | Alta si no se agenda sesion | Alto: doble trabajo | Hacer sesion de revision antes de tocar codigo |
| Sin testimonios reales disponibles | Media | Medio: seccion vacia o eliminada | Eliminar seccion de testimonios en v2, reemplazar con comparativa |
| Sin foto de Salvador disponible | Media | Bajo: fallback a avatar de marca | Usar social-avatar-1024-black.png como placeholder |
| Sin logotipos de clientes | Alta | Bajo: usar credenciales como proof bar alternativo | Ya contemplado en copy deck |
| Tabla comparativa compleja en mobile | Media | Medio: experiencia rota | Implementar con tabs desde el inicio, no como retoque |
| GSAP CDN lento en mobile | Baja | Bajo: fallback ya implementado | Verificar fallback funciona antes de deploy |

---

## Datos por validar antes del build

1. Deliverables exactos: cantidades y frecuencias del retainer
2. Rango de precio (o decision de no publicarlo)
3. Logotipos de clientes disponibles con permiso de uso
4. Testimonios reales disponibles: nombre, cargo, empresa, cita
5. Foto de Salvador para seccion de autoridad
6. Numero de WhatsApp principal para todos los CTAs (333 vs 477)
7. Mensaje de WhatsApp a pre-cargar en el link (validar que el URL encode es correcto)
8. Decision sobre seccion "Lo que cambia" (eliminar vs reemplazar con metricas reales)
