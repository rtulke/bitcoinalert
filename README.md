# bitcoinalert
python script to send an email if your bitcoin price limit is less than something quick&amp;dirty

install:

* download
* set your price > limit = 260.00
* change smtp settings (email, username, password, server, port)
* chmod 700 bitcoinalert.py
* crontab -e

*/1	*	*	*	*	/home/yourname/bitcoinaltert.py

if you want another exchange rate then have a look at https://coinbase.com/api/v1/currencies/exchange_rates and pick your rate. 

for example

* british pound = btc_to_gbp and gbp_to_btc
* us dollar  = btc_to_usd and usd_to_btc

after than, change this in btc and data variable...
