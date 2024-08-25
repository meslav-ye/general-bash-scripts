#!/usr/bin/env python3.9
import time
from datetime import datetime
from kafka import KafkaProducer

TOPIC_NAME = "test-topic"

producer = KafkaProducer(
    bootstrap_servers=f"<change-IP>:9094",

)

for i in range(100):
    ts = datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f")
    message = f"Hello from Python message: {i + 1}, Timestamp: "+ts+"."
    producer.send(TOPIC_NAME, message.encode('utf-8'))
    print(f"Message sent: {message}")
    time.sleep(1)

producer.close()