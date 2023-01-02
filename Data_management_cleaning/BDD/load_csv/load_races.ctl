load data
infile 'C:\Users\rayan\Desktop\ESILV\A4\Software_Engineering\BDD\races_clean.csv'
truncate
into table Races
fields terminated by ','
trailing nullcols
(
    raceId,
    round,
    circuitId,
    name,
    datetime_ "to_timestamp(:datetime_, 'MM/DD/YYYY HH24:MI:SS')",
    url

)