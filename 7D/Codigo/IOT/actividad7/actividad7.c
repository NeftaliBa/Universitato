// Librería para manejar sensores DHT (temperatura y humedad).
#include <DHT.h>

// Este #include se añadió automáticamente por el IDE de Particle.
#include <Adafruit_Sensor.h>
// Activa el sistema multithread de Particle para ejecutar el código en paralelo con el sistema operativo.
SYSTEM_THREAD(ENABLED);

#define DHTPIN D2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
double t;
const double treshhold = 30.000000;
void setup()
{
    Serial.begin(9600);
    dht.begin();
}
void loop()
{
    t = dht.readTemperature();
    String TEMP = String(t);
    Particle.publish("Temp °C", TEMP, PRIVATE);
    if (t > treshhold)
    {

        Particle.publish("EmailTest", TEMP, PRIVATE);
        // Después de publicar la alerta, espera 1 minuto (60000 ms) antes de continuar.
        delay(30000);
    }
}
