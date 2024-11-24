import dotenv
import krakenex
import os
import pandas as pd
dotenv.load_dotenv()

def get_BTC_data():
    ''' """
    Fetches Ethereum (ETH) OHLC data from Kraken API at a 60-minute interval.

    Returns:
    --------
    pd.DataFrame
        A DataFrame containing the following columns:
        - 'open': Opening price
        - 'high': Highest price
        - 'low': Lowest price
        - 'close': Closing price
        - 'vwap': Volume-weighted average price
        - 'volume': Total volume traded
        - 'count': Number of trades
        - 'Date': Timestamp converted to a human-readable datetime format
    """'''

    k = krakenex.API(os.getenv('KRAKEN_KEY'))
    data = k.query_public('OHLC', {'pair': 'XXBTZUSD', 'interval': 60})
    datos = data['result']['XXBTZUSD']  
    df = pd.DataFrame(datos)
            
    # Asignamos nombres a las columnas
    columns = ["timestamp", "open", "high", "low", "close", "vwap", "volume", "count"]
    df.columns = columns
            
    # Convertimos las columnas numéricas a tipo float
    df.close = df.close.astype(float)
    df.open = df.open.astype(float)
    df.high = df.high.astype(float)
    df.low = df.low.astype(float)
    df.vwap = df.vwap.astype(float)
    df.volume = df.volume.astype(float)
    # Convertimos el timestamp a formato de fecha
    df["Date"] = pd.to_datetime(df.timestamp, unit='s')
        
    # Eliminamos la columna timestamp ya que no la necesitamos
    df.drop('timestamp', axis=1, inplace=True)
            
            # Reiniciamos el índice para que sea consecutivo
    df.reset_index(drop=True, inplace=True)

    return df
        
         
