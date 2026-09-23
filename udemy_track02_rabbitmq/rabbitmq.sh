#!/bin/sh
echo "Avvio RabbitMQ....."
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl status rabbitmq-server
