truncate table drivers;
truncate table results;

drop table drivers;
drop table results;
drop table circuits;
drop table races;
drop table constructor;


-------------------  DRIVERS ---------------------   


create table drivers( driverId  NUMBER not null,
                        driverRef varchar2(20),
                        forename varchar2(20),
                        surname varchar2(20),
                        dob date,
                        nationality varchar2(20),
                        url varchar2(100) );
                        
alter table drivers add constraint pk_drivers primary key (driverId);



-------------------  CIRCUITS  ---------------------       
                        
create table circuits ( circuitId number not null, 
                        circuitRef varchar2(20),
                        name varchar2(40),
                        location varchar2(40),
                        country varchar2(20),
                        lat decimal(12,6),
                        lng decimal(12,6),
                        alt integer,
                        url varchar2(100));
                        
alter table circuits add constraint pk_circuits primary key(circuitId);
                        
                        
                        
                        
                        
-------------------  RACES ---------------------                        
                        
                        
                        
create table races ( raceId number not null,
                     round number,
                     circuitId number not null,
                     name varchar2(40),
                     datetime_ date,
                     url varchar2(100));
                     
                     
alter table races add constraint pk_races primary key (raceId);
alter table races add constraint fk_races_circuits foreign key(circuitId) references circuits(circuitId);



-------------------  Constructor  ---------------------     
            
create table constructor ( constructorId number not null,
                            constructorRef varchar2(40),
                            name varchar2(40),
                            nationality varchar2(20),
                            url varchar2(200));
                            
alter table constructor add constraint pk_constructor primary key (constructorId);
                      
                      
-------------------  RESULTS  ---------------------     
                    
create table results( resultId NUMBER,
                      raceId NUMBER,
                      driverId NUMBER not null,
                      constructorId NUMBER,
                      num_car NUMBER,
                      start_pos INTEGER,
                      final_pos INTEGER,
                      positionText Varchar2(20),
                      positionOrder Varchar2(20),
                      points integer,
                      nbr_laps INTEGER,
                      time_total decimal(12,6),
                      num_fastestLap NUMBER,
                      rank number,
                      fastestLapTime decimal(12,6),
                      fastestLapSpeed decimal(12,6),
                      statusId integer );
                      
                      
alter table results add constraint pk_results primary key(resultId);

-- on supprime tous les drivers qui n'existent pas dan snotre table drivers 
DELETE FROM results WHERE driverId NOT IN (SELECT driverId FROM drivers);
alter table results add constraint fk_results foreign key(driverId) references drivers(driverId);
                      
                      
select count(*)
from (  select distinct driverid
        from results);

select count(*)
from (  select distinct driverid
        from drivers);
                                          
                        

select * from drivers;    
select * from results;
select * from races;
