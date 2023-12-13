# main_file.py
import schedule
import time
import subprocess

def job():
    # 执行 file1.py
    subprocess.run(["python", "competition_info.py"])
    # 执行 file2.py
    subprocess.run(["python", "student_score.py"])
    # 执行 file3.py
    subprocess.run(["python", "team_score.py"])

# 定义每隔15秒执行一次 job 函数
schedule.every(15).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)