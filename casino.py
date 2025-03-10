import random
import pandas as pd
import polars as pl

def juego_casino(n_rondas):
    fondos = 1000
    monto_apuesta = fondos
    historial = []
    opciones = ['cara', 'cruz']
    
    for _ in range(n_rondas):
        lanzamiento = random.choice(opciones)
        resultado_dado = random.randint(1, 6)
        
        if lanzamiento == 'cara' and resultado_dado % 2 == 0:
            fondos *= 2
            monto_apuesta = fondos / 2
            historial.append(1)
        else:
            fondos -= monto_apuesta
            monto_apuesta *= 2
            historial.append(0)
    
    df_pandas = pd.DataFrame({'victorias': historial})
    df_polars = pl.DataFrame({'victorias': historial})
    
    print(f"Media: {df_pandas.mean().values[0]}, Mediana: {df_pandas.median().values[0]}, Moda: {df_pandas.mode().values[0][0]}")
    print("-" * 34)
    print(f"Media (Polars): {df_polars.mean().item()}, Mediana (Polars): {df_polars.median().item()}")
    print(f"Saldo final: {fondos}, Última apuesta: {monto_apuesta}")

juego_casino(100)


