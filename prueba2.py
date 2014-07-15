import serial , sys , time

ser = serial.Serial( port="/dev/ttyUSB0" , baudrate=9600 )

#print sys.argv[1]
"""
if sys.argv[1] == "on":
  ser.write( 'a' )

if sys.argv[1] == "off":
  ser.write( 'b' )
"""

while( True ):
    ser.write( 'a' )
    time.sleep( .5 )
    ser.write( 'b' )
    time.sleep( .5 )
