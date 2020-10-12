#!/usr/bin/python

from prometheus_client import start_http_server, Gauge
import random
import sched, time
import subprocess

import json
from types import SimpleNamespace

DOWNLOAD: Gauge = Gauge('download', 'down_gauge')
UPLOAD: Gauge = Gauge('upload', 'up_gauge')
PING: Gauge = Gauge('ping', 'ping_Gauge')
s = sched.scheduler(time.time, time.sleep)

def do_something(sc): 
    print("Start Speedtest...")
    
    result = subprocess.run(['speedtest-cli', '--json'], stdout=subprocess.PIPE)
    jsonObj = json.loads(result.stdout.decode('utf-8'), object_hook=lambda d: SimpleNamespace(**d))
    print(jsonObj.download, jsonObj.upload, jsonObj.ping)
    
    DOWNLOAD.set(jsonObj.download)
    UPLOAD.set(jsonObj.upload)
    PING.set(jsonObj.ping)
 
    s.enter(300, 1, do_something, (sc,))

s.enter(5, 1, do_something, (s,))
start_http_server(8000)
s.run()



data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.

