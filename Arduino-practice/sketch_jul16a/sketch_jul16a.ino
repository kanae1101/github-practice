int score = 0;
void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
 score = score +1;
 Serial.println("Hello!");
 Serial.println(score);
 digitalWrite(13,HIGH);
 delay(1000);
 digitalWrite(13,LOW);
 delay(2000);
}
