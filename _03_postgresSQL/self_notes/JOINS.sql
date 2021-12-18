create table table1 as select * from family_details 
create table table2 as select * from children_detais 

select * from table1 cross join children_detais 

select * from table1

select * from table2


alter table table1 add column locality varchar(10);
update table1 set locality='HYD' where member_name='srinivas';
update table1 set locality='TPT' where member_name='padma';

alter table table2 add column locality varchar(10);
update table2 set locality='HYD' where child_name='surya';
update table2 set locality='HYD' where child_name='shivani';
update table1 set member_name='srinivas' where member_name='Srinivas';


select * from table1 inner join table2 
on table1.member_name=table2.father_name;


select * from table1 inner join table2 
on table1.gender=table2.gender;


select * from table2 inner join table1 
on table2.father_name=table1.member_name;


select * from table1 where member_name='srinivas'

select * from table1 right outer join table2 
on table1.locality=table2.locality;


select * from table2 right outer join table1 
on table1.locality=table2.locality;

select * from table1 left outer join table2 
on table1.locality=table2.locality;


select * from table1 cross join table2;

select * from table1 full outer join table2 
on table1.member_name=table2.father_name;

insert into table2(child_name,age,gender,father_name,contact_no)
values('sadana',15,'f','srini','6778686');

select * from table2 where father_name='srinivas' and gender='m'