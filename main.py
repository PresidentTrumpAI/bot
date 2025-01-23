from tracemalloc import start
import tweepy
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
consumer_key='ubh3iKsW8hTN2SpeCjANqPovw'
consumer_secret='De12ZkOVUdrmJu212bbR0yAZJ6kxJwh8YYVr55ym5rKQDvbLmn'
access_token='1794082831334830080-drbpwePUq9dqRo49HBfDUPneIWxBes'
access_token_secret='wVgD67izmSUmhcZ9Lj54sPPPDz3bGtV3YNn2quUFMMr55'

# Telegram bot token
telegram_token='wVgD67izmSUmhcZ9Lj54sPPPDz3bGtV3YNn2quUFMMr55'

# Initialize Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Initialize Telegram bot
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

# List of influential Twitter usernames
usernames = [
    '@elonmusk', '@BillyM2k', '@VitalikButerin', '@ShytoshiKusama', '@MattWallace888', '@ProTheDoge', 
    '@DavidGokhshtein', '@cz_binance', '@Bitboy_Crypto', '@CryptoBitlord', '@WatcherGuru', '@CoinMarketCap', 
    '@ShibaInuHodler', '@DOGEofficialceo', '@WhaleChart', '@SHIBarmy', '@cryptocom', '@CoinDesk', '@FlokiInu', 
    '@PepeCommunity', '@AltcoinGordon', '@Pentoshi', '@TheMoonCarl', '@cryptunez', '@CryptoCapo_', '@InuWhale', 
    '@KoroushAK', '@satoshi_stacker', '@AltcoinSherpa', '@rektcapital', '@Dogecoin', '@ShibaInuCoin', 
    '@BabyDogeCoin', '@AkitaToken', '@FlokiInuCoin', '@KishuInuToken', '@Samoyedcoin', '@HogeFinance', 
    '@Pitbull_BSC', '@CheemsInu', '@0xPolygon', '@Uniswap', '@CoinGecko', '@whale_alert', '@CryptoKaleo', 
    '@elonmeme', '@DogeWhaleAlert', '@MemecoinKing', '@CryptoBull2020', '@MemeCoinDaily'
]




def tweet(update, context):
    messages = []
    for username in usernames:
        try:
            # Retrieve the latest tweet from the user
            latest_tweet = api.user_timeline(screen_name=username, count=1)[0]
            messages.append(f"{username}: {latest_tweet.text}")
        except Exception as e:
            messages.append(f"Failed to retrieve tweet from {username}: {str(e)}")
    
    # Send the tweets to the Telegram group
    for message in messages:
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Register handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

tweet_handler = CommandHandler('tweet', tweet)
dispatcher.add_handler(tweet_handler)

# Start the bot
updater.start_polling()
updater.idle()