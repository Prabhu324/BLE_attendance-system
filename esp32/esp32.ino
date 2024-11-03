#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>

BLEScan* pBLEScan;

void setup() {
  Serial.begin(115200);
  // Initialize BLE
  BLEDevice::init("ESP32_BLE_Scanner");
  
  // Create BLE scanner
  pBLEScan = BLEDevice::getScan(); // create new scan
  pBLEScan->setActiveScan(true); // Active scan uses more power, but gets results faster
  pBLEScan->setInterval(100); // Scan interval in ms
  pBLEScan->setWindow(99);     // Scan window in ms
}

void loop() {
  // Start scanning for 5 seconds
  BLEScanResults foundDevices = *pBLEScan->start(5);
  for (int i = 0; i < foundDevices.getCount(); i++) {
    BLEAdvertisedDevice device = foundDevices.getDevice(i);
    String btAddress = device.getAddress().toString().c_str();
    // Send the scanned Bluetooth address to the Serial port
    Serial.println(btAddress);
  }
  pBLEScan->stop();
  // Wait a bit before the next scan
  delay(10000); // Wait for 10 seconds before the next scan
}
