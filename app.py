from flask import Flask, request, jsonify, session
import time
import threading
import datetime

app = Flask(__name__)

class token_bucket:
    def __init__(self, N):
        self.limit = N
        self.tokens = N
        self.lock = threading.Lock()
        threading.Thread(target=self._increment, daemon=True).start()
        

    def is_allowed(self, route):
        if route == '/unlimited':
            return True
        elif route == '/limited':
            return self.tokens > 0

        return False

    def _increment(self):
        while True:
            time.sleep(1)
            with self.lock:
                if self.tokens < self.limit:
                    self.tokens += 1

    def decrement(self):
        if self.tokens > 0:
            self.tokens -= 1
            
class fixed_window:
    def __init__(self,T, N):
        self.limit = N
        self.Tokens = 0
        self.window_length = T
        self.lock = threading.Lock()
        tm = datetime.datetime.now()
        self.start_time = self.time_floor(tm)

    def is_allowed(self, route):
        if route == '/unlimited':
            return True
        elif route == '/limited':
            with self.lock:
                if self.Tokens < self.limit:
                    return True
                elif datetime.datetime.now() - self.start_time > datetime.timedelta(seconds=self.window_length):
                    self.start_time = self.time_floor(datetime.datetime.now())
                    self.Tokens = 0
                    return True
                return False
        else:
            return False

    def time_floor(self, tm):
        return tm - datetime.timedelta(minutes=tm.minute % 1,
                                        seconds=tm.second,
                                        microseconds=tm.microsecond)

    def increment(self):
        with self.lock:
            if self.Tokens < self.limit:
                self.Tokens += 1

cache = {}

@app.route('/unlimited')
def unlimited_test():
    ip_addr = request.remote_addr
    if ip_addr not in cache:
        cache[ip_addr] = fixed_window(60, 60)
    return jsonify("Unlimited! Let's Go!"), 200

@app.route('/limited')
def limited_test():
    ip_addr = request.remote_addr
    if ip_addr not in cache:
        cache[ip_addr] = fixed_window(60, 60)
        
    limiter = cache[ip_addr]
    if not limiter.is_allowed('/limited'):
        return jsonify("Too many requests! Slow down!"), 429
    else:
        limiter.increment()
    return jsonify("Limited, don't over use me!"), 200



if __name__ == '__main__':
    app.run(debug=True)
    
