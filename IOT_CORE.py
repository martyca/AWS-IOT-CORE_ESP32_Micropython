import time
from umqtt.simple import MQTTClient
import json

SSID        = '<SSID>'
PASS        = '<SSID-PASSPHRASE>'
THING_NAME  = 'ESP32'
TOPIC       = 'ESP32/sub'
ENDPOINT    = '<ENDPOINT_ID>.iot.<REGION>.amazonaws.com'
ROOT_CA     = open('./AmazonRootCA1.pem', 'r').read()
CERTIFICATE = open('./certificate.pem.crt', 'r').read()
PRIVATE_KEY = open('./private.pem.key', 'r').read()
SSL_CONFIG  = {'key': PRIVATE_KEY,'cert': CERTIFICATE, 'server_side': False}



def connect_wifi():
  import network
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
    print('Connecting to network...')
    sta_if.active(True)
    sta_if.connect(SSID, PASS)
    while not sta_if.isconnected():
      pass
  print('Connected to network...')
  print('network config:', sta_if.ifconfig())

def message_callback(topic, message):
  print(json.loads(message))

def connect_iot_core():
  mqtt = MQTTClient( THING_NAME, ENDPOINT, port = 8883, keepalive = 10000, ssl = True, ssl_params = SSL_CONFIG )
  mqtt.connect()
  mqtt.set_callback(message_callback)
  print('Connected to: {}'.format(ENDPOINT))
  mqtt.subscribe(TOPIC)
  print('Subscribed to topic: {}'.format(TOPIC))
  return mqtt
  
if __name__ == '__main__':
  connect_wifi()
  subscription = connect_iot_core()
  while True:
     subscription.wait_msg()
     time.sleep(1)
