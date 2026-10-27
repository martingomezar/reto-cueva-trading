# FICHA · NAS100 retroceso en tendencia con RSI(2)
Regla: Compro NAS100 cuando en velas de 1 hora el cierre está por encima de la media móvil de 200 periodos y el RSI de 2 periodos es menor a 10. Salgo cuando el cierre supera la media móvil de 5 periodos. Stop: 2.5 % por debajo del precio de entrada. Horario: lunes a viernes durante la sesión regular de mercado (09:30 a 16:00 hora de Nueva York).
Por qué funcionaría: La tendencia de fondo de NAS100 es alcista (58.5 % del tiempo sobre SMA 200 en el AED) y a corto plazo domina el zigzag (Kaufman 0.237): comprar caídas abruptas transitorias (sobreventa extrema en RSI de 2) dentro de una tendencia alcista estructural explota la sobrerreacción de corto plazo antes del rebote hacia la media. (propuesta, confírmala)

## Fase 01 · Hipótesis · CRITERIO
Agente / skill: hipotesis · escritor-hipotesis
Qué se hizo: regla y porqué estructurados a partir del AED de Connors adaptado a NAS100.
Resultado: hipótesis completa con activo, dirección, entrada, salida, stop y horario definidos.
Supuestos: temporalidad 1 hora; stop de protección del 2.5 % para mitigar el riesgo de colas gordas.
Veredicto: APRUEBA
Siguiente paso: fase 02 para contrastar la ventaja en datos históricos.

## Fase 02 · AED · CRITERIO + DATOS
Agente / skill: director · aed
Qué se hizo: análisis exploratorio de datos plasmado en activos/nas100.md (Mega Cueva Tester).
Resultado: tendencia alcista (+15.0 % CAGR), colas gordas (curtosis 74.93) y predominio de zigzag (Kaufman 0.237); comprar retrocesos es la familia adecuada.
Supuestos: datos representativos de 5.2 años en 15m/1h.
Veredicto: APRUEBA
Siguiente paso: fase 03 para pasar la regla a pseudocódigo sin ambigüedades.

## Fase 03 · Reglas · MOTOR
Agente / skill: reglas
Qué se hizo: regla descompuesta en piezas (horario, contexto, disparador, stop y salida), árbol de decisiones de sí o no y pseudocódigo paso a paso con 4 perillas.
Resultado: pseudocódigo sin ambigüedad lógica ni variables sin número; no usa datos del futuro.
Supuestos: ver lista debajo del pseudocódigo.
Veredicto: APRUEBA
Siguiente paso: fase 04 con el agente validador para realizar el backtest con costes fuera de muestra.

```
DATOS: velas de 1 hora de NAS100. Horario de Nueva York (09:30 a 16:00).
       Indicadores calculados con precios de cierre de velas ya cerradas:
       SMA200 = media móvil simple de 200 velas.
       SMA5 = media móvil simple de 5 velas.
       RSI2 = índice de fuerza relativa de 2 velas.

CADA VELA DE 1 HORA CERRADA (en horario de sesión):
  1. SI estoy fuera:
       a. SI el cierre de la vela > SMA200
          Y el RSI2 < 10:
            COMPRA en la apertura de la vela siguiente.
            PRECIO_ENTRADA = precio de apertura de esa vela siguiente.
            STOP = PRECIO_ENTRADA * (1 - 0.025).
            Ve al paso 2.
       b. SI NO:
            No hago nada en esta vela. FIN de la vela.

  2. MIENTRAS esté dentro, en cada vela nueva, en este orden:
       a. SI el mínimo de la vela <= STOP:
            SALGO en STOP.
            FIN de la operación.
       b. SI NO, SI el cierre de la vela > SMA5:
            SALGO al cierre de esa vela.
            FIN de la operación.
       c. SI NO:
            Mantengo la posición. FIN de la vela.

  3. Máximo 1 operación abierta a la vez.
```

### Piezas de la regla:
1. **Horario:** Lunes a viernes en sesión de mercado de Nueva York (09:30 a 16:00 EST/EDT).
2. **Contexto (Filtro de régimen):** Cierre de la vela > SMA(200) (filtro de viento a favor alcista).
3. **Disparador (Trigger):** RSI(2) < 10 al cierre de la vela (sobreventa extrema en zigzag).
4. **Dirección y entrada exacta:** Solo COMPRA; se ejecuta en la apertura de la vela inmediatamente siguiente a la confirmación de la señal.
5. **Stop y salida:**
   - Stop loss de protección en `PRECIO_ENTRADA * 0.975` (2.5 % de caída fija).
   - Salida técnica por toma de beneficio o normalización: cuando el cierre de la vela > SMA(5).

### Árbol de decisiones (Preguntas de Sí / No):
1. ¿Tengo una posición abierta actualmente?
   - **SÍ:** Ir a chequeo de salida y stop.
     - ¿El mínimo de la vela actual tocó o perforó el STOP?
       - **SÍ:** SALGO en STOP. (Fin operación).
       - **NO:** ¿El cierre de la vela es mayor a SMA(5)?
         - **SÍ:** SALGO al cierre. (Fin operación).
         - **NO:** Mantengo posición. (Fin vela).
   - **NO:** Ir a chequeo de entrada.
     - ¿La vela está dentro del horario operativo (09:30 a 16:00 NY)?
       - **SÍ:** ¿El cierre de la vela es mayor a SMA(200)?
         - **SÍ:** ¿El RSI(2) de la vela cerrada es menor a 10?
           - **SÍ:** COMPRA en la apertura de la siguiente vela y fijar STOP en 2.5 %.
           - **NO:** No operar. (Fin vela).
         - **NO:** No operar (filtro de tendencia no se cumple). (Fin vela).
       - **NO:** No operar (fuera de horario). (Fin vela).

### Control de perillas (máximo 4 parámetros):
1. **Perilla 1:** Periodo de media de tendencia = `200`
2. **Perilla 2:** Umbral de sobreventa de RSI = `10` (con longitud fija clásica de 2 velas)
3. **Perilla 3:** Periodo de media de salida rápida = `5`
4. **Perilla 4:** Porcentaje de stop de protección = `2.5 %`

### Supuestos:
1. Se opera en velas de 1 hora cerradas; los indicadores (SMA200, SMA5, RSI2) se leen al cierre para no usar datos del futuro.
2. La compra se ejecuta en la apertura de la vela siguiente a la señal.
3. El stop de 2.5 % se verifica intrabarra (con el precio mínimo de la vela). Si en la misma vela se toca el stop y el cierre supera la SMA(5), manda el stop (peor escenario).
4. No hay reentradas simultáneas: máximo una posición activa a la vez.
5. El horario contempla exclusivamente velas dentro de la jornada regular (09:30 a 16:00 hora de Nueva York).
