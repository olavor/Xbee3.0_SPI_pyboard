from pyb import SPI, Pin
import micropython,  time, ubinascii
micropython.kbd_intr(ord('q'))
p_out = Pin('Y5', Pin.OUT_PP)
p_out.high()
spi = SPI(2,SPI.MASTER,baudrate=500000,polarity=0,phase=0,firstbit=SPI.MSB,bits=8,crc=0x7)
data = [0x7E,0x00,0x11,0x10,0x01,0x00,0x13,0xA2,0x00,0x41,
        0x92,0xAE,0xAC,0xFF,0xFE,0x00,0x00,0x61,0x62,0x63,0xE9]
rbuf = bytearray(data)
#dd = b"".join(b'\\x%02x' % b for b in data)
ee = bytes(data)
jj= bytearray(bytes(data))
ax = ubinascii.hexlify(bytes(data))
print(len(ee))
print(ee)
data1 = 0x7E001110010013A2004192AEACFFFE0000616263E9
while True:
   x = input('digite 1 para o master enviar ')
   print(x)
   if x =='1':
      p_out.low()
      print('start SS alto')
      spi.send(jj)
      print('terminado')
      p_out.high()
   else:
      print('nada foi enviado')

------------------------------------------------------------------------- teste XBee3 slave

from pyb import Pin
from machine import SPI
import micropython,  time, ubinascii
micropython.kbd_intr(ord('q'))
import micropython
p_out = Pin('Y5', Pin.OUT_PP)
p_out.high()
rbuf = bytearray(24)
#data = [0x7E,0x00,0x11,0x10,0x01,0x00,0x13,0xA2,0x00,0x41,0x92,0xAE,0xAC,0xFF,0xFE,0x00,0x00,0x61,0x62,0x63,0xE9]
#rbuf = data
spi = machine.SPI(baudrate=500000,polarity=0,phase=0,firstbit=SPI.MSB,bits=8)
print('estou na espera')
while True:
   x = input('digite 1 para o SLAVE enviar ')
   print(x)
   p_out.low()
   if x =='1':
     spi.write(rbuf)





-------------------------------------------------------------------------
teste para pyboard slave

from pyb import Pin
from machine import SPI
import micropython
x1_pin = pyb.Pin.board.Y5
x1 = pyb.Pin(pyb.Pin.board.Y5)
rbuf = bytearray(24)

def x1_callback(line):
   spi.read(rbuf, 0)
   print(rbuf)
   print('recebi algo!')

spi = machine.SPI(2,baudrate=500000,polarity=0,phase=0,firstbit=SPI.MSB,bits=8)
print('estou na espera')
x_interrupt = pyb.ExtInt(x1_pin, pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_DOWN, x1_callback)







48











#spi.send(b'\x7E\x00\x14\x00\x00\x13\xA2\x00\x41\x84\x15\x3B\
               #xFF\xFE\x00\x00\x54\x78\x44\x61\x74\x61\xE2')
      #spi.send_recv(dd, rbuf)
      #SPI.write_readinto(dd, rbuf)
      #print(rbuf)
#SPI.write_readinto(data, rbuf)
#spi.send_recv(dd,rbuf)
#p_in = Pin('Y5', Pin.IN, Pin.PULL_NONE)
#byteToSend = 134
#x = p_in.value()#print(p_in.value())
#micropython.kbd_intr(ord('q'))
while True:
   if  x!= 0:
      for i in range(15):
         y =spi.recv(rbuf)
         print(rbuf)
      print('recebi algo!')
      x = p_in.value()
      print(rbuf)
      print(y)
   x = p_in.value()
while True:
    pass

ax = ubinascii.hexlify(bytes(data))
-------------------------------------------------------------
#data1 = 0x7E001410000013A2004184153BFFFE0000547844617461E2
print(data1)
firstbit=SPI.MSB,bits=8,ti=True
#ext = pyb.ExtInt('Y5', pyb.ExtInt.IRQ_RISING, pyb.Pin.PULL_DOWN, lambda l:print('INTERRUPÇÃO:', l))
SPI.write_readinto(write_buf, read_buf)
machine.Pin('X8', machine.Pin.ALT, alt=5) # give pin to SPI peripheral
machine.Pin('X8', machine.Pin.IN, machine.Pin.PULL_UP) # set MOSI as input pull-up

from machine import Pin
micropython.kbd_intr(ord('q'))
for i in range(5):
SPI.init(SPI.MASTER,ti=True, bits=16,)
data = [0xff, 0xff, 0xfd, 0x25]
ax = ubinascii.hexlify(bytes(data))



import micropython
import machine
import pyb
import utime
from machine import SPI


while True:
   p_out.low()
   time.sleep_us(1)
   p_out.high()
   time.sleep_us(1)

for i in range(999):
   rbuf = bytearray(1)
   byteToSend = 134
