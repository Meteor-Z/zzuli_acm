import json
import requests
from datetime import datetime,timedelta
import mysql.connector
 
def get_session(PTASession, JSESSIONID):
    session = requests.Session()
    cookies = {
        "PTASession": PTASession,
        "JSESSIONID": JSESSIONID
    }
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept-Language": "cn-ZH",
        "Accept": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    }
    session.cookies.update(cookies)
    session.headers.update(headers)
    return session

def get_competition_info(JSESSIONID):
    sql_command = 'SELECT PTA_session, Problem_Set FROM Competition_Info;'
    cursor.execute(sql_command)
    result=cursor.fetchone()
    if result:
        pta_value, set_value = result
        
    url = f"https://pintia.cn/api/problem-sets/{set_value}"
    session = get_session(pta_value, JSESSIONID)
    res = session.get(url)
    info_json = json.loads(res.text)

    start_time = info_json.get('exam').get('startAt')
    end_time = info_json.get('exam').get('endAt')
    
    bei_start_time=datetime.strptime(start_time,"%Y-%m-%dT%H:%M:%SZ")+timedelta(hours=8)
    bei_end_time=datetime.strptime(end_time,"%Y-%m-%dT%H:%M:%SZ")+timedelta(hours=8)
    
    sql_command="UPDATE Competition_Info SET Start_time=%s,End_time=%s;"
    params=(bei_start_time, bei_end_time)
    cursor.execute(sql_command,params)

###############################连接SQL数据库###############################
connection = mysql.connector.connect(
    host='zzulirank-mysql',
    port='3306',
    user='root',
    password='zzulirank_2024',
    database='PTA_Data',
)
cursor = connection.cursor()
###############################向数据库写入数据###############################
get_competition_info("E8119EF7C4CEBDA080224A3489FB962C")
###############################提交更改并断开连接###############################
connection.commit()
cursor.close()
connection.close()