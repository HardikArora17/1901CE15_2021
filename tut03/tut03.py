import os

os.mkdir('tuts_2021/tut03/output_by_subject')
os.mkdir('tuts_2021/tut03/output_individual_roll')

i=0
roll_no={}
sub_no={}


with open('tuts_2021/tut03/regtable_old.csv', 'r') as f:
    results = []
    for line in f:
            words = line.split(',')
            if(i==0):
                i+=1
                continue

            if(words[0] not in roll_no.keys()):
                roll_no[words[0]]=[]
                roll_no[words[0]].append((words[1],words[3],words[-1].replace("\n","")))
            else:
                roll_no[words[0]].append((words[1],words[3],words[-1].replace('\n','')))
           
            if(words[3] not in sub_no.keys()):
                sub_no[words[3]]=[]
                sub_no[words[3]].append((words[0],words[1],words[-1].replace("\n","")))
            else:
                sub_no[words[3]].append((words[0],words[1],words[-1].replace('\n','')))



for r,v in roll_no.items():
    f=open("tuts_2021/tut03/output_individual_roll/"+r+".csv",'w')
    fixed_line="roll_no,register_sem,subno,sub_type\n"
    f.write(fixed_line)

    for item in v:
        a=r+","+item[0]+","+item[1]+","+item[2]+"\n"
        f.write(a)

    f.close()

for r,v in sub_no.items():
    f=open("tuts_2021/tut03/output_by_subject/"+r+".csv",'w')
    fixed_line="roll_no,register_sem,subno,sub_type\n"
    f.write(fixed_line)

    for item in v:
        a=item[0]+","+item[1]+","+r+","+item[2]+"\n"
        f.write(a)

    f.close()