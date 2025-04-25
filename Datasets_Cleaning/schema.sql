


state_id : int(2)
state_name : str(40)
state_type : enum("S","U")
capital : (25)


CREATE TABLE `if0_38832826_logistics_network`.`state` ( `state_id` INT(5) NOT NULL AUTO_INCREMENT , `state_name` TEXT NOT NULL , `state_type` ENUM('State','Union Territory') NOT NULL , `capital` TEXT NOT NULL , PRIMARY KEY (`state_id`)) ENGINE = MyISAM;



district 

district_id 
district_name  
district_capital null ? 
state_id


CREATE TABLE `if0_38832826_logistics_network`.`district` ( `district_id` SMALLINT NOT NULL AUTO_INCREMENT , `district_name` TEXT NOT NULL , `state_id` TINYINT NOT NULL , PRIMARY KEY (`district_id`)) ENGINE = MyISAM COMMENT = 'This table is for storing District dimension.';

city

city_id
city_name
latitude
longitude
altitude
district_id
state_id


city-A city-C 
......
