# Producer
import pika 
import time 
if __name__ == "__main__":
    try:
        print("Collegamento a RabbitMQ...")
        connectionParameters = pika.ConnectionParameters(host="localhost")
        connection = pika.BlockingConnection(connectionParameters)

        # creazione canale 
        channel = connection.channel()

        # dichiarazione della queue
        channel.queue_declare(queue="worker_queue", durable=True)
        print("Connessione eseguita...")

        print("Creazione client...")
        i: int = 0
        while True:
            message: str = str(i)
            i += 1
            # routing_key == binding (nome coda)
            channel.basic_publish(exchange='', routing_key='worker_queue', body=message)
            print("Inviato Messagggio N° : ", message)
            time.sleep(1)
            if i > 100_000:
                break
        connection.close()
    except Exception as e:
        print(f"Qualcosa è andato storto... \n")
        print(f"{e}")