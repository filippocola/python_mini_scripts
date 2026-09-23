import pika 
# consuma i messaggi creati dal producer

def callback(ch, method, properties, msg):
    print(f"Ricevuto messaggio N°: {msg}")


if __name__ == "__main__":
    print("Collegamento a RabbitMQ...")
    connectionParameters = pika.ConnectionParameters(host="localhost")
    connection = pika.BlockingConnection(connectionParameters)

    # creazione canale 
    channel = connection.channel()

    # dichiarazione della queue
    channel.queue_declare(queue="worker_queue", durable=True)

    print("Creazione client...")
    channel.basic_consume(queue="worker_queue", on_message_callback=callback, auto_ack=False, exclusive=False, consumer_tag=None )
    channel.start_consuming()