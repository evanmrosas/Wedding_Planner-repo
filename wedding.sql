
        
CREATE TABLE  gifts
(
  id         INT          NOT NULL AUTO_INCREMENT,
  gift_name  VARCHAR(255) NOT NULL,
  user_id    INT          NOT NULL,
  created_at timestamp    NOT NULL DEFAULT NOW(),
  updated_at timestamp    NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id)
);

CREATE TABLE budgets
(
  id         INT          NOT NULL AUTO_INCREMENT,
  item_name  VARCHAR(255) NOT NULL,
  price      FLOAT        NOT NULL,
  user_id    INT          NOT NULL,
  created_at timestamp    NOT NULL DEFAULT NOW(),
  updated_at timestamp    NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id)
);

CREATE TABLE guests
(
  id         INT       NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(255)   NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  attending  BOOLEAN   NOT NULL,
  user_id    INT       NOT NULL,
  created_at timestamp NOT NULL DEFAULT NOW(),
  updated_at timestamp NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id)
);

CREATE TABLE users
(
  id         INT          NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name  VARCHAR(255) NOT NULL,
  email      VARCHAR(255) NOT NULL,
  password   VARCHAR(255) NOT NULL,
  created_at timestamp    NOT NULL DEFAULT NOW(),
  updated_at timestamp    NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id)
);

CREATE TABLE weddings
(
  id             INT          NOT NULL AUTO_INCREMENT,
  partner_name_1 VARCHAR(255) NOT NULL,
  partner_name_2 VARCHAR(255) NOT NULL,
  location       VARCHAR(255) NOT NULL,
  date           DATE         NOT NULL,
  reception      VARCHAR(255) NOT NULL,
  total_guest    INT          NOT NULL,
  notes          TEXT         NOT NULL,
  user_id        INT          NOT NULL,
  created_at     timestamp    NOT NULL DEFAULT NOW(),
  updated_at     timestamp    NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id)
);

ALTER TABLE weddings
  ADD CONSTRAINT FK_users_TO_weddings
    FOREIGN KEY (user_id)
    REFERENCES users (id);

ALTER TABLE budgets
  ADD CONSTRAINT FK_users_TO_budgets
    FOREIGN KEY (user_id)
    REFERENCES users (id);

ALTER TABLE guests
  ADD CONSTRAINT FK_users_TO_guests
    FOREIGN KEY (user_id)
    REFERENCES users (id);

ALTER TABLE  gifts
  ADD CONSTRAINT FK_users_TO_gifts
    FOREIGN KEY (user_id)
    REFERENCES users (id);