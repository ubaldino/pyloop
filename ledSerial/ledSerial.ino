void setup(){
  Serial.begin( 9600 );
  pinMode( 13 , 1 );
}
void loop(){
 
  if( Serial.available() ){
   char valor = (char) Serial.read();
   if( valor == '0' ){
   		digitalWrite( 2 , 1 );
                digitalWrite( 3 , 1 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 1 );
   		digitalWrite( 6 , 1 );
                digitalWrite( 7 , 1 );
   		digitalWrite( 8 , 0 );             
   }
   if( valor == '1' ){
   		digitalWrite( 2 , 0 );
                digitalWrite( 3 , 1 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 0 );
   		digitalWrite( 6 , 0 );
                digitalWrite( 7 , 0 );
   		digitalWrite( 8 , 0 ); 
   }
      if( valor == '2' ){
   		digitalWrite( 2 , 1 );
                digitalWrite( 3 , 1 );
   		digitalWrite( 4 , 0 );
                digitalWrite( 5 , 1 );
   		digitalWrite( 6 , 1 );
                digitalWrite( 7 , 0 );
   		digitalWrite( 8 , 1 ); 
      }
      if( valor == '3' ){
   		digitalWrite( 2 , 1 );
                digitalWrite( 3 , 1 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 1 );
   		digitalWrite( 6 , 0 );
                digitalWrite( 7 , 0 );
   		digitalWrite( 8 , 1 ); 
      }
      if( valor == '4' ){
   		digitalWrite( 2 , 0 );
                digitalWrite( 3 , 1 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 0 );
   		digitalWrite( 6 , 0 );
                digitalWrite( 7 , 1 );
   		digitalWrite( 8 , 1 );
      } 
      if( valor == '5' ){
   		digitalWrite( 2 , 1 );
                digitalWrite( 3 , 0 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 1 );
   		digitalWrite( 6 , 0 );
                digitalWrite( 7 , 1 );
   		digitalWrite( 8 , 1 ); 
      }
      if( valor == '6' ){
   		digitalWrite( 2 , 0 );
                digitalWrite( 3 , 0 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 1 );
   		digitalWrite( 6 , 1 );
                digitalWrite( 7 , 1 );
   		digitalWrite( 8 , 1 ); 
      }
      if( valor == '7' ){
   		digitalWrite( 2 , 1 );
                digitalWrite( 3 , 1 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 0 );
   		digitalWrite( 6 , 0 );
                digitalWrite( 7 , 0 );
   		digitalWrite( 8 , 0 ); 
      }
      if( valor == '8' ){
   		digitalWrite( 2 , 1 );
                digitalWrite( 3 , 1 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 1 );
   		digitalWrite( 6 , 1 );
                digitalWrite( 7 , 1 );
   		digitalWrite( 8 , 1 ); 
      }
      if( valor == '9' ){
   		digitalWrite( 2 , 1 );
                digitalWrite( 3 , 1 );
   		digitalWrite( 4 , 1 );
                digitalWrite( 5 , 0 );
   		digitalWrite( 6 , 0 );
                digitalWrite( 7 , 1 );
   		digitalWrite( 8 , 1 ); 
 }
  }
  }
