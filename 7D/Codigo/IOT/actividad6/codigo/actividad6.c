// Author: Ramon J Betancourt
// Actual editor: Neftali Barrera Rodriguez

SYSTEM_THREAD(ENABLED); // Habilita el uso de hilos del sistema para que el dispositivo siga funcionando aunque no esté conectado a internet

#include "math.h"  // Incluye la librería matemática estándar para funciones como 'atof'
#include "stdio.h" // Incluye la librería estándar de entrada y salida para operaciones básicas

// Esta rutina se ejecuta una sola vez al iniciar el dispositivo
void setup()
{
    // Define una función que se puede llamar desde la nube de Particle
    // La función "TMS_2" será llamada desde el entorno de Particle Cloud, y ejecutará la función 'tms_2'
    Particle.function("TMS_2", tms_2);
}

float TMS; // Variable global para almacenar el multiplicador de tiempo (Time Multiplier Setting)

int tms_2(String command)
{
    // Convierte el comando de texto recibido en un valor flotante y lo asigna a la variable TMS
    TMS = atof(command);
    return TMS; // Devuelve el valor de TMS como entero para indicarle al entorno Particle que se ha procesado correctamente
}

// Esta rutina se ejecuta repetidamente en bucle
void loop()
{
    float Value = 5; // Valor inicial de la variable 'Value'
    // 'Value' se multiplica por el valor almacenado en 'TMS'
    Value = TMS * Value;
    String VALOR = String(Value); // Convierte el valor de 'Value' a una cadena de texto
    // Publica el valor actualizado de 'Value' en el tema 'VALOR' de Particle Cloud, de manera privada
    Particle.publish("VALOR", VALOR, PRIVATE);
    delay(2000); // Espera 2 segundos antes de repetir el ciclo
}
