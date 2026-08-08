# Operar Claude Code desde el celular

Pixel 10 Pro, o cualquier telefono. Sin depender de que la MacBook este
encendida.

## Como funciona

Claude Code en la web corre en un contenedor en la nube. El repositorio se
clona ahi al iniciar la sesion. Tu escritorio no participa. Puede estar
apagado, sin bateria o en otro pais.

Consecuencia: todo lo que se haga en una sesion web vive en ese contenedor
hasta que se commitea y pushea. El contenedor se recicla tras un periodo de
inactividad. Lo no commiteado se pierde.

Regla operativa: commit y push al cerrar cada bloque, no al final del dia.

## Setup en el Pixel, una sola vez

1. Chrome, abrir `claude.ai/code`
2. Menu de Chrome, "Agregar a pantalla de inicio"
3. Queda como app, sin barra de direcciones
4. Verificar que aparezcan las sesiones existentes

Alternativa: la app de Claude en Android. Verificar en tu version si expone
las sesiones de Code o solo el chat.

## Continuidad de contexto

Tres capas, en orden de fuerza:

| Capa | Alcance | Como se activa |
|---|---|---|
| Retomar la sesion | Conversacion completa, con todo el hilo | Tocar la sesion en la lista |
| `CLAUDE.md` | Perfil, stack, reglas de trabajo | Automatico en toda sesion nueva |
| `ESTADO.md` | Donde quedamos, pendientes, decisiones | Pedirlo al abrir sesion nueva |

Retomar la sesion es siempre mejor que abrir una nueva. Solo abre una nueva
cuando el tema cambie por completo.

## Arranque de sesion nueva

Primer mensaje:

```
Lee ESTADO.md y dime en 5 bullets donde quedamos, que esta pendiente y cual
es la siguiente accion. No hagas nada mas todavia.
```

## Cierre de sesion

Ultimo mensaje, antes de guardar el telefono:

```
Actualiza ESTADO.md con lo que hicimos, los pendientes nuevos y la siguiente
accion. Commit y push.
```

Tres segundos de escribir, y la siguiente sesion arranca con contexto real.

## Limitaciones desde movil

| Limitacion | Impacto | Mitigacion |
|---|---|---|
| Teclado chico para prompts largos | Fricción | Dictado por voz de Gboard |
| No puedes ver el sitio en local | No hay preview inmediato | Deploy preview de Vercel y abrir la URL |
| Revisar diffs largos es incomodo | Revision superficial | Pedir resumen del diff antes del commit |
| Sesion reciclada por inactividad | Trabajo no commiteado se pierde | Commit por bloque |

## Que si conviene hacer desde el celular

- Retomar y cerrar pendientes acotados
- Revisar y aprobar cambios
- Redactar contenido, propuestas y copy
- Actualizar `ESTADO.md` y documentacion
- Lanzar deploys y revisar el preview
- Responder a fallas de CI

## Que conviene dejar para la Mac

- Refactors grandes con muchos archivos
- Revision visual fina de responsive
- Cualquier cosa que requiera correr el vault de Obsidian local
