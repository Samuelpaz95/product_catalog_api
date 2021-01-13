use catalog_db;
DROP PROCEDURE IF EXISTS GetNotifications;
DELIMITER //
CREATE PROCEDURE GetNotifications (IN UserID INT(11))
BEGIN
    SELECT 
        N.id,
        U.user_ID,
        N.responsable_id,
        RU.full_name AS responsable_full_name,
        RU.email AS responsable_email,
        N.action,
        UF.field_name
    FROM (
        SELECT user_ID 
        FROM user 
        WHERE user_ID = UserID
    ) U
    INNER JOIN 
        noti_to_users NTU 
    ON 
        U.user_ID = NTU.user_id
    INNER JOIN 
        notifications N 
    ON 
        NTU.noti_id = N.id
    INNER JOIN (
        SELECT 
            user_ID,
            full_name,
            email 
        FROM user
    ) RU 
    ON 
        N.responsable_id = RU.user_ID
    INNER JOIN 
        action_in_notifications AN 
    ON 
        N.id = AN.noti_id
    INNER JOIN 
        updated_fields UF 
    ON 
        AN.field_id = UF.field_id;
END//

DELIMITER ;