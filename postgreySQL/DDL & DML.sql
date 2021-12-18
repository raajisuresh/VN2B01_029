create table grades(

name varchar(30),
roll_no varchar(15),
marks integer

);

delete from grades where name='honey';

select * from grades

insert into grades(name,roll_no,marks)
values('yash','11x1',78),
	('suresh','11x2',81);

select * from grades

update grades set marks=85 where name='yash';

insert into grades(name,roll_no,marks)
values('honey','11r33',75),
	   ('sravya','10x55',86),
	     ('siva','112e',88);

alter table grades add column age int;

insert into grades(name, roll_no,marks,age)
values('hari','11w23',79,21),
('abhi','11fr33',88,20);

update grades set age=20 where name='siva';
update grades set age=21 where name='suresh';
update grades set age=20 where name='yash';
update grades set age=20 where name='sravya';
update grades set age=20 where name='honey';


select * from grades
