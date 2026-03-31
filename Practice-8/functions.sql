-- 1. Функция поиска по паттерну
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_search text)
RETURNS TABLE(id int, user_name varchar, phone_number varchar) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.user_name, c.phone_number FROM contacts c
    WHERE c.user_name ILIKE '%' || p_search || '%' 
       OR c.phone_number ILIKE '%' || p_search || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Функция пагинации
CREATE OR REPLACE FUNCTION get_contacts_paged(p_limit int, p_offset int)
RETURNS TABLE(id int, user_name varchar, phone_number varchar) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.id, c.user_name, c.phone_number FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;