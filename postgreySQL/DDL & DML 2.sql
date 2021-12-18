create table rankers as select * from grades;

alter table rankers add column grade varchar(5);

update rankers set grade='A' where name='yash';

select * from rankers;

update rankers set grade='A1' where name='honey';

delete from rankers where name='abhi';


