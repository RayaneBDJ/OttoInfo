load data
infile 'C:\Users\rayan\Desktop\ESILV\A4\Software_Engineering\BDD\constructors_clean.csv'
truncate
into table Constructor
fields terminated by ','
trailing nullcols
(
    constructorId,
    constructorRef,
    name,
    nationality,
    url

)