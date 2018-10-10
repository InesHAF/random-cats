from flask import Flask, render_template
import random
from redis import Redis, RedisError
#import os
#import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2,
socket_timeout=2)
app = Flask(__name__)

# list of cat images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-32501-1$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-22919-1$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/4/6/9/anigif_enhanced-buzz-24011-1$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-32505-1$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-32585-1$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/4/6/9/anigif_enhanced-buzz-23997-1$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-22675-1$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr01/2013/4/6/9/anigif_enhanced-buzz-578-136$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-22911-1$
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/8/anigif_enhanced-buzz-22680-1$
]

@app.route('/')
def index():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    url = random.choice(images)
    return render_template('index.html', url=url,visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)



