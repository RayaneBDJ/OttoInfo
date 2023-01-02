load data
infile 'C:\Users\rayan\Desktop\ESILV\A4\Software_Engineering\BDD\results_clean.csv'
truncate
into table Results
fields terminated by ','
trailing nullcols
(
    resultId,
    raceId,
    driverId,
    constructorId,
    num_car,
    start_pos,
    final_pos,
    positionText,
    positionOrder,
    points,
    nbr_laps,
    time_total "to_number(:time_total, '99999D999999', 'NLS_NUMERIC_CHARACTERS=''.,''')",
    num_fastestLap,
    rank,
    fastestLapTime "to_number(:fastestLapTime, '99999D999999', 'NLS_NUMERIC_CHARACTERS=''.,''')",
    fastestLapSpeed "to_number(:fastestLapSpeed, '99999D999999', 'NLS_NUMERIC_CHARACTERS=''.,''')",
    statusId


)