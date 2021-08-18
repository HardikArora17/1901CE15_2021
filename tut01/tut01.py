
def meraki_helper(input_l):
    
    input_list=input_l
    sumy=0
    sumn=0

    for number in input_list:
        n=str(number)
        flag="Yes"
        
        for i in range(1,len(n)):
            if(abs(int(n[i-1])-int(n[i]))==1):
                continue
            else:
                flag="No"
                break
            
        if(flag=="Yes"):
            sumy+=1
            print(flag," - ",n,"is a Meraki Number")
            
        else:
            sumn+=1
            print(flag," - ",n,"is not a Meraki Number")
            
            
    print("the input list contains",sumy,"meraki numbers and",sumn,"non meraki numbers")
    

input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
meraki_helper(input)
