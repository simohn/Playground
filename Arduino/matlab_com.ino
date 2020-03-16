const int ledPin = 23;

const int freq = 5000;
const int ledChannel = 0;
const int resolution = 8;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);

  ledcSetup(ledChannel, freq, resolution);
  ledcAttachPin(ledPin, ledChannel);
  
  Serial.begin(115200);
  delay(100);
}

int iBuffer;

void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available() > 0)
  {
    iBuffer = Serial.read();

    ledcWrite(ledChannel, iBuffer);
  }

  delay(10);
}
