files_main=open("data.txt","r")
files_user=open("user.txt","a")
files_agent=open("agent.txt","a")
dat=files_main.read()
lin=dat.split("\n")
lin=lin[:-1]
msg_txt=""

cu=0 # user

tmp_msg_u=""
tmp_msg_a=""

for wrd in lin:
  msg=wrd.split(",")
  msg_txt=",".join(msg[3:]) # message is obtained
  if msg[2]== " uSER ":
    print(1)
    tmp_msg_u= tmp_msg_u+ msg_txt
    if cu ==1:  # if previous was an agent
      files_agent.write(tmp_msg_a+"\n")
    tmp_msg_a=""
    cu=0
  
  if msg[2]== " aGENT ":
    print(2)
    tmp_msg_a= tmp_msg_a+ msg_txt

    if cu ==0:
      files_user.write(tmp_msg_u+"\n")
    tmp_msg_u=""
    cu=1

files_user.close()
files_agent.close()
files_main.close()
