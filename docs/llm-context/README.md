# Contexto multi-LLM desde Obsidian / BUNKER

Sistema para que cualquier LLM (ChatGPT, Claude, Gemini, NotebookLM, Perplexity)
opere con el mismo contexto operativo de Estrategias Vitales IA, sin pegar texto
manualmente en cada conversacion.

## Problema que resuelve

Un enlace a una carpeta local o a Google Drive privado no da acceso real al
modelo. Y aunque conectes un connector, el resultado es *retrieval*: el modelo
busca fragmentos solo cuando decide buscar. Si no busca, responde sin contexto.

Claude Code no tiene ese problema porque `CLAUDE.md` se inyecta en cada sesion.
Ese es el patron a replicar.

## Arquitectura de 3 capas

| Capa | Archivo | Funcion | Se carga |
|---|---|---|---|
| L1 Nucleo | `EVIA-CORE.md` | Identidad, negocio, stack, reglas | Siempre, en instrucciones |
| L2 Pack | `pack/*.md` | Base consultable comprimida | Como archivos del Project |
| L3 Vault | Repo Git o Drive del vault | Busqueda profunda bajo demanda | Via connector |

Regla: **L1 es obligatorio**. L2 y L3 son opcionales y aditivos.

## Archivos de esta carpeta

- `SOP-contexto-multi-llm.md` - procedimiento completo paso a paso
- `CONTEXT-PACK.template.md` - plantilla del nucleo `EVIA-CORE.md`
- `compile-context.sh` - compila el vault de Obsidian en pack + indice
- `instrucciones-chatgpt.md` - texto listo para pegar en ChatGPT Project o Custom GPT
- `checklist-verificacion.md` - como comprobar que el contexto realmente carga

## Quick start

```bash
chmod +x docs/llm-context/compile-context.sh
docs/llm-context/compile-context.sh ~/Obsidian/EVIA-Brain ~/Desktop/evia-context
```

Salida en `~/Desktop/evia-context/`:
- `EVIA-CORE.md` borrador del nucleo, editar a mano
- `INDEX.md` mapa completo del vault
- `pack/parte-01.md` ... archivos troceados listos para subir

## Mantenimiento

| Frecuencia | Accion |
|---|---|
| Semanal | Recompilar pack y resubir a los Projects |
| Mensual | Revisar y podar `EVIA-CORE.md`, no debe crecer sin limite |
| Al cambiar oferta o pricing | Actualizar nucleo el mismo dia |

## Limites conocidos

- Los connectors disponibles cambian por plan y por proveedor. Verificar en la
  cuenta antes de asumir disponibilidad.
- MCP remoto requiere endpoint HTTPS publico. Un servidor MCP local no sirve
  para ChatGPT web ni para apps moviles.
- Ningun connector garantiza que el modelo consulte la fuente en cada turno.
  Por eso existe la capa L1.
