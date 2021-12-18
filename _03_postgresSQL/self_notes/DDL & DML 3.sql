create table family_details(
Member_name varchar(30),
Age int,
Gender char,
Children int
);

alter table family_details add column contact_no varchar(10);
alter table family_details rename column age to Member_age;

insert into family_details(Member_name,member_Age,gender,children,contact_no)
values('Srinivas',50,'m',2,'6758768'),
		('padma',45,'f',2,'5765878');
	
select * from family_details 
		
create table children_detais(
Child_name varchar(30),
Age int,
Gender char
);

insert into children_detais(child_name,age,gender,father_name,contact_no)
values('surya',30,'m','srinivas','5765765'),
	('shivani',28,'f','srinivas','5765767');

alter table children_detais add column father_name varchar(30);
alter table children_detais add column contact_no varchar(10);

