# Análisis de protección familiar Cardona Gosserez

Fecha de corte: 2026-07-28
Fuente: Portal de Agentes Prudential, ruta Consultas > Pólizas, pestaña Coberturas de la carátula
Clave de agente: C16991
Alcance: 6 pólizas, 21 coberturas, todas EN VIGOR y con pago de primas en curso

## 1. Regla de lectura

Las sumas aseguradas no se suman entre sí de forma plana. Cada cobertura paga bajo un supuesto distinto:

| Tipo | Cuándo paga | Cómo se acumula |
|---|---|---|
| BASICA | Fallecimiento por cualquier causa | Es la protección de piso real |
| ACCIDENTAL (muerte accidental o pérdidas orgánicas) | Solo si el fallecimiento es accidental | Se suma a la básica, únicamente en ese supuesto |
| INVALIDEZ TOTAL Y PERMANENTE | Invalidez dictaminada | Beneficio independiente, no se suma al fallecimiento |
| SALUD (cirugías, enfermedades graves) | Evento médico cubierto | Beneficio independiente |
| EXCESO | Componente de aportación adicional en Universal Life | 0.00 en ambas pólizas, sin capa adicional |

El error de lectura más común es sumar todo y reportar una cifra inflada. Las cifras que importan son dos: fallecimiento por cualquier causa y fallecimiento accidental.

## 2. Protección por persona

### Fallecimiento por cualquier causa (solo cobertura básica)

| Persona | UDIS | USD |
|---|---|---|
| Daniel Cardona Sánchez | 435,000 | 113,300 |
| Martha Leticia Gosserez Rojas | 250,000 | 0 |
| Aldo Cardona Gosserez | 60,000 | 0 |
| **Total familia** | **745,000** | **113,300** |

### Fallecimiento accidental (básica más muerte accidental)

| Persona | UDIS | USD |
|---|---|---|
| Daniel Cardona Sánchez | 1,010,000 | 226,600 |
| Martha Leticia Gosserez Rojas | 500,000 | 0 |
| Aldo Cardona Gosserez | 430,000 | 0 |
| **Total familia** | **1,940,000** | **226,600** |

### Invalidez total y permanente

| Persona | UDIS | USD |
|---|---|---|
| Daniel Cardona Sánchez | 575,000 | 113,300 |
| Martha Leticia Gosserez Rojas | 250,000 | 0 |
| Aldo Cardona Gosserez | 0 | 0 |

### Coberturas de salud

| Persona | Cobertura | Suma asegurada |
|---|---|---|
| Daniel Cardona Sánchez | Cirugías Bronce (89793) | 40,000 UDIS |
| Martha Leticia Gosserez Rojas | Enfermedades Graves Plus (92834) | 27,500 UDIS |
| Aldo Cardona Gosserez | ninguna | 0 |

## 3. Detalle por póliza

| Póliza | Asegurado | Producto | Básica | Invalidez | Accidental | Salud |
|---|---|---|---|---|---|---|
| 89793 | Daniel | Bienestar 20 años (UDIS) | 150,000 | 150,000 | 150,000 | 40,000 |
| 102239 | Daniel | Personaliza Pru 20 años (UDIS) | 60,000 | 200,000 | 200,000 | 0 |
| 102261 | Daniel | Garantía Prudential 20 años (UDIS) | 225,000 | 225,000 | 225,000 | 0 |
| 102264 | Daniel | Bienestar 5 años (USD) | 113,300 | 113,300 | 113,300 | 0 |
| 92834 | Martha | Bienestar 10 años (UDIS) | 250,000 | 250,000 | 250,000 | 27,500 |
| 100631 | Aldo | Personaliza Pru 20 años (UDIS) | 60,000 | **0** | 370,000 | 0 |

## 4. Hallazgos

### 4.1 Aldo no tiene cobertura de invalidez

La póliza 100631 es el mismo producto que la 102239 de Daniel, Personaliza Pru 20 años en UDIS, con la misma suma básica de 60,000 UDIS. La 102239 incluye Invalidez Total y Permanente por 200,000 UDIS. La 100631 no incluye esa cobertura.

Es el único asegurado de los tres sin protección por invalidez. Pendiente por validar si fue exclusión por suscripción, decisión al contratar, o una omisión en la solicitud.

### 4.2 La protección real es mucho menor que la aparente

La suma de todas las coberturas de fallecimiento da 1,940,000 UDIS más 226,600 USD. Pero eso solo aplica si la muerte es accidental. Ante la causa estadísticamente más probable, enfermedad, la familia recibe 745,000 UDIS más 113,300 USD, es decir el 38 por ciento de la cifra bruta.

El portafolio está sobreponderado hacia muerte accidental. Es la cobertura más barata por peso de suma asegurada y la menos probable de detonar.

### 4.3 Aldo depende casi por completo de la cobertura accidental

Su básica es de 60,000 UDIS contra 370,000 UDIS de muerte accidental, una razón de 6.2 a 1. Es el desbalance más extremo de las seis pólizas.

### 4.4 Los riders no siguen una proporción consistente

| Póliza | Básica | Rider accidental | Razón |
|---|---|---|---|
| 89793 | 150,000 | 150,000 | 1.0 |
| 102261 | 225,000 | 225,000 | 1.0 |
| 102264 | 113,300 | 113,300 | 1.0 |
| 92834 | 250,000 | 250,000 | 1.0 |
| 102239 | 60,000 | 200,000 | 3.3 |
| 100631 | 60,000 | 370,000 | 6.2 |

