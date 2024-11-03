-- Step 1: Create the database
CREATE DATABASE attendance_db;

-- Step 2: Use the database
USE attendance_db;

-- Step 3: Create the attendance table
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    bt_address VARCHAR(17) NOT NULL UNIQUE,
    status VARCHAR(10) DEFAULT 'Absent',
    last_marked TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

