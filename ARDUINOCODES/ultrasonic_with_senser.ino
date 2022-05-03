int echoPin=12,trigPin=13;
long duration;  
float distance;

void setup()
{  pinMode(trigPin,OUTPUT); 
  pinMode(echoPin,INPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
    Serial.begin(9600);
    
}

void loop()
{
  
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trigPin,LOW);
  
  duration=pulseIn(echoPin,HIGH);
   
  distance=duration*(0.017);
  
  if(distance>100){
    digitalWrite(11,LOW);
    int key1=Serial.read();
    if (key1 == 'w'){     
        digitalWrite(5, LOW);
        digitalWrite(6, HIGH);
        digitalWrite(9, LOW);
        digitalWrite(10, HIGH);
        Serial.println("moving FORWARD ");

    }
    
    else if (key1 == 's'){
        digitalWrite(5, HIGH);
        digitalWrite(6, LOW);
        digitalWrite(9, HIGH);
        digitalWrite(10, LOW);
        Serial.println("moving BACKWARD ");
 

    }
    
    else if (key1 == 'd'){
      digitalWrite(5, LOW);
        digitalWrite(6, HIGH);
        digitalWrite(10, LOW);
        digitalWrite(9, LOW);
      Serial.println("moving RIGHT ");
    }
    else if (key1 == 'a'){
      digitalWrite(5, LOW);
        digitalWrite(6, LOW);
        digitalWrite(10, HIGH);
        digitalWrite(9, LOW);
      Serial.println("moving LEFT ");
    }
    else if (key1 == ' '){
        digitalWrite(11,HIGH);
      digitalWrite(5, LOW);
        digitalWrite(6, LOW);
        digitalWrite(10, LOW);
        digitalWrite(9, LOW);
        Serial.println(" STOPPED ");
    }
  }
  else{ digitalWrite(11,HIGH);
        digitalWrite(5, LOW);
        digitalWrite(6, LOW);
        digitalWrite(10, LOW);
        digitalWrite(9, LOW);
        Serial.println(" STOPPED ");
  }
}
