DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  assignee VARCHAR(255),
  duration INT,
  completed BOOLEAN,
  user_id INT REFERENCES users(id)
);

INSERT INTO tasks (description, assignee, duration, completed)
VALUES ('get milk', 'Zsolt', 5, False);
INSERT INTO tasks (description, assignee, duration, completed)
VALUES ('Walk the hedgehog', 'John', 15, True);
INSERT INTO tasks (description, assignee, duration, completed)
VALUES ('Cook dinner', 'Juan', 30, False);