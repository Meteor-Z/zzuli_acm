import mysql.connector

def get_team_score():
    sql_command = "UPDATE Team_Info SET part1 = (SELECT SUM(part1) FROM Student_Info WHERE Team_Info.TeamID = Student_Info.team_id)"
    cursor.execute(sql_command)

    sql_command = "UPDATE Team_Info SET part2 = (SELECT SUM(part2) FROM Student_Info WHERE Team_Info.TeamID = Student_Info.team_id)"
    cursor.execute(sql_command)

    sql_command = "UPDATE Team_Info SET part3 = (SELECT SUM(part3) FROM Student_Info WHERE Team_Info.TeamID = Student_Info.team_id)"
    cursor.execute(sql_command)

    sql_command = """
    UPDATE Team_Info
    SET score = CASE
    WHEN part1 > (SELECT standard1 FROM Competition_Info) AND part2 > (SELECT standard2 FROM Competition_Info) THEN part1 + part2 + part3
    WHEN part1 > (SELECT standard1 FROM Competition_Info) THEN part1 + part2
    ELSE part1
    END;
    """
    cursor.execute(sql_command)

    sql_command = "SET @temp = 0"
    cursor.execute(sql_command)
    
    sql_command = """
    UPDATE Team_Info
    SET rank = (@temp := @temp + 1)
    ORDER BY score DESC;
    """
    cursor.execute(sql_command)

    sql_command = "UPDATE Team_Info SET sum1 = 1000,sum2 = 1000,sum3 = 900"
    cursor.execute(sql_command)

connection = mysql.connector.connect(
    host='zzulirank-mysql',
    port='3306',
    user='root',
    password='zzulirank_2023',
    database='PTA_Data',
)
cursor = connection.cursor()

get_team_score()

connection.commit()
cursor.close()
connection.close()