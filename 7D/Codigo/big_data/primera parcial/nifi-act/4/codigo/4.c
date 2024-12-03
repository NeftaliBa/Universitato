// Librerías necesarias para MQTT, DHT11 y Adafruit Sensor
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <MQTT.h>

SYSTEM_THREAD(ENABLED);

// Definir el pin y tipo del sensor DHT11
#define DHTPIN D2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Configuración de MQTT
MQTT client("192.168.1.129", 1883, callback); // Usa la IP de tu broker

void callback(char *topic, byte *payload, unsigned int length)
{
    // Manejo de mensajes entrantes si es necesario
}

void setup()
{
    // Inicializa el puerto serial para mensajes de depuración
    Serial.begin(9600);

    // Iniciar la conexión MQTT y el sensor DHT11
    dht.begin();
}

void loop()
{
    if (client.connect("Niftali"))
    {
        Particle.publish("MQTT Status", "Conectado al broker MQTT", PRIVATE);
    }
    else
    {
        Particle.publish("MQTT Status", "No se pudo conectar al broker MQTT", PRIVATE);
    }
    delay(3000);

    String ip = WiFi.localIP();
    Particle.publish("mi ip", ip, PRIVATE);

    // Leer la temperatura
    float t = dht.readTemperature();

    // Publicar temperatura a Particle (para monitorear) y preparar para MQTT
    String tempString = String(t);
    Particle.publish("Temp °C", tempString, PRIVATE);

    // Publicar datos si estamos conectados a MQTT
    if (client.isConnected())
    {
        client.publish("Neftariable", tempString); // Publicar en el tema "Neftariable"
        Particle.publish("Datos publicados en MQTT: ", tempString, PRIVATE);
    }
    else
    {
        Particle.publish("Error: No conectado al broker MQTT", PRIVATE);
    }

    delay(2000);   // Ajusta el intervalo según sea necesario
    client.loop(); // Mantener la conexión MQTT
}
