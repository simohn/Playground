int ledPin = 23;
int buttonPin = 21;

bool ret_buttonPin = LOW;

void setup() {
  // put your setup code here, to run once:

  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  
  Serial.begin(115200);
  delay(100);

  Serial.println("Setup done");
}

void loop() {
  // put your main code here, to run repeatedly:

  ret_buttonPin = digitalRead(buttonPin);

  if(ret_buttonPin)
  {
    Serial.println("Button pin status: true");
  }
  else
  {
    Serial.println("Button pin status: false");
  }

  digitalWrite(ledPin, HIGH);
  delay(500);

  digitalWrite(ledPin, LOW);
  delay(500);
}
