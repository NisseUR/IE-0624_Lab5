#include <Arduino_LSM9DS1.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  Serial.println("IMU initialized!");
}

void loop() {
  float accelerationX, accelerationY, accelerationZ;
  float gyroX, gyroY, gyroZ;

  if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
    IMU.readAcceleration(accelerationX, accelerationY, accelerationZ);
    IMU.readGyroscope(gyroX, gyroY, gyroZ);

    Serial.print("Acceleration: ");
    Serial.print(accelerationX);
    Serial.print(", ");
    Serial.print(accelerationY);
    Serial.print(", ");
    Serial.print(accelerationZ);
    Serial.print(" | Gyro: ");
    Serial.print(gyroX);
    Serial.print(", ");
    Serial.print(gyroY);
    Serial.print(", ");
    Serial.println(gyroZ);
  }
  delay(100);
}
