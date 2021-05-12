import discord
import os
import requests
import json
import re

cryptoClient = discord.Client()

apikey = 'APIKEY'

def get_btc_pln():
  cryptourlbtc = 'https://coinlib.io/api/v1/coin?key=XXX&pref=PLN&symbol=BTC'
  response = requests.get(cryptourlbtc)
  json_data = json.loads(response.text)
  price = json_data["price"]
  crcurpln = "Bitcoin price in PLN: " + re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(price))
  return crcurpln

def get_eth_pln():
  cryptourleth = 'https://coinlib.io/api/v1/coin?key=XXX&pref=PLN&symbol=ETH'
  response = requests.get(cryptourleth)
  json_data = json.loads(response.text)
  price = json_data["price"]
  crcurpln = "Etherum price in PLN: " + re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(price))
  return crcurpln  

def get_ltc_pln():
  cryptourlltc = 'https://coinlib.io/api/v1/coin?key=XXX&pref=PLN&symbol=LTC'
  response = requests.get(cryptourlltc)
  json_data = json.loads(response.text)
  price = json_data["price"]
  crcurpln = "Litecoin price in PLN: " + re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(price))
  return crcurpln  
    
def get_btc_usd():
  response = requests.get('https://coinlib.io/api/v1/coin?key=XXX&pref=USD&symbol=BTC')
  json_data = json.loads(response.text)
  price = json_data["price"]
  crcurusd = "Bitcoin price in USD: " + re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(price))
  return crcurusd

print(get_btc_pln())

@cryptoClient.event
async def on_ready():
  print(f'We have logged in as {cryptoClient.user}')

@cryptoClient.event
async def on_message(message):

  if (message.author == cryptoClient.user):
    return

  if (message.content.startswith('$jasioka')):
    crcurpln = get_btc_pln()
    await message.channel.send("Czary mary hokus pokus jasioka to mały łobuz")

  if (message.content.startswith('$btcpln')):
    crcurpln = get_btc_pln()
    await message.channel.send(crcurpln)
  
  if (message.content.startswith('$ethpln')):
    crcurpln = get_eth_pln()
    await message.channel.send(crcurpln)

  if (message.content.startswith('$ltcpln')):
    crcurpln = get_ltc_pln()
    await message.channel.send(crcurpln)


cryptoClient.run(os.getenv('TOKEN'))
