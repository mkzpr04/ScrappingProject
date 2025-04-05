import crypto_metrics
import crypto_visualisation

file_path = "/home/ubuntu/crypto_data.csv"

# calcul des métriques
metrics = crypto_metrics.calcul_metrics(file_path)

# résultats des métriques
print(f"Volatilité Bitcoin : {metrics['volatilite_btc']:.2f}")
print(f"Volatilité Ethereum : {metrics['volatilite_eth']:.2f}")
print(f"Rendement Bitcoin sur 24h : {metrics['rendement_btc_24h']:.2f}%")
print(f"Rendement Ethereum sur 24h : {metrics['rendement_eth_24h']:.2f}%")
print(f"Rendement total Bitcoin : {metrics['rendement_btc_total']:.2f}%")
print(f"Rendement total Ethereum : {metrics['rendement_eth_total']:.2f}%")

crypto_visualisation.visualiser_crypto_data(file_path)
