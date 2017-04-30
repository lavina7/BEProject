int trigPin1 = 7;
int echoPin1 = 8;
int trigPin2 =2;
int echoPin2 = 4;
int ledPin1 = 5;
int ledPin2 = 6;
int ledPin3 = 9;
int ledPin4 = 10;
int duration2, distance2;
int red,green;
int duration1, distance1;
int x ;
int c;
String command;
String data;

void setup() {
  Serial.begin (9600);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
 
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4,OUTPUT);
}

void firstsensor();
void secondsensor();
void sensor1();
void sensor2();
void setColor(int red,int green)
  {
    #ifdef COMMON_CATHODE
    red = 255 - red;
    green = 255 - green;
    #endif
    analogWrite(ledPin1, red);
    analogWrite(ledPin2, green);
    
  }


void setColor1(int red,int green)
  {
    #ifdef COMMON_CATHODE
    red = 255 - red;
    green = 255 - green;
    #endif
    analogWrite(ledPin3, red);
    analogWrite(ledPin4, green);
    
  }

void firstsensor(){ // This function is for first sensor.
 digitalWrite (trigPin1, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin1, LOW);
  duration1 = pulseIn (echoPin1, HIGH);
  distance1 = (duration1/2) / 29.1;
   if (distance1 < 15 && distance1 >0 ) {  // Change the number for long or short distances.
   setColor1( 255,0);
   delay(50);
 } 
    else if (distance1 > 15 && distance1 >0){
      setColor1(0, 255);
      delay(50);    
  }
}
void secondsensor(){ // This function is for Second sensor.
  digitalWrite (trigPin2, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin2, LOW);
  duration2 = pulseIn (echoPin2, HIGH);
  distance2 = (duration2/2) / 29.1;
 
      if (distance2 < 15  ) {  // Change the number for long or short distances.
        setColor(255, 0);
        delay(50);
        
        } 
    else if (distance2 > 15 && distance2 >0 ){
    setColor(0, 255);
           delay(50); 
  } 
}

void sensor1(){ // This function is for first sensor.
  digitalWrite (trigPin1, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin1, LOW);
  duration1 = pulseIn (echoPin1, HIGH);
  distance1 = (duration1/2) / 29.1;
  if (distance1 < 15 && distance1 >0 ) {  // Change the number for long or short distances.
     Serial.print("a1"); 
  } 
    else if (distance1 > 15 && distance1 >0){
      Serial.print("a0");  
    }
    sensor2();
}
void sensor2(){ // This function is for first sensor.
  digitalWrite (trigPin2, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin2, LOW);
  duration2 = pulseIn (echoPin2, HIGH);
  distance2 = (duration2/2) / 29.1;
  if (distance2 < 15 && distance2 >0 ) {  // Change the number for long or short distances.
     Serial.println("b1");
   } 
    else if (distance2 > 15 && distance2 >0){
      Serial.println("b0");
    }
    delay(2000);
}



void loop() {
  
   sensor1();
   if(Serial.available()>0){
     data = Serial.readStringUntil('#');
    if(data =="light")
    {
      firstsensor();
      delay(50);
      secondsensor();
      delay(50);
     }
     else if(data =="lightoff")
    {
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, LOW);
      digitalWrite(ledPin3, LOW);
      digitalWrite(ledPin4,LOW);
    }
    else {
      Serial.println("Invalid data");
    }
    
  }
}
     


