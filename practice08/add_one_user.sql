CREATE OR REPLACE PROCEDURE add_user(
    new_username VARCHAR(255),
    new_phone VARCHAR(255)
)
AS $$
BEGIN
    INSERT INTO contacts(username, phone)
    VALUES (new_username, new_phone)
    ON CONFLICT (username)
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$ LANGUAGE plpgsql;

CALL add_user('Dj', '+77716471414');