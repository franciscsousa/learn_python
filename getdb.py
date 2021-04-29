import json
import connector
import MySQLdb 
    
class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

dbhost='172.16.106.150'
user=password='root'
database='totem_calcard'
mydict = create_dict()
select_employee = """select * from `totem_calcard`.`card` where PAYMENTCONFIRMPCHCOMPLETED = 1 AND PAYMENTCOMPLETED = 1 AND RENEGOTIATIONPROGRESS = 0 LIMIT 10;"""
db_connection = connector.connect(host=dbhost, user=user, password=password, database=database)
with db_connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute(select_employee)
    result = cursor.fetchall()

for row in result:
    mydict.add(row[0], ({"ID":row[1],"BALANCE":row[2],"CARDNUMBER":row[3],"CUSTOMER":row[4],"PAYSLIP":row[5],"PAYMENTRESULT":row[6],"PRINTSLIP":row[7],"PRINTSTATEMENTACCOUNT":row[8],"RELEASECARD":row[9],"RELEASECARDCOMPLETED":row[10],"REPRINTSLIP":row[11],"STATEMENTACCOUNT":row[12],"UTILIZATION_ID":row[13],"RENEGOTIATIONPROCESSCONFIRMED":row[14],"RENEGOTIATIONSIMULATE":row[15],"ACCOUNDID":row[15],"AGREEMENTID":row[16],"CARDID":row[17],"CPFCARRIER":row[18],"INTEGRATIONPAYMENTSAP":row[19],"PAYMENTCOMPLETED":row[20],"PAYMENTCONFIRMPCHCOMPLETED":row[21],"PAYMENTCONFIRMPCHRESULT":row[22],"REFIN":row[23]}))

#stud_json = json.dumps(mydict, ensure_ascii=False, indent=2, sort_keys=True)
stud_json = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
with open ('db_json.json', 'w') as saida:
    json.dump(stud_json, saida)


