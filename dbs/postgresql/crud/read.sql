--SELECT <columns // *>
--FROM <table>
-- WHERE <READ CONSTRAINS>
--ORDER <>  LIMIT <>

--Read all columns

--SELECT * FROM student;


--Read only name and email

--SELECT name, email FROM student

--read using where (specific)

--SELECT * FROM  student
--WHERE name = 'Akothee'


SELECT * FROM student 
ORDER BY name ASC
LIMIT 2
