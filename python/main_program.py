import mysql.connector
import serial
import time

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="sql_username",
    password="your_sql_password",
    database="attendance_db",
)

cursor = db.cursor()

# Set up serial communication (ensure the COM port matches your setup here its COM6 which is gennerally the case)
serial_port = serial.Serial("COM6", 115200, timeout=1)

def process_ble_address(address):
    # Check if the scanned Bluetooth address exists in the attendance table
    query = "SELECT * FROM attendance WHERE bt_address = %s"
    cursor.execute(query, (address,))
    result = cursor.fetchone()

    if result:
        # If a match is found, update the attendance status to "Present"
        update_query = "UPDATE attendance SET status = 'Present' WHERE bt_address = %s"
        cursor.execute(update_query, (address,))
        db.commit()
        print(f"Attendance marked for {result[1]} with address {address}.")
    else:
        print(f"No match found for address: {address}")

try:
    while True:
        # Read data from the ESP32 serially
        if serial_port.in_waiting > 0:
            ble_address = serial_port.readline().decode().strip()
            print(f"Scanned BLE Address: {ble_address}")
            process_ble_address(ble_address)
            time.sleep(1)  # Delay for readability

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    # Clean up the database and serial connections
    cursor.close()
    db.close()
    serial_port.close()