Los cuatro productos tradicionales mantienen paridad exacta. Las dos pólizas Universal Life, Personaliza Pru, tienen riders contratados de forma independiente a la básica. Pendiente por validar contra la carátula si en Universal Life el beneficio por fallecimiento incluye además el valor del fondo, en cuyo caso la básica de 60,000 UDIS subestima la protección efectiva de esas dos pólizas.

### 4.5 La póliza en dólares tiene un costo por unidad de protección muy favorable, y un plazo por aclarar

Datos confirmados en carátula de la 102264:

| Campo | Valor |
|---|---|
| Solicitud | SE0000111188 |
| Emisión | 30/10/2025 |
| Prima anual | 821.76 USD |
| Prima por periodo | 821.76 USD, frecuencia anual |
| Primas en depósito | 0.00 USD |
| Medio de cobro | Débito |
| Asegurado | Daniel Cardona Sánchez, ID 87727 |
| Fecha de nacimiento | 16/04/1981 |
| Edad de emisión | 44 |

Costo por unidad de protección: 821.76 USD anuales para 113,300 USD de suma asegurada equivale a **7.25 USD por cada 1,000 USD de cobertura**. Es la relación más eficiente identificada hasta ahora en el portafolio familiar.

Si el "5 años" del producto es periodo de pago de primas y no vigencia, el desembolso total sería de 4,108.80 USD, unos 71,957 MXN, por una protección de 1,984,223 MXN. Relación de 27.6 a 1.

**Pendiente crítico por validar.** Hay dos lecturas posibles de "BIENESTAR PRUDENTIAL 5 AÑOS":

1. Pago limitado a 5 años con cobertura vitalicia o de largo plazo. Escenario favorable.
2. Vigencia de 5 años. En ese caso la cobertura termina el 30/10/2030 y Daniel pierde 1,984,223 MXN, el 34 por ciento de su protección, a los 49 años.

La diferencia entre ambas lecturas es material para la planeación. Se resuelve leyendo la carátula o las condiciones generales del producto.

### 4.6 Exceso en cero en ambas Universal Life

Tanto 102239 como 100631 muestran EXCESO en 0.00. No hay aportación adicional por encima de la prima base, por lo que no hay capa de suma asegurada extra ni acumulación acelerada de valor de rescate por esa vía.

## 5. Conversión a pesos

Valores usados:
- UDI: 8.830830 MXN, valor vigente a julio 2026
- USD: 17.5130 MXN, tipo de cambio FIX publicado en el DOF para el 24 de julio de 2026

Ambos deben reconfirmarse contra Banxico antes de usar estas cifras con un cliente. La UDI se actualiza a diario y el FIX cada día hábil.

### Total consolidado por persona

| Persona | Cualquier causa (MXN) | Accidental (MXN) |
|---|---|---|
| Daniel Cardona Sánchez | 5,825,634 | 12,887,584 |
| Martha Leticia Gosserez Rojas | 2,207,708 | 4,415,415 |
| Aldo Cardona Gosserez | 529,850 | 3,797,257 |
| **Total familia** | **8,563,191** | **21,100,256** |

### Desglose de Daniel por póliza, fallecimiento por cualquier causa

| Póliza | Moneda | Suma asegurada | MXN | Peso relativo |
|---|---|---|---|---|
| 102261 Garantía Prudential | UDIS | 225,000 | 1,986,937 | 34.1 % |
| 102264 Bienestar 5 años | USD | 113,300 | 1,984,223 | 34.1 % |
| 89793 Bienestar 20 años | UDIS | 150,000 | 1,324,625 | 22.7 % |
| 102239 Personaliza Pru | UDIS | 60,000 | 529,850 | 9.1 % |
| **Total** | | | **5,825,634** | **100 %** |

La póliza en dólares aporta poco más de un tercio de la protección de Daniel, prácticamente empatada con la 102261. Es además la única cobertura del portafolio familiar que no está expuesta al peso.

### Invalidez, total consolidado

| Persona | MXN |
|---|---|
| Daniel Cardona Sánchez | 7,061,950 |
| Martha Leticia Gosserez Rojas | 2,207,708 |
| Aldo Cardona Gosserez | 0 |

Fórmula para recalcular:

```
MXN = (suma_UDIS x valor_UDI) + (suma_USD x tipo_cambio_FIX)
```

## 6. Pendientes por validar

1. Si el "5 años" de la póliza 102264 es periodo de pago o vigencia. Determina si Daniel conserva o pierde el 34 por ciento de su protección en octubre de 2030.
2. Ausencia de cobertura de invalidez en la póliza 100631 de Aldo.
3. Si el beneficio por fallecimiento en Personaliza Pru incluye el valor del fondo además de la suma básica.
4. Reconfirmar UDI y tipo de cambio FIX contra Banxico el día que se use el análisis.
5. Suma asegurada de la póliza de auto Banorte 2314473 de Martha, no digitalizada.
6. Estatus individual de las coberturas de invalidez y accidental, que el portal no muestra en pantalla.

## 7. Método de extracción

Ruta usada: Consultas > Pólizas, pestaña Coberturas de la carátula. Solo lectura.

Nota operativa importante: la ruta Gestión de Póliza abre un flujo de endoso al entrar al detalle, con la secuencia "¿Quién formaliza la solicitud?" seguida de "Categorías de Endoso", que sí permite modificaciones. Para consulta de datos usar siempre Consultas > Pólizas.

Limitación observada: la tabla de coberturas no tiene columna de moneda por cobertura. La moneda se muestra a nivel póliza y coincide con el sufijo del nombre del producto. Se reportó la moneda de póliza para todas sus coberturas, sin conversiones.
