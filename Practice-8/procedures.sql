-- 3. Процедура добавления или обновления (Upsert)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name varchar, p_phone varchar)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE user_name = p_name) THEN
        UPDATE contacts SET phone_number = p_phone WHERE user_name = p_name;
    ELSE
        INSERT INTO contacts (user_name, phone_number) VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- 4. Процедура удаления
CREATE OR REPLACE PROCEDURE delete_contact_proc(p_val varchar)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE user_name = p_val OR phone_number = p_val;
END;
$$;