import cx_Oracle  
  
conn = cx_Oracle.connect('pmsadm/pmsadm_1@10.111.43.112ß/sjzldb1')    
cursor = conn.cursor ()  
cursor.execute ("select 1from dual")  
row = cursor.fetchone ()  
print row[0]  
  
cursor.close ()  
conn.close ()  