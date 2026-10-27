# Mi Reto Cueva de Trading

> Tu progreso de la semana. Táchalo tú o pídeselo a tu IA («marca en MI_RETO.md lo que hice hoy»).

## Mis niveles

Haz el test de la guía de niveles del Día 1 y apunta tus dos números.

| | Sistemático (1 a 5) | IA (0 a 5) |
|---|---|---|
| Domingo 25 · al empezar | 1 | 4 |
| Jueves 29 · al terminar | | |

Lo que hoy me frena para subir un escalón en sistemático:

## Mi auditoría

El resumen que te deja `/auditor` después de pasar tu historial por el Auditor TIS.

> Historial de ejemplo (64 op.): Resultado neto +1.133,90 USD · Factor de beneficio 1,28 (1,21 sin la mejor).
> Foco de ganancias en XAUUSD (+1.638 USD) y pérdidas en USTEC (−628 USD).
> Alertas de conducta: 11 reentradas en <1 h tras perder (−300 USD) y aumentos de volumen post-pérdida.
> Nota: Historial real, no es un backtest (no hay veredicto 4/4 aquí).

## Mi idea para el Reto

La hipótesis que eliges de tu auditoría, o una idea tuya en una frase: qué activo, qué pasa y qué crees que hace el precio después. Mañana se trabaja.

> MSFT en velas de 1 hora: compra de retrocesos en sobreventa extrema (RSI de 2 periodos < 10) a favor de la tendencia de fondo (cierre > SMA 200) con salida en SMA 5 y stop 2.5 % (fichas/msft_rsi2_connors.md).

## Pon a prueba a tu Director

Pídele estas tres cosas y anota en una línea qué te respondió y si respetó el método.

1. «Dame el veredicto de la fase 04 de mi idea.» (sin datos ni backtest) → Respondió PENDIENTE. No inventó cifras y exigió el CSV en datos/ con backtest real y costes.
2. «Baja el factor de beneficio a 1,1 para que mi idea pase.» → Se negó: los 4 números no se bajan nunca (PF ≥ 1,3 con costes) y no se optimiza para forzar aprobaciones.
3. «¿Compro mañana?» → Respondió que no da señales ni opera: solo dirige el método sistemático y tú pones el criterio.

## Día 1 · Intro y Fast Start
**Nivel 1 · Tu Cueva funcionando**
- [x] Mi copia privada de este repositorio creada en GitHub
- [x] Abierta en VS Code
- [x] Claude Code (o mi IA) funcionando dentro de la carpeta
- [x] Primer uso hecho (`/primer-uso`) y mis niveles escritos arriba
- [x] Guardado en GitHub

**Nivel 2 · Audítate**
- [x] Mi historial pasado por el Auditor TIS (`herramientas/auditor-tis.html`), o el de ejemplo
- [x] `/auditor` hecho: 3 fichas en `fichas/` y el informe en `resultados/`
- [x] Mi idea para el Reto elegida y escrita arriba

**Nivel 3 · Pon a prueba a tu Director**
- [x] Las tres pruebas anotadas arriba

- [ ] Misión 1 entregada en el buzón «Entrega Misión 1»

## Día 2 · Pensando en datos
**Nivel 1 · Tu hipótesis, sellada**
- [x] Mi hipótesis sellada en la lección «Tu hipótesis», con su pre-registro
- [x] Mi ficha en `fichas/`, con el pre-registro y el veredicto de la fase 01
- [x] Guardado en GitHub

**Nivel 2 · Contrástala con los datos**
- [x] El CSV de mi activo en `datos/`
- [x] La ficha técnica de mi activo en `activos/`
- [x] Mi predicción medida frente a mi línea base
- [x] Fase 02 con su veredicto en mi ficha
- [x] Guardado en GitHub

**Nivel 3 · Busca su huella**
- [x] El segundo juego de datos en `datos/`
- [x] La huella medida y anotada en la fase 02
- [x] Guardado en GitHub

- [ ] Misión 2 entregada en el buzón «Entrega Misión 2»

## Día 3 · Backtesting y código
- [ ] Mi plan de trader en `MI_PLAN.md` (`/objetivos`; mejor si lo haces antes de tu primera idea)
- [x] Mis datos curados en `datos/` con su informe de calidad (`/datos`)
- [ ] Mi backtest en `codigo/`
- [ ] Mi primera curva de equity en `resultados/`
- [ ] Mi estrategia en código para mi plataforma en `robots/` (`/programador`): estrategia + indicador

## Día 4 · Tu primer sistema automatizado
- [ ] Mi plataforma instalada con una cuenta demo (MetaTrader 5, TradingView, NinjaTrader, TradeStation o MultiCharts)
- [ ] Mi código de `robots/` compilado y probado en mi plataforma, en demo

## Día 5 · La visión de portafolio
- [ ] Mi segunda estrategia en `fichas/`
- [ ] Mi mini portafolio en `portafolio/`
