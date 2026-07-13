# SOP: publicación en redes vía Claude + Metricool

- Dueño: Daniel
- Frecuencia: según calendario de contenido
- Última revisión: 2026-07-13
- Herramientas: Claude (conector Metricool), Google Drive (assets), este vault (calendario)

## Objetivo

Publicar o programar contenido en Instagram, Threads, TikTok, Facebook y YouTube sin abrir cada red, con aprobación humana antes de programar.

## Prerrequisitos

- Metricool conectado en Claude (verificado 2026-07-13, marca coach_financiero_)
- Asset final (video/imagen) subido a Drive o ya en Metricool
- Idea o brief del post

## Pasos

1. Pedir a Claude: "Lee mi calendario de contenido y redacta el copy del post de [tema] para [redes]"
2. Revisar y ajustar el copy propuesto
3. Pedir: "Consulta en Metricool el mejor horario para publicar en [red] y proponme fecha y hora"
4. Aprobar explícitamente: "Aprobado, prográmalo"
5. Claude programa vía Metricool (createScheduledPost)
6. Verificar en el planner de Metricool que quedó programado
7. Registrar en el calendario de contenido del vault: tema, red, fecha, estado

## Criterio de terminado

Post visible en el planner de Metricool con fecha, hora, copy y asset correctos, y registrado en el calendario del vault.

## Errores comunes

- Programar sin revisar el copy: siempre aprobar antes del paso 5
- Asset en formato incorrecto por red (vertical vs horizontal): validar specs antes
- No registrar en el vault: se pierde la trazabilidad de qué se publicó y por qué
