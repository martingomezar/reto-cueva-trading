# Auditoría de mi historial · Auditor TIS (EJEMPLO)

Cuenta ••••0000 (demo) · 2 jun 2026 a 26 ago 2026 · 64 operaciones cerradas

## Números
- Resultado neto: +1.133,90 USD
- Factor de beneficio: 1,28 (sin la mejor operación: 1,21)
- Ganadoras: 59 % (38 de 64)
- Ganancia media 137,83 USD · pérdida media 157,83 USD
- Caída máxima: 8,8 % (921,69 USD)
- Los 4 números TIS aplicados a mi historial real: 3/4 (no es un backtest)

## Desglose
- Por activo: XAUUSD +1.638 USD (28 op.) · EURUSD +124 USD (9 op.) · USTEC −628 USD (27 op.)
- Manual vs automático: Manual +1.189 USD (52 op.) · Automática «ORB» −55 USD (12 op.)
- Por dirección: Ventas (cortos) +652 USD (28 op.) · Compras (largos) +482 USD (36 op.)
- Posiciones abiertas: XAUUSD compra −212 USD sin stop

## Hallazgos
- [ALERTA] Tienes una posición abierta sin stop. Va −212,40 USD en flotante y nada la limita. Es el riesgo más grande de toda tu cuenta en este momento.
- [ALERTA] Vuelves a entrar rápido después de perder. 11 veces abriste otra operación menos de una hora después de cerrar una perdedora. Resultado de esas operaciones: −300 USD.
- [ATENCIÓN] En USTEC vas en negativo. 27 operaciones con −628 USD. Donde mejor te va es XAUUSD (+1.638 USD). Con tan pocas operaciones todavía no se sabe si es el activo o la racha.
- [ATENCIÓN] Subes el tamaño después de perder. 12 veces aumentaste el volumen en el mismo activo justo después de una pérdida. Es la forma más rápida de agrandar una caída.
- [ATENCIÓN] Tu peor horario: 04:00 a 08:00. 3 operaciones con −185 USD (hora del servidor de tu bróker). Pocas operaciones: tómalo como pista.
- [ATENCIÓN] Aguantas más las pérdidas que las ganancias. Tus perdedoras duran en promedio 4,6 h y tus ganadoras 2,9 h.
- [ATENCIÓN] Tu regla automática «ORB» va en negativo en tu cuenta. 12 operaciones, 58 % ganadoras, −55 USD. Son 12 operaciones: muy pocas para saber si la regla tiene ventaja o si fue una mala racha. Eso solo lo responde un backtest con años de datos.
- [FORTALEZA] Tu mejor horario: 16:00 a 20:00. 24 operaciones con +567 USD (hora del servidor de tu bróker). Pocas operaciones: tómalo como pista.

## Hipótesis para probar
1. Lo que haces a mano en XAUUSD se puede escribir como regla. En tu cuenta, tus operaciones manuales van en positivo. Si logras escribir qué ves antes de entrar en XAUUSD, esa regla se puede medir con datos y dejar de depender de tu estado de ánimo. (52 operaciones manuales · +1.189 USD)
2. Operar solo de 16:00 a 20:00. Es tu mejor franja horaria, aunque con pocas operaciones. La hipótesis: en ese horario el mercado se mueve de una forma que aprovechas. Una regla limitada a esas horas se puede probar. (24 operaciones · +567 USD · hora del servidor)
3. Una pausa de una hora después de cada pérdida. Si no hubieras operado en la hora siguiente a una pérdida, tu resultado habría mejorado +300 USD. Es una regla de conducta que se puede probar y automatizar. (11 operaciones · −300 USD)

---
Director: usa la skill auditor. Con este informe, escribe estas 3 hipótesis como fichas de la fase 01 en fichas/, márcalas como «propuesta, confírmala» y dime cuál tiene más sentido trabajar en el Reto. No inventes cifras que no estén aquí.
