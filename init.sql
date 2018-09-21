CREATE TABLE Hash_table(
  id_ INTEGER PRIMARY KEY ,
  link text not NULL UNIQUE ,
  include blob NOT NULL ,
  weight DECIMAL(10,5),
  updateTime datetime ,
  type int DEFAULT 0
);

CREATE TABLE Webpage_info(
  id_ INTEGER PRIMARY KEY,
  linkId int NOT NULL UNIQUE,
  page text,
  title text,
  content text,
  total int,
  note text,
  FOREIGN KEY (linkId) REFERENCES Hash_table(id_)
);

CREATE TABLE word_list(
  id_ INTEGER PRIMARY KEY,
  word CHAR ,
  part char ,
  index_ blob,
  count int,
  note text
);
# word & part主键
insert INTO Hash_table(link, include, type) VALUES ("http://www.bitren.com", 1, 0);