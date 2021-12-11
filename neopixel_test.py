import machine
import neopixel
from time import sleep

LEDCOUNT = 8
LEDPIN   = 13
DELAY    = 0.1
np = neopixel.NeoPixel(machine.Pin(LEDPIN), LEDCOUNT)

if __name__ == '__main__':
  while True:
    for i in range(LEDCOUNT):
      np.fill((0,0,0))
      np[i] = (255,0,0)
      np.write()
      sleep(DELAY)
    for i in range(7,0,-1):
      np.fill((0,0,0))
      np[i] = (255,0,0)
      np.write()
      sleep(DELAY)
