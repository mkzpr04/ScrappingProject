#!/bin/bash

# Télécharger la page HTML de Bitcoin
curl -s https://coinmarketcap.com/currencies/bitcoin/ > bitcoin_page.html
# Télécharger la page HTML d'Ethereum
curl -s https://coinmarketcap.com/currencies/ethereum/ > ethereum_page.html


# Extraire le prix actuel de Bitcoin et remplacer les virgules par des espaces
price_btc=$(grep -oP '(?<=<span class="sc-65e7f566-0 WXGwg base-text" data-test="text-cdp-price-display">)\$[0-9,\.]+' bitcoin_page.html | sed 's/\$//g' | sed 's/,//g')
price_eth=$(grep -oP '(?<=<span class="sc-65e7f566-0 WXGwg base-text" data-test="text-cdp-price-display">)\$[0-9,\.]+' ethereum_page.html | sed 's/\$//g' | sed 's/,//g')

# Extraire le Market Cap (première occurrence correspondant au vrai market cap) et remplacer les virgules par des espaces
market_cap_btc=$(grep -oP '(?<=<div class="BasePopover_base__T5yOf popover-base"><span>)\$[0-9\.TMBK]+' bitcoin_page.html | head -n 1 | sed 's/\$//g' | sed 's/,//g')
market_cap_eth=$(grep -oP '(?<=<div class="BasePopover_base__T5yOf popover-base"><span>)\$[0-9\.TMBK]+' ethereum_page.html | head -n 1 | sed 's/\$//g' | sed 's/,//g')

# Extraire le Volume 24h (deuxième occurrence) et remplacer les virgules par des espaces
volume_24h_btc=$(grep -oP '(?<=<div class="BasePopover_base__T5yOf popover-base"><span>)\$[0-9\.TMBK]+' bitcoin_page.html | sed -n '2p' | sed 's/\$//g' | sed 's/,//g')
volume_24h_eth=$(grep -oP '(?<=<div class="BasePopover_base__T5yOf popover-base"><span>)\$[0-9\.TMBK]+' ethereum_page.html | sed -n '2p'| sed 's/\$//g' | sed 's/,//g')

timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# Définir le fichier CSV
csv_file="/home/mkzpr0/ScrappingProject/crypto_data.csv"

# Vérifier si le fichier CSV existe, sinon ajouter un header
if [ ! -f "$csv_file" ]; then
    echo "timestamp,price_btc,market_cap_btc,volume_24h_btc,price_eth,market_cap_eth,volume_24h_eth" > "$csv_file"
fi
# Ajouter la nouvelle ligne avec timestamp
echo "$timestamp,$price_btc,$market_cap_btc,$volume_24h_btc,$price_eth,$market_cap_eth,$volume_24h_eth" >> "$csv_file"

