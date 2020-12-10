--create table

CREATE TABLE random (
	rand_num	integer		NOT NULL,
	rand_word 	varchar(2)	NOT NULL);

--insert data
INSERT INTO random (rand_num, rand_word)
	SELECT trunc(73 + random()*15),
		chr(trunc(73 + random()*15)::int) || chr(trunc(73 + random()*15)::int)
	 FROM generate_series(1,50);

--Btree (default)
CREATE INDEX num ON random(rand_num);
--Btree
CREATE INDEX num_btree ON random USING btree(rand_num);

--GIN

CREATE EXTENSION btree_gin;

CREATE INDEX gin_num ON random USING GIN (rand_num);