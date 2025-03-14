import pandas as pd
import numpy as np

def calcul_metrics(file_path):
    data = pd.read_csv(file_path)

    #conversion numérique
    data['price_btc'] = pd.to_numeric(data['price_btc'], errors='coerce')
    data['price_eth'] = pd.to_numeric(data['price_eth'], errors='coerce')

    # Volatilité
    volatilite_btc = np.std(data['price_btc'].pct_change())  # Retour quotidien
    volatilite_eth = np.std(data['price_eth'].pct_change())  # Retour quotidien

    # Rendement : (variation totale des prix sur toute la période)
    rendement_btc = (data['price_btc'].iloc[-1] - data['price_btc'].iloc[0]) / data['price_btc'].iloc[0] * 100
    rendement_eth = (data['price_eth'].iloc[-1] - data['price_eth'].iloc[0]) / data['price_eth'].iloc[0] * 100

    # Rendement_24h
    if len(data)>288:
        rendement_btc_24h = (data['price_btc'].iloc[-1] - data['price_btc'].iloc[-288]) /data['price_btc'].iloc[-288] * 100
        rendement_eth_24h = (data['price_eth'].iloc[-1] - data['price_eth'].iloc[-288]) / data['price_eth'].iloc[-288] * 100
    else:
        rendement_btc_24h = rendement_btc
        rendement_eth_24h = rendement_eth

    # Moyenne mobile sur 7 jours (SMA)
    sma_btc = data['price_btc'].rolling(window=7).mean()
    sma_eth = data['price_eth'].rolling(window=7).mean()

    return {
        'volatilite_btc': volatilite_btc,
        'volatilite_eth': volatilite_eth,
        'rendement_btc_24h': rendement_btc_24h,
        'rendement_eth_24h': rendement_eth_24h,
        'rendement_btc_total': rendement_btc,
        'rendement_eth_total': rendement_eth,
        'sma_btc': sma_btc,
        'sma_eth': sma_eth
    }