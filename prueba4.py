import threading , time , serial , re

class SummingThread( threading.Thread ):
     def __init__( self , low , high ):
         super( SummingThread , self ).__init__()
         self.ser = serial.Serial( "COM49" , 9600 )
         self.low = low
         self.high = high
         self.total = 0

     def run( self ):
		while True:
			self.ser.write( 'U' )
			time.sleep( 3 )
			valor = 0
			if self.ser.inWaiting():
				valor = self.ser.read( self.ser.inWaiting() )
			valor = re.findall( "[0-9]+" , str( valor ) )
			print valor
			
			if int( valor[0] ) > 400:
				print "alerta"

thread1 = SummingThread( 0 , 50 )
thread1.start() # This actually causes the thread to run
#thread1.join()  
# At this point, both threads have completed
