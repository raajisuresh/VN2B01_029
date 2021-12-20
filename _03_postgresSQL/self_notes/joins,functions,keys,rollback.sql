/*TABLE1 CREATION*/

create table student_personnal(
roll_no varchar(30),
primary key(roll_no),    /*primary key*/
name varchar(50),
surname varchar(20),
father_name varchar(50),
mother_name varchar(30),
gender char
);

select * from student_personnal

/*Funtion for inserting values*/

create or replace function insert_fun(roll_no varchar(30),name varchar(50),surname varchar(20),
father_name varchar(50),mother_name varchar(30),gender char)
returns void as
$body$
begin
	insert into student_personnal 
	values(roll_no,name,surname,father_name,mother_name,gender);
end
$body$
language plpgsql;

/*inserting into table1 using function*/

select insert_fun('afsh2312','alia','A','arun','aruna','f');
select insert_fun('ad123ds3','balu','B','bharath','bharathi','m');
select insert_fun('fdaf2131','cherry','C','charan','chinni','f');
select insert_fun('fds234fd','dharsh','D','dharshan','dhurga','m');
select insert_fun('fdsf34fd','dharsh','D','dharshan','dhurga','m');

select * from student_personnal

/*Table2 creation*/

create table student_grades(
roll_no varchar(20),
school varchar(10),
grade char,
constraint fk_stud123
foreign key(roll_no)
references student_personnal(roll_no)
);

select * from student_grades

/*Funtion for inserting values*/

create or replace function insert_fun2(roll_no varchar(30),school varchar(10),grade char)
returns void as
$$
begin
	insert into  student_grades
	values(roll_no,school,grade);
end;
$$
language plpgsql;



select insert_fun2('afsh2312','AVR','f');
select insert_fun2('ad123ds3','SVR','A');
select insert_fun2('fdaf2131','GVR','f');
select insert_fun2('fds234fd','KSH','m');
select insert_fun2('fdsf34fd','ESC','m');

/*cross joining*/
select * from student_personnal cross join student_grades;

/*inner join*/
select * from student_personnal inner join student_grades 
ON student_personnal.roll_no=student_grades.roll_no;

/*left outer join*/
select * from student_personnal left outer join student_grades
on student_personnal.roll_no=student_grades.roll_no;

/*right outer join*/
select * from student_personnal right outer join student_grades
on student_personnal.roll_no=student_grades.roll_no;

/*full outer join*/
select * from student_personnal full outer join student_grades
on student_personnal.roll_no=student_grades.roll_no;

insert into student_personnal values('dsaf13122','Eshwar','E','Hari','Eshwari','m');