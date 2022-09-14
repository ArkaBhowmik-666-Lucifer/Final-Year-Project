#include <DHT.h>
#include "WiFi.h"
#include <Wifi.h>
#include <FirebaseESP32.h>

int sensor_pin = 35;
int value ;

#include <addons/TokenHelper.h>
#include <addons/RTDBHelper.h>

#define WIFI_SSID "Joker"
#define WIFI_PASSWORD "Ysocreeus"

#define API_KEY "VqWBKewQ1HAH6pgtbU5Fnh7LCdV0bjGAM0hNJ7qZ"
#define DATABASE_URL "https://cropyeildprediction-b9f79-default-rtdb.firebaseio.com/"

#define DHTPIN 4
#define DHTTYPE DHT11   // DHT 11

#define rainAnalog 27
#define rainDigital 14

FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

DHT dht= DHT(DHTPIN, DHTTYPE);

void setup() {
//  Serial.begin(9600);
//  WiFi.mode(WIFI_STA);
//  WiFi.disconnect();
  Serial.begin(115200);
  delay(2000);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Serial.printf("Firebase Client v%s\n\n", FIREBASE_CLIENT_VERSION);

  config.api_key = API_KEY;

  config.database_url = DATABASE_URL;
  Firebase.begin(DATABASE_URL, API_KEY);

  Firebase.setDoubleDigits(5);
  delay(100);
  Serial.println("Setup done");
  Serial.println(F("DHTxx test!"));
  Serial.println("Soil Moisture:");
  delay(2000);
  pinMode(rainDigital,INPUT);
  dht.begin();
}

void loop() {
  delay(5000);
  Serial.println("scan start");
  int n = WiFi.scanNetworks();
  Serial.println("scan done");
  Serial.println("");

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);
  value= analogRead(sensor_pin);
  value = map(value,550,0,0,100);

  if (isnan(h) || isnan(t) || isnan(f) || isnan(value)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  else{
    if(Firebase.ready()){
      Firebase.setInt(fbdo, "/test/humidity", h);
      Firebase.setInt(fbdo, "/test/temperature", t);
      Firebase.setInt(fbdo, "/test/moisture", value);
    }
  }
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F\n"));//  Heat index: "));
  Serial.print("Moisture : ");
  Serial.print(value);
  Serial.println("%");
  delay(5000);

}
