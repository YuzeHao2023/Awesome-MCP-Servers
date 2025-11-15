import datetime
import os

def change_day(): 
  return datetime.timedelta(days=1) 

def change_time(): 
  return datetime.timedelta(minutes=1) 

now = datetime.datetime.now() 
commit_date = (now.replace(year=now.year-1) + change_day()) 

while commit_date < now: 
  commit_date = commit_date + change_day() 
  for i in range(2): 
    f = open('data.txt', 'a+') 
    commit_date = commit_date + change_time() 
    f.writelines(commit_date.isoformat() + '\n') 
    f.close()
    os.system('git add .') 
    os.system('git commit --date={time} -m "Update {time}"'.format(time=commit_date.isoformat()))

os.system('git push')