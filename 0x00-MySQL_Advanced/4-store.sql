-- Create a trigger to decrease the quantity of
-- an item after adding a new order

-- Create a trigger named 'update_quantity_after_order'
CREATE TRIGGER update_quantity
AFTER INSERT ON orders FOR EACH ROW
    -- Update the quantity based on the items in the new order
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE item_id = NEW.item_id;
