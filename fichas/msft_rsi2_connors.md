# FICHA · MSFT retroceso en tendencia con RSI(2)
Regla: Compro MSFT cuando en velas de 1 hora el cierre está por encima de la media móvil de 200 periodos y el RSI de 2 periodos es menor a 10. Salgo cuando el cierre supera la media móvil de 5 periodos. Stop: 2.5 % por debajo del precio de entrada. Horario: lunes a viernes durante la sesión regular de mercado (09:30 a 16:00 hora de Nueva York).
Por qué funcionaría: La tendencia de fondo de MSFT es estructuralmente alcista (+17.7 % CAGR, 56.2 % del tiempo sobre SMA 200 en el AED) y a corto plazo domina el zigzag (Kaufman 0.224): comprar caídas abruptas de sobreventa extrema (RSI de 2 < 10) a favor de la tendencia permite entrar a descuento antes de que el precio vuelva a su media. (propuesta, confírmala)

## Fase 01 · Hipótesis · CRITERIO
Agente / skill: hipotesis · escritor-hipotesis
Qué se hizo: hipótesis de compra de retrocesos en tendencia adaptada a la personalidad de MSFT.
Resultado: regla completa con activo, dirección, entrada, salida, stop y horario sin ambigüedades.
Supuestos: temporalidad 1 hora; stop de protección del 2.5 % para cubrir las colas gordas del AED.
Veredicto: APRUEBA
Siguiente paso: fase 02 para contrastar la hipótesis con el histórico del activo.

## Fase 02 · AED · CRITERIO + DATOS
Agente / skill: director · aed
Qué se hizo: medición empírica de 1.455 señales en MSFT frente a línea base y búsqueda de huella en 1.688 señales de AAPL (datos/aapl_1h_alpaca.csv).
Resultado: en MSFT, 53.5 % de acierto a 5 velas vs 52.1 % línea base (+4.1 pb); en AAPL (huella), 54.1 % de acierto a 5 velas vs 53.4 % línea base (+1.6 pb). La ventaja en tasa de acierto se repite en ambos activos.
Supuestos: datos curados de Alpaca IEX en 1 hora (2020-2026); salida rápida requerida por colas gordas.
Veredicto: APRUEBA
Siguiente paso: fase 03 para pasar la regla a pseudocódigo paso a paso.

## Fase 03 · Reglas · MOTOR
Agente / skill: reglas
Qué se hizo: descomposición de la regla en piezas, árbol de preguntas de sí o no y pseudocódigo con 4 perillas sin variables ambiguas ni datos del futuro.
Resultado: pseudocódigo paso a paso listo para ser probado en backtest.
Supuestos: ver lista debajo del pseudocódigo.
Veredicto: APRUEBA
Siguiente paso: fase 04 con el agente validador para ejecutar el backtest con costes fuera de muestra.

```
DATOS: velas de 1 hora de MSFT. Horario de Nueva York (09:30 a 16:00).
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
1. **Horario:** Lunes a viernes en sesión regular de Nueva York (09:30 a 16:00).
2. **Contexto (Filtro de tendencia):** Cierre de la vela > SMA(200).
3. **Disparador (Trigger):** RSI(2) < 10 al cierre de la vela.
4. **Dirección y entrada exacta:** Solo COMPRA; se ejecuta en la apertura de la vela inmediatamente siguiente a la confirmación de la señal.
5. **Stop y salida:**
   - Stop loss fijo en `PRECIO_ENTRADA * 0.975` (2.5 % por debajo del precio de compra).
   - Salida técnica: cierre de la vela > SMA(5).

### Árbol de decisiones (Preguntas de Sí o No):
1. ¿Tengo una posición abierta actualmente?
   - **SÍ:**
     - ¿El mínimo de la vela tocó o perforó el STOP?
       - **SÍ:** SALGO en STOP. (Fin operación).
       - **NO:** ¿El cierre de la vela es mayor a SMA(5)?
         - **SÍ:** SALGO al cierre. (Fin operación).
         - **NO:** Mantengo posición. (Fin vela).
   - **NO:**
     - ¿La vela está dentro del horario operativo (09:30 a 16:00 NY)?
       - **SÍ:** ¿El cierre de la vela es mayor a SMA(200)?
         - **SÍ:** ¿El RSI(2) al cierre es menor a 10?
           - **SÍ:** COMPRA en la apertura de la vela siguiente y fijar STOP en 2.5 %.
           - **NO:** No operar. (Fin vela).
         - **NO:** No operar (filtro de tendencia no cumplido). (Fin vela).
       - **NO:** No operar (fuera de horario). (Fin vela).

### Control de perillas (4 perillas):
1. **Perilla 1:** Periodo de media de tendencia = `200`
2. **Perilla 2:** Umbral de sobreventa de RSI = `10`
3. **Perilla 3:** Periodo de media de salida = `5`
4. **Perilla 4:** Porcentaje de stop loss = `2.5 %`

### Supuestos:
1. Operativa en velas de 1 hora cerradas para evitar fugas de información del futuro.
2. Entrada al precio de apertura de la vela siguiente a la señal.
3. El stop de 2.5 % se monitorea con el mínimo de la vela; si en la misma vela se toca el stop y el cierre supera SMA(5), manda el stop (peor escenario).
4. No hay posiciones simultáneas: máximo 1 operación abierta a la vez.
5. Solo aplica en horario regular de mercado de EE. UU. (09:30 a 16:00 hora de Nueva York).
