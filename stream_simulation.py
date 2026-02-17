import pandas as pd
from kafka import KafkaProducer
import json
import time

# --- Kafka Configuration ---
# This producer will send messages to a Kafka broker running on your machine.
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Encode messages as JSON
)

# The "topic" is like a channel name in Kafka. We'll call ours 'ecommerce_transactions'.
KAFKA_TOPIC = 'ecommerce_transactions'

print("--- Starting Kafka Producer ---")
print(f"Will send messages to topic: '{KAFKA_TOPIC}'")

# --- Read the CSV and Stream Data ---
df = pd.read_csv('ecommerce_data.csv')

# Loop through each row of the DataFrame
for index, row in df.iterrows():
    # Convert the row to a dictionary (which can be easily converted to JSON)
    message = row.to_dict()

    # Send the message to the Kafka topic
    producer.send(KAFKA_TOPIC, value=message)

    print(f"Sent: {message['transaction_id']}")

    # Wait for a short time to simulate a real-time stream
    time.sleep(0.5)

# Ensure all messages are sent before exiting
producer.flush()
producer.close()

print("\n--- Kafka Producer Finished ---")
