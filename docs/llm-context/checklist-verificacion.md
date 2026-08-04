# Checklist de verificacion

No declares el setup terminado sin pasar las 6 pruebas. Corrige y repite.

## Prueba 1: nucleo cargado

Prompt:
```
Sin buscar en ningun archivo, dime en 5 bullets quien soy, que vendo y a quien.
```

Pasa si responde correcto y sin buscar. Falla si pide contexto o inventa.
Correccion si falla: el nucleo no esta en instrucciones, o esta demasiado abajo.

## Prueba 2: retrieval activo

Prompt:
```
Que dice mi nota sobre [tema especifico que exista en el vault]?
Cita la ruta del archivo.
```

Pasa si abre el archivo correcto y cita la ruta.
Correccion si falla: revisar que INDEX.md este subido y que el pack no exceda el
limite de archivos de la plataforma.

## Prueba 3: honestidad ante ausencia

Prompt:
```
Cual fue el resultado del proyecto con [nombre de cliente inventado]?
```

Pasa si responde "sin respaldo en la fuente" y no inventa nada.
Falla si fabrica un caso. Esta es la prueba mas importante.
Correccion si falla: reforzar la seccion 12 del nucleo, subirla mas arriba.

## Prueba 4: formato

Prompt:
```
Dame un roadmap 30-60-90 para automatizar el onboarding de clientes.
```

Pasa si entrega tabla o bullets, sin emojis, sin em dash, en espanol, con
seccion de riesgos y supuestos, y cierra con siguiente accion.
Correccion si falla: las reglas de salida quedaron muy abajo en el nucleo.

## Prueba 5: continuidad entre sesiones

Abre una conversacion nueva dentro del mismo Project al dia siguiente.

Prompt:
```
Retoma donde quedamos con [tema trabajado ayer].
```

Pasa si ubica el tema via archivos o memoria del Project.
Nota: la continuidad conversacional real solo existe si guardas los resumenes de
sesion de vuelta al vault. Ver "Loop de escritura" abajo.

## Prueba 6: paridad entre LLMs

Corre la Prueba 1 y la Prueba 3 en ChatGPT y en Claude.

Pasa si ambas respuestas son consistentes en hechos.
Correccion si falla: el nucleo o el pack estan desincronizados entre plataformas.

---

## Loop de escritura, para continuidad real

El contexto de "lo que voy platicando" no se sincroniza solo. Ningun LLM escribe
en tu vault sin que tu cierres el ciclo.

SOP de cierre de sesion, 3 minutos:

1. Al terminar una conversacion util, pide:
```
Genera una nota de cierre en markdown con este formato:
- titulo
- fecha
- contexto en 3 bullets
- decisiones tomadas
- pendientes con owner
- siguiente accion
Sin preambulo, solo el markdown.
```
2. Pega la salida en Obsidian en `40-Sesiones/AAAA-MM-DD-tema.md`
3. Si usas Obsidian Git, el commit y push son automaticos
4. Recompila el pack semanal

Automatizacion opcional, pendiente por validar: n8n con webhook que reciba la
nota y la escriba al repo del vault via GitHub API. Elimina el paso 2 manual.

---

## Tabla de diagnostico rapido

| Sintoma | Causa probable | Fix |
|---|---|---|
| Responde generico siempre | Nucleo no cargado | Pegar EVIA-CORE en instrucciones del Project |
| Sabe quien eres pero no los proyectos | Falta capa L2 o L3 | Subir pack, conectar repo |
| A veces si y a veces no | Retrieval opcional | Reforzar protocolo obligatorio de seccion 12 |
| Inventa clientes o cifras | Falta regla de honestidad | Prueba 3, reforzar nucleo |
| Contexto viejo | Pack desactualizado | Recompilar y resubir |
| Pierde el hilo entre dias | No hay loop de escritura | SOP de cierre de sesion |
