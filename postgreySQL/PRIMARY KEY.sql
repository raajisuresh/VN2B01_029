create table voter_list(
id serial primary key ,
name varchar(50)not nuLL
);

insert into voter_list(name)
values('abhi'),('bindu'),('cherry'),('durga');

alter table voter_list add column age int;
alter table voter_list add column constituency text;
alter table voter_list add column enroll_ID varchar(10);

insert into voter_list(NAME,age,constituency,enroll_id)
values('ali',18,'mydukur','BDY115021'),
('bharani',20,'PANYAM','QSR131021'),
('chaithanya',21,'NANDYAL','CVS134021');

update  VOTER_LIST set AGE =23 where NAME='DURGA'


select * from VOTER_LIST