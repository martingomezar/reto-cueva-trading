# MI PLAN DE TRADER · 2026-10-28

## Lo que quiero conseguir
«Estrategias rentables en los próximos 3 meses».
Operar principalmente acciones argentinas, CEDEARs, acciones de EE. UU. o cripto con capital propio.

## Mis límites (el Director los usa en todas mis fichas)
- Capital aproximado: 5.000; perderlo sería una pérdida, pero no cambiaría mi vida.
- Riesgo por operación: máximo declarado de 5 % de la cuenta (250 con el capital aproximado). El riesgo real depende del stop.
- Límite de pérdida diaria: 5 %; si lo alcanzo, paro. Una sola operación con el riesgo máximo declarado podría alcanzar este límite.
- Caída máxima de la cuenta: 15 % desde el máximo → si la toco, apago y reviso.
- Caída máxima que acepto en un backtest: 7,5 % (la mitad de mi caída máxima de cuenta).
- Tiempo: disponible con alertas · Horario: flexible · zona horaria: Buenos Aires (UTC−3); prefiero no operar de noche.
- Frecuencia: puedo operar a diario; revisaré una estrategia después de reunir 64 operaciones de esa misma estrategia, sin acelerar ni cambiar sus reglas para alcanzar la cifra.
- Mercados: acciones y bonos argentinos, CEDEARs, acciones de EE. UU. y cripto · Plataforma: plataforma de mi bróker aún sin identificar; TradingView para gráficos y pruebas de SPY.
- Estilo: trading sistemático, con reglas escritas y comprobables, sin depender de decidir bajo presión.
- Tamaño de posición mencionado: alrededor del 10–15 % del capital; no equivale al riesgo ni limita la pérdida si no hay stop.
- Lo que no hago: no operar de forma nocturna. La regla SPY diaria puede mantener una posición abierta durante la noche; no usarla en real hasta confirmar que esto te resulta aceptable.
- Fondeo: no aplica; usaré capital propio.

## Qué estrategias encajan conmigo
- Reglas escritas y comprobables, sin depender de decidir bajo presión.
- Horarios y gestión compatibles con Buenos Aires y con evitar la operativa nocturna.
- Riesgo por operación cuantificado con un stop; una señal de salida no garantiza limitar la pérdida.
- Revisar resultados con datos reales y costes, sin prometer rentabilidad ni forzar una cantidad de operaciones.

## Qué NO encaja conmigo
- Una estrategia sin stop si necesito limitar cada pérdida al 5 % de la cuenta.
- Considerar 64 operaciones de distintos activos como prueba de una sola estrategia.
- Automatizar órdenes reales en un activo o bróker cuya disponibilidad y conexión no estén confirmadas.

## Mi riesgo principal
El 5 % declarado por operación coincide con el límite de pérdida diaria: una sola pérdida máxima lo alcanzaría. La auditoría demo también registró reentradas rápidas tras perder y aumentos de tamaño después de una pérdida.

## Lo que digo frente a lo que hago
- Dices que apagarías al perder 5 % en un día; la auditoría demo registró 11 reentradas dentro de una hora tras perder (−300 USD). Es una diferencia a vigilar, no un juicio.
- Dices que revisarías después de 64 operaciones; las 64 de la auditoría mezclan activos y tipos de operativa, así que no cuentan como muestra de 64 operaciones de SPY.

## Mis límites en números
Estimación fechada 2026-10-28; no es una predicción. Se usó el resumen de la auditoría demo (59 % de acierto y ratio ganancia media/pérdida media 0,873), un riesgo de 5 % y una secuencia simulada de 64 operaciones:
- Pérdidas seguidas hasta superar la caída máxima del 15 %: 4.
- En 3 meses: la mitad de las simulaciones tuvo una racha máxima de 4 o más pérdidas; 1 de cada 20, 7 o más.
- Caída máxima simulada en 3 meses: típica 26,5 %; 1 de cada 20 simulaciones, 46,9 % o más.
- Probabilidad simulada de tocar el 15 % en esas 64 operaciones: 93 %.
- Lo que toca aguantar sin cambiar reglas: la racha simulada de pérdidas; al alcanzar el límite de apagado, se detiene y se revisa, no se sigue operando.

La estimación presupone operaciones independientes y repite estadísticas de una muestra demo pequeña y mezclada; no demuestra que esa frecuencia, esas estadísticas o esos resultados se repitan. En el backtest actual de SPY hubo solo 3 operaciones fuera de muestra: no alcanza para estimar la frecuencia o el riesgo de esa estrategia.

## Lo que no cuadraba y cómo lo resolví
- Buscar estrategias rentables en 3 meses no se puede garantizar; se usará como plazo para aprender y evaluar, no como promesa de ganancias.
- El riesgo máximo del 5 % por operación y una regla sin stop no son compatibles como límite efectivo: queda pendiente definir un stop o aceptar que la pérdida puede superar ese porcentaje antes de usarla en real.
- La regla diaria de SPY puede mantener posiciones de noche; queda pendiente confirmar ese punto.
- «64 operaciones» será una meta de revisión, no una cuota de ejecución ni una razón para aumentar operaciones. Deben pertenecer a la misma estrategia.
- Binance es una plataforma de cripto; no se da por hecho que permita operar SPY. TradingView se usará aquí para graficar y probar, no como confirmación de conexión al bróker.

## Supuestos
1. Los 5.000 son una aproximación en USD, consistente con la auditoría de ejemplo; no se guardan datos de cuenta.
2. El 5 % es un límite declarado por el trader, no una recomendación ni un riesgo probado.
3. La referencia de 21,33 operaciones al mes usada por la simulación (64 en 3 meses) procede del historial mezclado, no de la estrategia SPY.
4. No se proporcionaron límites de pérdida ni otras reglas de una empresa de fondeo porque no aplica.

## Revísalo
Cuando cambie mi capital, mi tiempo o mi objetivo, o cada 3 meses: /objetivos
