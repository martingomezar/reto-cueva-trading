# FICHA TÉCNICA · AED · MSFT (VELAS DE 1 HORA)

Fuente: Alpaca (`datos/msft_1h_alpaca.csv`)
Periodo: 2020-07-27 a 2026-10-26 (6.2 años · 11.416 velas de 1 hora)

## Personalidad del activo
- **Familia recomendada:** Seguir la tendencia de fondo / Comprar retrocesos en tendencia.
- **Tendencia de fondo:** Fuertemente alcista (+176.6 % total, +17.7 % CAGR anualizado). Pasa el 56.2 % del tiempo sobre su media de 200 velas horarias. Peor caída comprando y aguantando: −37.9 %.
- **Día a día:** Sin patrón claro a 1 vela (autocorrelación −0.0121: puro ruido).
- **Eficiencia de Kaufman:** Mediana 0.224 (domina el zigzag: las compras de rupturas dan señales falsas; los retrocesos a favor de la tendencia son la opción más robusta).
- **Forma de los movimientos:** Colas gordas (curtosis en exceso 20.49; 1.79 % de las velas superan 3 desviaciones estándar). Peor vela horaria: −7.9 %; mejor vela: +10.7 %.
- **Volatilidad:** 27.0 % anualizada (moderada en acciones grandes, pero con saltos por resultados trimestrales).
- **Línea base (% velas al alza):** 50.3 % de velas alcistas.
- **Calendario:** Lunes es el mejor día (+1.85 pb de media); Martes es el peor (−0.29 pb). La apertura de sesión (09:00 NY) concentra el mayor retorno positivo (+4.78 pb).

## Pistas para las reglas:
1. **Filtro de contexto:** Solo compras cuando el precio esté por encima de la media móvil de 200 velas (SMA 200).
2. **Disparador:** Comprar en sobreventa extrema (retroceso/zigzag) con RSI(2) < 10 en vez de perseguir rupturas.
3. **Stop obligatorio:** Por las colas gordas (curtosis 20.49 y peor vela de −7.9 %), usar stop fijo (ej. 2.5 % o 3.0 %).
4. **Salida rápida:** Salir al recuperar la media corta (SMA 5) para no quedar atrapado en reversiones.
