-- Create a new database and table.
-- Create database hbtn_0d_usa.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select table
USE `hbtn_0d_usa`;
-- Create table states.
CREATE TABLE IF NOT EXISTS states(`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(256) NOT NULL);
