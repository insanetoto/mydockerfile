#!/bin/bash
mysqld_safe &
sleep 3
mysql -e "GRANT ALL PRIVILEGES ON *.* TO '$MYSQL_USER'@'%' identified by '$MYSQL_PASS' WITH GRANT OPTION;"
mysql -e "create database scores"
mysql -e "create table scores.name_score(name char(20) not null ,score int not null) DEFAULT CHARSET=utf8"
mysql -e "insert into scores.name_score values('tom',80),('jerry',89),('tossgirl',77)"
