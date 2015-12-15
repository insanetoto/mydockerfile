# -*- coding: UTF-8 -*-
import cx_Oracle
from datetime import date



user = "pmsadm"
password = "pmsadm_1"
con = None
dns = cx_Oracle.makedsn("10.111.43.112", "1521", "sjzldb1")


def get_conn():
    global con
    con = cx_Oracle.Connection(user, password, dns)
    return con


def close_conn():
    if con is not None:
        con.close()


def query(sql_string):
    global con
    i = 0
    j = 0
    filename = "zysdmx.sql"
    resultfile = open(filename, "w")
    resultfile.write("START TRANSACTION;\n")
    cursor = con.cursor()
    for result in cursor.execute(sql_string):
        i=i+1
        line = "insert into sdmx(HSDY, TQBH, YHBH, YHMC, JLDH, ZWYF, ZJDF, HJDL, DDDF, JFRL, JFXL, JBDF, LTDF, ZDSL, NWHD,ZYSK,DFSK,KZSNY,CBDJ,KTJJJ)\
        VALUES('"+str(result[1])+"',"  \
        +str(result[2])+","   \
        "'"+str(result[4])+"',"  \
        +"'"+str(result[5])+"',"  \
	    +str(result[6])+","  \
	    +str(result[3])+","  \
	    +str(result[7])+"," \
	    +str(result[8])+"," \
	    +str(result[9])+"," \
	    +str(result[10])+"," \
	    +str(result[11])+","\
	    +str(result[12])+"," \
	    +str(result[13])+"," \
	    +str(result[14])+"," \
	    +str(result[15])+"," \
	    +str(result[16])+"," \
	    +str(result[17])+"," \
	    +str(result[18])+"," \
	    +str(result[19])+"," \
	    +str(result[20]) \
	    +");\n"
        resultfile.write(line)
        j=j+1
        if i%10000==0:
	        resultfile.write("commit;\n")
	        resultfile.write("START TRANSACTION;\n")
	        resultfile.flush()
	        print str(i)+ " rows "

    resultfile.write("commit;\n")
    resultfile.close()
    cursor.close();


def main():
    con = get_conn()
    sql ='''	SELECT a.jgbm,a.dybm,b.tqbh,a.zwyf,a.yhbh,b.yhmc,a.jldh,a.ysdf,a.hjdl,a.dddf,a.jfrl,a.jfxl,
a.jbdf,a.ltdf,a.zdsl,a.nwhd,a.zysk,a.dfsk,a.kzsny,a.cbdj,a.ktjjj FROM(
(SELECT jgbm AS jgbm,dybm AS dybm,zwyf AS zwyf,yhbh AS yhbh,jldh AS jldh,
nvl(SUM(ysdf),0) AS ysdf,
nvl(SUM(CASE WHEN djlb =0 AND ywlb <> 8 THEN hjdl END ),0) AS hjdl,
nvl(SUM(CASE WHEN djlb =0 THEN ysdf END ),0) AS dddf,
nvl(SUM(CASE WHEN djlb =3 THEN jfrl END ),0) AS jfrl,
nvl(SUM(CASE WHEN djlb =3 THEN jfxl END ),0) AS jfxl,
nvl(SUM(CASE WHEN djlb =3 THEN ysdf END ),0) AS jbdf,
nvl(SUM(CASE WHEN djlb =4 THEN ysdf END ),0) AS ltdf,
nvl(SUM(CASE WHEN djlb =2 THEN ysdf END ),0) AS zdsl,
nvl(SUM(CASE WHEN djlb =1 THEN ysdf END ),0) AS nwhd,
nvl(SUM(CASE WHEN djlb =5 THEN ysdf END ),0) AS zysk,
nvl(SUM(CASE WHEN djlb =6 THEN ysdf END ),0)AS dfsk,
nvl(SUM(CASE WHEN djlb =7 THEN ysdf END ),0) AS kzsny,
nvl(SUM(CASE WHEN djlb =12 THEN ysdf END ),0) AS cbdj,
nvl(SUM(CASE WHEN djlb =13 THEN ysdf END ),0) AS ktjjj
FROM pmsadm.zw_ljfysmx_14_2015@sc_link  WHERE jgbm ='14' and zwyf=201512
GROUP BY jgbm,dybm,zwyf,yhbh,jldh)a
LEFT JOIN
(select dybm,tqbh,yhbh,yhmc from pmsadm.yh_jbxx_14@sc_link)b
ON a.yhbh =b.yhbh )
    '''
    query(sql)
    close_conn()

if __name__ == '__main__':
    main()
