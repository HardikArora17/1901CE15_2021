def get_memory_score(input_list):
    score=0

    not_valid_elemets=[]
    for i in input_list:
        if(type(i)!=int):
            not_valid_elemets.append(i)


    if(len(not_valid_elemets)>0):
        print("Please enter a valid input list")
        print("Invalid inputs detected : ",not_valid_elemets)
        return 

    
    elements_in_memory=[]

    for ele in input_list:
        if (ele in elements_in_memory):
            score+=1
        
        else:
            if  (len(elements_in_memory)>=5):
                del elements_in_memory[0]
                elements_in_memory.append(ele)

            else:
                elements_in_memory.append(ele)
                
    return score

