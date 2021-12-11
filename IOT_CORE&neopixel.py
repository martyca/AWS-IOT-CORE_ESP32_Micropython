import time
from umqtt.simple import MQTTClient
import json
import machine
import neopixel



SSID        = '<SSID>'
PASS        = '<SSID-PASSPHRASE>'
THING_NAME  = 'ESP32'
TOPIC       = 'ESP32/sub'
ENDPOINT    = '<ENDPOINT_ID>.iot.<REGION>.amazonaws.com'
ROOT_CA     = open('./AmazonRootCA1.pem', 'r').read()
CERTIFICATE = open('./certificate.pem.crt', 'r').read()
PRIVATE_KEY = open('./private.pem.key', 'r').read()
SSL_CONFIG  = {'key': PRIVATE_KEY,'cert': CERTIFICATE, 'server_side': False}
LEDCOUNT    = 8
LEDPIN      = 13

np = neopixel.NeoPixel(machine.Pin(LEDPIN), LEDCOUNT)

def yellowPixel(lednumber):
    np[lednumber] = (128,128,0)
    np.write()

def greenPixel(lednumber):
    np[lednumber] = (0,128,0)
    np.write()

def redPixel(lednumber):
    np[lednumber] = (128,0,0)
    np.write()

def connect_wifi():
  import network
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
    print('Connecting to network...')
    yellowPixel(0)
    sta_if.active(True)
    sta_if.connect(SSID, PASS)
    while not sta_if.isconnected():
      pass
  print('Connected to network...')
  greenPixel(0)
  print('network config:', sta_if.ifconfig())

def message_callback(topic, message):
  message = json.loads(message)
  print(message)
  if 'leddata' in message:
    for i in range(len(message['leddata'])):
      np[i] = message['leddata'][i]
    np.write()

def connect_iot_core():
  print('Connecting to: {}'.format(ENDPOINT))
  yellowPixel(1)
  mqtt = MQTTClient( THING_NAME, ENDPOINT, port = 8883, keepalive = 10000, ssl = True, ssl_params = SSL_CONFIG )
  mqtt.connect()
  mqtt.set_callback(message_callback)
  print('Connected to: {}'.format(ENDPOINT))
  greenPixel(1)
  mqtt.subscribe(TOPIC)
  print('Subscribed to topic: {}'.format(TOPIC))
  greenPixel(2)
  return mqtt
  
if __name__ == '__main__':
  np.fill((0,0,0))
  connect_wifi()
  subscription = connect_iot_core()
  while True:
     subscription.wait_msg()
     time.sleep(1)
