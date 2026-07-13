# SOP: conectar WhatsApp Business y atender todos los mensajes en un solo lugar

- Dueño: Daniel
- Última revisión: 2026-07-13
- Estado: WhatsApp pendiente de conectar; campaña piloto espera este paso

## Parte 1: conectar WhatsApp Business a la página (15 minutos, una sola vez)

1. Instala la app WhatsApp Business (gratuita) en tu teléfono si no la tienes
2. Actívala con el número que quieres usar para clientes (si tu número está en WhatsApp normal, la app te ofrece migrarlo con chats incluidos)
3. En el teléfono o en business.facebook.com entra a Meta Business Suite con tu cuenta que administra la página Daniel Cardona Finanzas
4. Ve a Configuración > Canales conectados (o WhatsApp) > Conectar cuenta de WhatsApp
5. Escribe tu número; te llega un código de 6 dígitos por WhatsApp; ingrésalo
6. Listo: la página queda vinculada, los anuncios pueden dirigir a WhatsApp y puedes poner botón de WhatsApp en la página

Después de esto: pedir al agente cambiar el destino de la campaña piloto de Messenger a WhatsApp y activarla.

## Parte 2: una sola bandeja con notificaciones (hoy, gratis)

- Instala la app Meta Business Suite en el teléfono: unifica en una sola bandeja los mensajes de Messenger, Instagram DM y comentarios de la página, con notificaciones push
- WhatsApp Business notifica por su propia app
- Con esas dos apps cubres el 100% de los mensajes entrantes con notificación inmediata

Automatización nativa gratuita en Business Suite > Bandeja > Respuestas automáticas:
- Respuesta instantánea de bienvenida
- Respuestas a preguntas frecuentes (precio, horarios, cómo trabajo)
- Mensaje de ausencia fuera de horario

En WhatsApp Business: Herramientas de empresa > Mensaje de bienvenida, respuestas rápidas (/plan, /precios) y mensaje de ausencia.

## Parte 3: bot o IA que responda (siguiente nivel)

| Opción | Qué hace | Costo aprox | Cuándo elegirla |
|---|---|---|---|
| Automatización nativa Meta | Bienvenida y FAQs fijas | Gratis | Hoy mismo, sin excusa |
| ManyChat | Flujos con palabra clave (PLAN), captura de datos, respuestas en IG/FB/WhatsApp | Desde ~15 USD/mes | Cuando la campaña genere volumen |
| WhatsApp Cloud API + n8n + Claude API | Agente IA propio que responde con tu contexto, califica leads y agenda | Variable, requiere setup | Fase 2, cuando el flujo esté validado |

## Regla de gobernanza del bot

El bot responde preguntas frecuentes, captura nombre y objetivo, y agenda o entrega el siguiente paso. El cierre de venta siempre lo hace Daniel. Toda conversación debe poder escalar a humano con notificación.

## Criterio de terminado

Cero mensajes sin responder en 24 horas, con notificación push funcionando en ambas apps.
