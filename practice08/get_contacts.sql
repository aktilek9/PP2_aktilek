CREATE OR REPLACE FUNCTION get_contacts(
    page_number INT,
    page_size INT
)
RETURNS TABLE (
    id INT,
    username VARCHAR(255),
    phone VARCHAR(255)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.username, c.phone
    FROM contacts c
    ORDER BY c.id
    LIMIT page_size
    OFFSET (page_number - 1) * page_size;
END;
$$;

SELECT * FROM get_contacts(1, 3);