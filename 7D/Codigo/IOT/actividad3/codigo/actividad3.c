// This #include statement was automatically added by the Particle IDE.
#include <Adafruit_Sensor.h>

// This #include statement was automatically added by the Particle IDE.
#include <DHT.h>


SYSTEM_THREAD(ENABLED);

#define DHTPIN 2     // Pin digital al que está conectado el sensor
#define DHTTYPE DHT11   // Tipo de sensor DHT

DHT dht(DHTPIN, DHTTYPE);

double t;   // Temperatura en °C
double f;   // Temperatura en °F
double h;   // Porcentaje de humedad
double hic; // Índice de calor

void setup() {
  Serial.begin(9600);

  dht.begin();

  // Publicar variables en el servidor de Particle
  Particle.variable("TEMP", t);  // Enviar la temperatura al servidor de Particle
  Particle.variable("HUM", h);   // Enviar la humedad al servidor de Particle
}

void loop() {
  delay(2000);  

  h = dht.readHumidity();         // Leer la humedad
  t = dht.readTemperature();      // Leer la temperatura en °C
  f = dht.readTemperature(true);  // Leer la temperatura en °F

  // Calcular el índice de calor en °C
  hic = dht.computeHeatIndex(t, h, false);

}