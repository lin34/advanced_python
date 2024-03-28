-- CREATE TABLE USERS(
--     username TEXT NOT NULL PRIMARY KEY,
--     password NOT NULL,
--     email NOT NULL
-- )
INSERT INTO users (username, password, email)
VALUES ("joe", "joepass", "joe@yahoo.com");
SELECT password
FROM users
WHERE username is "joe"
DELETE FROM users
WHERE username = "mike"