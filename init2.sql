CREATE TABLE Hash_table(
  id_ INTEGER PRIMARY KEY ,
  link text not NULL UNIQUE ,
  rate integer ,
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

CREATE TABLE Word_list(
  id_ INTEGER PRIMARY KEY,
  word CHAR ,
  part char ,
  index_ blob,
  count int,
  note text
);
# word & part主键
CREATE UNIQUE INDEX index_word on Word_list (word);
CREATE UNIQUE INDEX index_link on Hash_table (link);
insert INTO Hash_table(link, include, type) VALUES ("http://www.bit.edu.cn", 1, 0);