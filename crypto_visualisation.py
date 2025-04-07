import pandas as pd
import matplotlib.pyplot as plt

def visualiser_crypto_data(file_path):
    data = pd.read_csv(file_path)
    
    data['price_btc'] = pd.to_numeric(data['price_btc'], errors='coerce')
    data['price_eth'] = pd.to_numeric(data['price_eth'], errors='coerce')
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.dropna(subset=['price_btc', 'price_eth', 'timestamp'], inplace=True)

    # Bitcoin
    plt.figure(figsize=(10, 5))
    plt.plot(data['timestamp'], data['price_btc'], label="Prix Bitcoin", color="orange")
    plt.title("Évolution du prix de Bitcoin")
    plt.xlabel("Temps")
    plt.ylabel("Prix (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("/home/ubuntu/ScrappingProject/bitcoin_prices.png")
    plt.show()

    # Ethereum
    plt.figure(figsize=(10, 5))
    plt.plot(data['timestamp'], data['price_eth'], label="Prix Ethereum", color="green")
    plt.title("Évolution du prix d'Ethereum")
    plt.xlabel("Temps")
    plt.ylabel("Prix (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("/home/ubuntu/ScrappingProject/ethereum_prices.png")
    plt.show()
