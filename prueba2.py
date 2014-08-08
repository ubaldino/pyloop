


import serial , sys , time , re
ser = serial.Serial( port="/dev/ttyUSB0" , baudrate=9600 )

print "ingrese RFID"
codigos = { "0700A167C001" : "benji" , "0700A16ED41C" : "rafo gates" }

while( True ):
  if ser.inWaiting():
    a = ser.read( ser.inWaiting() )
    capturado = re.findall( "\w+" , a )
    if len( capturado ) > 0:
      valor = str( capturado[0] )
      if len( valor ) == 12:
        print codigos[ valor ]
  time.sleep( 0.03 )
