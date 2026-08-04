# Configurar contexto en Claude chat

Documento especifico para claude.ai web, movil y el chat de Claude Desktop.
Para ChatGPT ver `instrucciones-chatgpt.md`.

## El error de capas mas comun

`CLAUDE.md` **no** lo lee el chat de Claude. Lo lee Claude Code.
Son superficies distintas del mismo modelo, con configuracion independiente y
sin herencia entre ellas.

| Superficie | Lee CLAUDE.md | Lee MCP local | Donde se configura |
|---|---|---|---|
| Claude Code CLI | Si | Si | `~/.claude/CLAUDE.md` y CLAUDE.md de proyecto |
| Claude Code en Desktop, Web, IDE | Si | Segun entorno | Igual que arriba |
| Chat de Claude Desktop | No | Si, via config MCP del app | Settings del app y Projects |
| Chat de claude.ai web y movil | No | No | Preferencias de perfil, Projects, Connectors |

Consecuencia practica: tener un `CLAUDE.md` impecable no hace que claude.ai en el
celular sepa quien eres. Hay que configurarlo aparte.

Un servidor MCP local, por ejemplo el de Obsidian, solo es alcanzable desde
aplicaciones que corren en la misma maquina. claude.ai en el navegador o en el
telefono no puede verlo. Para esos casos se requiere un connector remoto con
endpoint HTTPS publico, o espejar el vault a GitHub o Google Drive.

---

## Nivel 1: preferencias personales

Aplica a todos los chats, en todos los dispositivos. Es el equivalente mas
cercano a un `CLAUDE.md` global para el chat.

Ubicacion: Settings, seccion de perfil o preferencias personales.

Limitacion: el campo es corto por diseno. No metas proyectos ni clientes ahi.
Solo identidad estable y reglas de salida.

Texto sugerido:

```
Soy Salvador "Salva" Villarreal, fundador de Estrategias Vitales IA.
Consultor certificado en IA para negocios y Fractional CAIO para empresas B2B
y MiPyMEs en Mexico y LatAm. Web: iaconsultoresvitales.mx

Lineas de servicio: consultoria e implementacion de IA, Fractional CAIO con
retainer mensual, Taller Express IA Estrategica de 6h, Bootcamp Ejecutivo de
20h, diseno de agentes y automatizaciones con n8n, GoHighLevel y Make.com,
voice AI agents con ElevenLabs Convai.

Stack habitual: ChatGPT, Claude, custom GPTs, Obsidian, Vercel, Google
Workspace, Shopify, GA4, Meta, Gamma, Skool, n8n, GoHighLevel, ElevenLabs,
NotebookLM.

Como quiero que respondas:
- Espanol primero. Terminos en ingles cuando sean mas precisos: workflow,
  agent, prompt, funnel, deployment, stack, roadmap, source of truth.
- Estructurada, accionable y concisa. Bullets, tablas, checklists, SOPs, JSON,
  plantillas, prompts listos para usar, roadmaps 30-60-90.
- Sin emojis. Sin el caracter em dash.
- Nivel avanzado. No expliques conceptos obvios.
- Distingue explicitamente entre hecho confirmado, recomendacion, inferencia y
  pendiente por validar.
- Nunca inventes cifras, nombres de cliente, fechas ni resultados. Si no lo
  tienes, marcalo como pendiente por validar.
- Ante falta de claridad, avanza con supuestos razonables y marcalos. Entrega
  primero una version usable. Pide confirmacion solo antes de acciones con
  riesgo.
- Cierra con una linea "Siguiente accion:" y un paso concreto.
- Prioriza entregables reutilizables con cliente sobre explicaciones.
```

---

## Nivel 2: Project EVIA Brain

Ubicacion: seccion Projects en claude.ai.

1. Crear Project `EVIA Brain`
2. Custom instructions del Project: pegar `EVIA-CORE.md` completo, precedido por
   el protocolo de citado que esta abajo
3. Project knowledge: subir `INDEX.md` y todos los `pack/parte-NN.md`
4. Trabajar siempre dentro del Project para temas de negocio

Protocolo a pegar antes del nucleo:

```
Operas con la base de conocimiento de este Project, que es un espejo del vault
de Obsidian EVIA-Brain.

PROTOCOLO DE CONTEXTO, obligatorio en cada turno:

1. Clasifica la pregunta:
   A) Requiere contexto propietario: proyectos, clientes, pricing real,
      decisiones previas, contenido publicado, configuraciones existentes.
   B) No lo requiere: conocimiento general, redaccion, calculo, codigo generico.

2. Si es tipo A, consulta primero el Project knowledge. Empieza por INDEX.md
   para ubicar la nota, luego abre el archivo del pack que la contiene.

3. Cita la fuente al final con el formato: Fuente: <ruta/de/la/nota.md>

4. Si no hay resultado relevante, escribe literalmente "sin respaldo en la
   fuente" antes de continuar y marca la respuesta como inferencia general.

5. Nunca inventes cifras, clientes, fechas, resultados ni decisiones previas.

A continuacion, el contexto operativo estable:
```

---

## Nivel 3: connectors

Ubicacion: Settings, seccion de connectors.

Opciones segun plan, verificar disponibilidad en la cuenta:

| Connector | Uso | Requisito |
|---|---|---|
| GitHub | Vault espejado como repo privado. Recomendado. | Repo privado con el vault |
| Google Drive | Vault o carpeta BUNKER en Drive | Sync de Drive activo |
| Connector remoto MCP | Acceso directo a un servidor propio | Endpoint HTTPS publico |

Para el chat de Claude Desktop se pueden agregar servidores MCP locales desde la
configuracion del app, incluido un MCP de filesystem apuntando al vault. Eso
resuelve el escritorio pero no el movil.

Recomendacion: GitHub. Funciona igual en web, movil y desktop, versiona el vault
y sirve tambien para ChatGPT sin trabajo adicional.

Setup del espejo en `SOP-contexto-multi-llm.md`, Fase 4.

---

## Como forzar contexto en un chat suelto

Si estas fuera del Project, por ejemplo desde el celular, arranca el hilo asi:

```
Antes de responder nada:
1. Busca en el connector de GitHub, repo evia-brain, el archivo INDEX.md
2. Lista las 5 notas mas relevantes para: [TEMA]
3. Abre esas notas y resume el estado actual en 5 bullets
4. Marca que informacion falta

No opines sobre el tema todavia.
```

Esto convierte retrieval opcional en retrieval forzado, que es la causa raiz de
que el chat responda sin contexto de forma intermitente.

---

## Verificacion

Corre las 6 pruebas de `checklist-verificacion.md` dentro de claude.ai.
La Prueba 3, preguntar por un cliente inventado, es la mas importante.

## Pendiente por validar

- Plan actual de claude.ai y que connectors habilita
- Si el chat de Claude Desktop ya tiene el MCP de Obsidian o solo Claude Code
- Tamano del vault para decidir cuantos archivos del pack caben en el Project
