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

np = neopixel.NeoPixel(machine.Pin(LEDPIN), LEDCOUNT
)
def clearstrip(LEDCOUNT):
  print('Clearing led strip.')
  for i in range(LEDCOUNT):
    np[i] = (0,0,0)
  np.write()

def connect_wifi():
  import network
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
    print('Connecting to network...')
    np[0] = (128,128,0)
    np.write()
    sta_if.active(True)
    sta_if.connect(SSID, PASS)
    while not sta_if.isconnected():
      pass
  print('Connected to network...')
  np[0] = (0,128,0)
  np.write()
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
  np[1] = (128,128,0)
  np.write()
  mqtt = MQTTClient( THING_NAME, ENDPOINT, port = 8883, keepalive = 10000, ssl = True, ssl_params = SSL_CONFIG )
  mqtt.connect()
  mqtt.set_callback(message_callback)
  print('Connected to: {}'.format(ENDPOINT))
  np[1] = (0,128,0)
  np.write()
  mqtt.subscribe(TOPIC)
  print('Subscribed to topic: {}'.format(TOPIC))
  np[2] = (0,128,0)
  np.write()
  return mqtt
  
if __name__ == '__main__':
  clearstrip(LEDCOUNT)
  connect_wifi()
  subscription = connect_iot_core()
  while True:
     subscription.wait_msg()
     time.sleep(1)
