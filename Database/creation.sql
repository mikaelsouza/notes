CREATE TABLE category (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name TEXT NOT NULL
)

CREATE TABLE note (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cat_id INT NOT NULL references category(id),
    title TEXT NOT NULL,
    data TEXT NOT NULL,
    deleted BOOL NOT NULL
)

INSERT INTO category (name) VALUES ('Sem Categoria')