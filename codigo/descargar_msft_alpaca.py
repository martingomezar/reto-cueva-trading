"""Descarga de barras históricas de MSFT desde Alpaca.
Usa credenciales desde el archivo .env (nunca se suben a GitHub).
"""
from datetime import datetime
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.enums import Adjustment, DataFeed

def descargar():
    env = dict(l.strip().split('=', 1) for l in open('.env') if '=' in l and not l.startswith('#'))
    c = StockHistoricalDataClient(env['ALPACA_API_KEY'].strip(), env['ALPACA_SECRET_KEY'].strip())
    
    r = StockBarsRequest(
        symbol_or_symbols='MSFT',
        timeframe=TimeFrame.Hour,
        start=datetime(2016, 1, 1),
        adjustment=Adjustment.ALL,
        feed=DataFeed.IEX
    )
    
    bars = c.get_stock_bars(r)
    df = bars.df
    if not df.empty:
        df.reset_index().to_csv('datos/crudos/msft_1h_alpaca.csv', index=False)
        print(f"Descargadas {len(df)} barras crudas en datos/crudos/msft_1h_alpaca.csv")

if __name__ == '__main__':
    descargar()
