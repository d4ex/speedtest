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

def speedtest(sc): 
    print("Start Speedtest...")
    
    try: 
        result = subprocess.run(['speedtest-cli', '--json'], stdout=subprocess.PIPE)
        jsonObj = json.loads(result.stdout.decode('utf-8'), object_hook=lambda d: SimpleNamespace(**d))
        print(jsonObj.download, jsonObj.upload, jsonObj.ping)
    
        DOWNLOAD.set(jsonObj.download)
        UPLOAD.set(jsonObj.upload)
        PING.set(jsonObj.ping)
 
        s.enter(300, 1, speedtest, (sc,))
    except:
        print("Unexpected error: Result - ", result)
        s.enter(300, 1, speedtest, (sc,))

s.enter(5, 1, speedtest, (s,))
start_http_server(8000)
s.run()
