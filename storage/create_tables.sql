PRAGMA foreign_keys = OFF;

drop table if exists decks;
create table decks(
	id integer primary key,
);

drop table if exists deck_card_relation;
create table deck_card_relation(
	id integer primary key,
	d_id integer not null,
	c_id integer not null,	
	FOREIGN KEY(c_id) REFERENCES cards(id),
	FOREIGN KEY(d_id) REFERENCES decks(id)	
);


drop table if exists cards;
create table cards(
	id integer primary key, 
	q_id integer not null,
	FOREIGN KEY(q_id) REFERENCES qas(id)	
);

drop table if exists qas;
create table qas( -- question and answers
	id integer primary key,
	type integer not null, -- 0 for question, 1 for answer
	c_id integer not null,
	FOREIGN KEY(c_id) REFERENCES cards(id)	
);

drop table if exists information;
create table information(
	id integer primary key, 
	key varchar(30) not null,
	type varchar(50) not null, 
	value blob not null,
	qa_id integer not null,
	FOREIGN KEY(qa_id) REFERENCES qas(id)	
);

drop table if exists attributes;
create table attributes(
	id integer primary key,
	key varchar(30) not null,
	type varchar(50) not null, 
	value blob not null, 
	d_id integer not null,
	FOREIGN KEY(d_id) REFERENCES deck(id)
);

-- dummy question and dummy card
-- so that we can further create new cards
-- and qas because they each reference eachother
insert into qas(type, c_id) values(0, 0);
insert into cards(q_id) values(0);

PRAGMA foreign_keys = ON;
