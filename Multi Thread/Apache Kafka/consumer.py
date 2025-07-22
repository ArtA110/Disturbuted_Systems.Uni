from kafka import KafkaConsumer
import json
import threading
import time

NUM_MESSAGES = 1000
counter = 0
lock = threading.Lock()
start_time = None

def process_message(msg_id):
    global counter
    time.sleep(0.01)
    with lock:
        global counter
        counter += 1
        if counter % 100 == 0:
            print(f"Processed {counter} messages")
        if counter == NUM_MESSAGES:
            print(f"Done processing all messages in {time.time() - start_time}")

def consume():
    global start_time
    consumer = KafkaConsumer(
        'work-topic',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id='worker-group',
        enable_auto_commit=True,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    start_time = time.time()
    for message in consumer:
        threading.Thread(target=process_message, args=(message.value['id'],)).start()
        if counter >= NUM_MESSAGES:
            break

consume()
