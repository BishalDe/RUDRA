int echoPin=12,trigPin=10;
long duration;  
float distance;

void setup()

{
  Serial.begin(9600); 
  pinMode(trigPin,OUTPUT); 
  pinMode(echoPin,INPUT);
 }
void loop(){
  
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trigPin,LOW);
  
  duration=pulseIn(echoPin,HIGH);
   
  distance=duration*(0.017);
  Serial.print("Distance : ");
  Serial.print(distance);
  Serial.println(" cm ");
  delay(1000);
               
}
