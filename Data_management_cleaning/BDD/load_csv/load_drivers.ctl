load data
infile 'C:\Users\rayan\Desktop\ESILV\A4\Software_Engineering\BDD\drivers_clean.csv'
truncate
into table Drivers
fields terminated by ','
trailing nullcols
(
    driverId,
    driverRef,
    forename,
    surname,
    dob "to_timestamp(:dob, 'MM/DD/YYYY')",
    nationality,
    url
)