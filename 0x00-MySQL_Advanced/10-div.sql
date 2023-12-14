-- Create a function SafeDiv to divide the
-- first number by the second or return 0
-- if the second number is equal to 0


-- Create the function SafeDiv
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    -- Check if the second number is equal to 0
    IF b = 0 THEN
        RETURN 0;
    ELSE
        -- Return the result of the division
        RETURN a / b;
    END IF;
END //
DELIMITER ;
