import paho.mqtt.publish as publish

topic = "paradise/heart-rate/data"


def send_heart_rate(heart_rate):
	data = {data: str(heart_rate)}

	publish.single(topic, data, port=8883, tls={'ca_certs':"ca.crt",'tls_version':2}, hostname="nyx.bjornhaug.net")