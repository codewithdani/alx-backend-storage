-- Create a trigger to reset valid_email
-- only when the email has been changed

DELIMITER $$ ;
CREATE TRIGGER reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is updated
    IF NEW.email <> OLD.email THEN
        -- Reset valid_email to its default value or any logic you want
        SET NEW.valid_email = 0; -- 0 means not valid
    END IF;
END;$$
delimiter ;
