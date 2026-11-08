CREATE OR REPLACE PROCEDURE delete_contact(
    p_username VARCHAR(255) DEFAULT NULL,
    p_phone VARCHAR(255) DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_username IS NULL AND p_phone IS NULL THEN
        RAISE EXCEPTION 'You must provide username or phone';

    ELSIF p_username IS NOT NULL AND p_phone IS NOT NULL THEN
        DELETE FROM contacts
        WHERE username = p_username OR phone = p_phone;

    ELSIF p_username IS NOT NULL THEN
        DELETE FROM contacts
        WHERE username = p_username;

    ELSE
        DELETE FROM contacts
        WHERE phone = p_phone;
    END IF;

    RAISE NOTICE 'Contact deletion completed';
END;
$$;

CALL delete_contact(p_username := 'Parasat');