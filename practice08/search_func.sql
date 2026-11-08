CREATE OR REPLACE FUNCTION search(txt TEXT)
RETURNS TABLE (
    username VARCHAR(255),
    phone VARCHAR(255)
)
AS $$
BEGIN
    RETURN QUERY
        SELECT c.username, c.phone
        FROM contacts AS c
        WHERE c.username ILIKE '%' || txt || '%'
           OR c.phone ILIKE '%' || txt || '%';
END;
$$ LANGUAGE plpgsql;

SELECT * FROM search('MARAL');