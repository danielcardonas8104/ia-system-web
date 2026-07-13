# Estructura de Google Drive: capa de distribución y colaboración

Drive NO es el cerebro. Es la capa donde publicas y compartes con colegas, agentes, promotores y clientes lo que tú autorices. El source of truth de conocimiento sigue siendo el vault; lo que vive en Drive compartido es la versión publicada.

## Estructura de carpetas recomendada

```
Mi unidad (o Unidad compartida si tienes Workspace)
└── IA-SYSTEM/
    ├── 00-PUBLICO/                Cualquiera con el link puede ver
    │   ├── Brochures y one-pagers
    │   ├── Media kit (logos, fotos aprobadas)
    │   └── Material de promotores (scripts, presentaciones)
    ├── 10-COLABORADORES/          Solo cuentas invitadas, permiso comentar o editar
    │   ├── Entregas/              Aquí SUBEN ellos (editor solo en esta carpeta)
    │   ├── Recursos/              Aquí LEEN ellos (solo lector)
    │   └── Plantillas/            Formatos que deben usar
    ├── 20-CLIENTES/
    │   └── [Cliente X]/           Una carpeta por cliente, compartida solo con ese cliente
    │       ├── Propuestas/
    │       ├── Entregables/
    │       └── Sesiones/
    ├── 30-MEDIA/                  Videos, fotos, audio pesado (privado, se linkea desde el vault)
    └── 90-ARCHIVO/                Todo lo muerto, sin compartir
```

## Reglas de gobernanza

1. El permiso se asigna a la CARPETA, nunca archivo por archivo; un archivo hereda el permiso de donde vive
2. Tres niveles y nada más: Lector (promotores, prospectos), Comentarista (revisión), Editor (solo en carpetas de entrega)
3. Nadie externo tiene editor en 00-PUBLICO ni en Recursos: lo compartido para leer es de solo lectura
4. Lo que va a 00-PUBLICO se considera publicado en internet: nada de pricing interno, estrategias ni datos de clientes
5. Todo documento publicado en Drive tiene su fuente en el vault; si se actualiza la fuente, se re-exporta, nunca se edita solo en Drive
6. Nomenclatura: AAAA-MM-DD-nombre-descriptivo (permite ordenar y saber vigencia)
7. Revisión trimestral de "Compartido con": revocar accesos de colaboraciones terminadas

## Cómo lo usan los LLMs y agentes

- Claude con el conector de Google Drive puede buscar, leer y crear archivos en tu Drive bajo tu cuenta
- Para que un agente guarde entregas: siempre en la carpeta de Entregas correspondiente, nunca en la raíz
- Para dar contexto de un documento de Drive a cualquier LLM sin conector: pegar el link con permiso de lector o exportar a markdown/PDF

## Matriz rápida de decisión

| Quién necesita el archivo | Carpeta | Permiso |
|---|---|---|
| Cualquiera (marketing, promotores masivos) | 00-PUBLICO | Lector con link |
| Colaborador que entrega trabajo | 10-COLABORADORES/Entregas | Editor |
| Colaborador que consume material | 10-COLABORADORES/Recursos | Lector |
| Cliente activo | 20-CLIENTES/[Cliente] | Lector o comentarista |
| Solo yo y mis agentes | 30-MEDIA o vault | Sin compartir |
