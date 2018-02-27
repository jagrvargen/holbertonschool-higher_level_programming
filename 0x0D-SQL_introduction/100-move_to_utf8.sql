-- Converts hbtn_0c_0 database to UTF8.
-- Convert hbtn_0c_0 to UTF8.
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert first_table to UTF8.
ALTER TABLE `first_table` CHARACTER SET = utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert name field in first_table to UTF8.
ALTER TABLE `first_table` CHANGE `name` `name` VARCHAR(256) CHARACTER SET\
      utf8mb4 COLLATE utf8mb4_unicode_ci;
