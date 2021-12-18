create table experiment as select * from table1

select * from experiment

alter table experiment drop column children;

update experiment set member_age=55 where member_name='srinivas';

insert into experiment values('druv',30,'m','434133','KNL');
insert into experiment values('druva',30,'m','434133','KNL');
insert into experiment values('druva',30,'m','434133','KDP');
insert into experiment values('dhara',30,'m','434133','KDP');

begin;
insert into experiment values('dharani',31,'m','4343433','KKR');
insert into experiment values('druva',35,'m','434133','KDP');
rollback;

begin;
insert into experiment values('bhagya',30,'m','433533','KDP');
rollback;



begin;
insert into experiment values('druva',30,'m','433533','KDP');
commit;


begin;
insert into experiment values('arun',30,'m','433533','KDP');
commit;

alter table experiment rename to exampes;

alter table exampes rename to examples;

select * from examples;

select * from examples where member_name='druva';

select * from examples 
where member_name in (select member_name from examples 
where member_name='druva');



