from kafka import KafkaProducer
import time
import json

NUM_MESSAGES = 1000

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

start = time.time()

for i in range(NUM_MESSAGES):
    producer.send('work-topic', {'id': i})
    if i % 100 == 0:
        print(f"Sent {i} messages...")

producer.flush()
end = time.time()
print(f"Sent {NUM_MESSAGES} messages in {end - start}")
