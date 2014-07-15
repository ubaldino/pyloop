void setup(){
  Serial.begin( 9600 );
  pinMode( 13 , 1 );
}
void loop(){
 
  if( Serial.available() ){
   char valor = (char) Serial.read();
   if( valor == 'a' ){
   		digitalWrite( 13 , 1 );
   }
   if( valor == 'e' ){
   		digitalWrite( 13 , 0 );
   }
 }
 
}