load data
infile 'C:\Users\rayan\Desktop\ESILV\A4\Software_Engineering\BDD\circuits_clean.csv'
truncate
into table Circuits
fields terminated by ','
trailing nullcols
(
    circuitId,
    circuitRef,
    name,
    location,
    country,
    lat "to_number(:lat, '99999D999999', 'NLS_NUMERIC_CHARACTERS=''.,''')",
    lng "to_number(:lng, '99999D999999', 'NLS_NUMERIC_CHARACTERS=''.,''')",
    alt,
    url

)