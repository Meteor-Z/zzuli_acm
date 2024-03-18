import json
import requests
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

def get_problem_label(index):
    if index == "7-1":
        return "p11"
    elif index == "7-2":
        return "p12"
    elif index == "7-3":
        return "p13"
    elif index == "7-4":
        return "p14"
    elif index == "7-5":
        return "p15"
    elif index == "7-6":
        return "p16"
    elif index == "7-7":
        return "p17"
    elif index == "7-8":
        return "p18"
    elif index == "7-9":
        return "p21"
    elif index == "7-10":
        return "p22"
    elif index == "7-11":
        return "p23"
    
def s_to_m_s(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return "%02d:%02d" % (minutes, seconds)
    
def get_student_score_info(JSESSIONID):
    sql_command = 'SELECT PTA_session, Problem_Set FROM Competition_Info;'
    cursor.execute(sql_command)
    result=cursor.fetchone()
    if result:
        pta_value, set_value = result

    ###############################获取总人数计算页面遍历次数###############################
    url = f"https://pintia.cn/api/problem-sets/{set_value}/rankings?page=0&limit=20"
    session = get_session(pta_value, JSESSIONID)
    res = session.get(url)
    member_json = json.loads(res.text)
    print(member_json)

    sum_count = int(member_json.get("total"))
    if sum_count % 100 == 0:
        page_count = int(sum_count / 100)
    else:
        page_count = int(sum_count / 100) + 1
    
    label_tuple = member_json.get("commonRankings").get("labelByIndexTuple")
    ###############################遍历信息页面，生成信息列表###############################
    member_list = list()
    for i in range(page_count):
        url = f"https://pintia.cn/api/problem-sets/{set_value}/rankings?page={i}&limit=100"
        session = get_session(pta_value, JSESSIONID)
        res = session.get(url)
        member_json = json.loads(res.text)
        member_list = member_list + member_json.get("commonRankings").get("commonRankings")

    ###############################遍历信息列表，将考生信息导入数据库###############################
    for member_list_item in member_list:
        problem_info = dict()
        member_user_item = member_list_item.get("user")
        if 'studentUser' in member_user_item:
            stu_id = member_user_item.get("studentUser").get("studentNumber")
            rank = member_list_item.get("rank")
            slovingtime = member_list_item.get("solvingTime")
            score = member_list_item.get("totalScore")

            sql_command = "UPDATE Student_Info SET rank = %s, penalty = %s WHERE stu_id = %s"
            cursor.execute(sql_command, (rank, slovingtime, stu_id))

            problem_info["problemScores"] = member_list_item.get("problemScores")
            sloved=0
            for label in label_tuple:
                res_str=""
                if label in list(problem_info["problemScores"].keys()):
                    problem_score = problem_info["problemScores"][label]["score"]
                    itcnt = int(problem_info["problemScores"][label]["validSubmitCount"])
                    actime = int(problem_info["problemScores"][label]["acceptTime"])
                    acceptime = s_to_m_s(actime)
                    if problem_score!=0:
                        sloved = sloved+1
                        if itcnt==1:
                            res_str="+"
                        else:
                            res_str=f"+{itcnt-1}"
                    else:
                        if itcnt==0:
                            res_str="--"
                        elif itcnt==1:
                            res_str="-"
                        else:
                            res_str=f"-{itcnt-1}"
                else:
                    problem_score = 0
                    res_str="--"
                    acceptime="00:00"
        
                sql_command = "UPDATE Student_Info SET " + f"{get_problem_label(label)}" + " = %s WHERE stu_id = %s"
                cursor.execute(sql_command, (problem_score, stu_id))
                sql_command = "UPDATE Student_Info SET " + f"str{get_problem_label(label)}" + " = %s WHERE stu_id = %s"
                cursor.execute(sql_command, (res_str, stu_id))
                sql_command = "UPDATE Student_Info SET " + f"tme{get_problem_label(label)}" + " = %s WHERE stu_id = %s"
                cursor.execute(sql_command, (acceptime, stu_id))
                
            sql_command = "UPDATE Student_Info SET sloved = %s WHERE stu_id = %s"
            cursor.execute(sql_command, (sloved, stu_id))
        else:
            continue

###############################连接SQL数据库###############################
connection = mysql.connector.connect(
    host='s1.mcsol.cn',
    port='50420',
    user='root',
    password='zzulirank_2024',
    database='PTA_Data',
)
cursor = connection.cursor()
###############################向数据库写入数据###############################
get_student_score_info("E8119EF7C4CEBDA080224A3489FB962C")
sql_command = "UPDATE Student_Info SET rank = 999 WHERE rank IS NULL"
cursor.execute(sql_command)
###############################提交更改并断开连接###############################
connection.commit()
cursor.close()
connection.close()