CREATE OR REPLACE PROCEDURE add_many_users(
    new_usernames VARCHAR(255)[],
    new_phones VARCHAR(255)[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    incorrect_data TEXT[] := ARRAY[]::TEXT[];
BEGIN
    IF array_length(new_usernames, 1) IS DISTINCT FROM
       array_length(new_phones, 1) THEN
        RAISE EXCEPTION 'Number of usernames and phones must match';
    END IF;

    FOR i IN 1..COALESCE(array_length(new_usernames, 1), 0)
    LOOP
        IF new_phones[i] ~ '^\+7[0-9]{10}$' THEN

            INSERT INTO contacts(username, phone)
            VALUES (new_usernames[i], new_phones[i]);

        ELSE

            incorrect_data := array_append(
                incorrect_data,
                'Username: ' || new_usernames[i] ||
                ', Phone: ' || new_phones[i]
            );

        END IF;
    END LOOP;

    RAISE NOTICE 'Incorrect data: %', incorrect_data;
END;
$$;


CALL add_many_users(
    ARRAY['Parasat', 'Alima', 'Beiba', 'Daniyar'],
    ARRAY['+71234567890', '123', '9876543210', 'abc']
);