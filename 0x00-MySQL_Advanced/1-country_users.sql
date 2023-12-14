-- Create table 'users' with the specified attributes

-- If the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS users (
    -- id, integer, auto increment and primary key, not null
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,

    -- email, string (255 characters), not null and unique
    email VARCHAR(255) NOT NULL UNIQUE,

    -- name, string (255 characters)
    name VARCHAR(255),

    -- country, enumeration of countries: US, CO and TN,
    -- never null (default US)
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

-- The script can be executed on any database
