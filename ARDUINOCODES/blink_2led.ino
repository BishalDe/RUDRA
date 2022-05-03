int led1=10,led2=12;
void setup()
{
  pinMode(led1, OUTPUT);
  pinMode(led2,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(led1, HIGH);
  delay(1000); 
  Serial.println("1st led is glowing");
  digitalWrite(led1, LOW);
  delay(1000); 
  digitalWrite(led2, HIGH);
  delay(1000); 
  Serial.println("2st led is glowing");
  digitalWrite(led2, LOW);
  delay(1000); 
}
