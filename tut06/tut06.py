#def regex_renamer():
import re
import os
import shutil

# Taking input from the user

print("1. Breaking Bad")
print("2. Game of Thrones")
print("3. Lucifer")

webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
season_padding = int(input("Enter the Season Number Padding: "))
episode_padding = int(input("Enter the Episode Number Padding: "))

web_name={1:"Breaking Bad",2:"Game of Thrones",3:"Lucifer"}

name_series=web_name[webseries_num]
path='tut06/wrong_srt/'+name_series+"/"

pathfile = "tut06/corrected_srt/"+name_series
    
if os.path.exists("tut06/corrected_srt/"):
    shutil.rmtree("tut06/corrected_srt/")
os.makedirs(pathfile)

for file in os.listdir(path):
    series_name=name_series
    value=re.findall(r'[0-9]+', file)
    
    if('720p' in file):
        title=""
    
    else:
    	temp=re.split('-', file)
    	temp= [s for s in temp if((".WEB") in s or ".HDTV" in s)][0]
    
    	title=re.split(".WEB|.HDTV",temp,maxsplit=2)[0].strip()
    
    if(len(value[0])<season_padding):
        season_number=(season_padding- len(value[0]))*"0"+value[0]
        
    else:
        p=-1*season_padding
        season_number=value[0][p:]
        
        
    if(len(value[1])<episode_padding):
        episode_number=(episode_padding- len(value[1]))*"0"+value[1]
        
    else:
        p=-1*episode_padding
        episode_number=value[1][p:]
        
        
    last=file[-4:]
    new_file_name=series_name+" Season "+season_number+" Episode "+episode_number
    
    if(len(title)>0):
        new_file_name=new_file_name+' '+title
    
    new_file_name+=last
    shutil.copyfile(os.path.join(path,file),os.path.join(pathfile,new_file_name))