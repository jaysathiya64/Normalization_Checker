def file_read():
    file_r = open("input.txt","r")
    
    # No of Attribute
    att_list = (file_r.readline()).strip()
    att_list_split = att_list.split(',')
    
    file_list = file_r.readline()
    file_list_split = file_list.split(",")   #a->b, a->d
  
    left = []
    right = []

    for i in range(len(file_list_split)):
        data_left_right = file_list_split[i].split("->") #a->b
        
        data_left = data_left_right[0].split(" ")   #split a b-> c to a,b
        data_right = data_left_right[1].split(" ")  #split a b-> c,d to c,d

        left.append(data_left)
        right.append(data_right)
    file_r.close()
    return att_list_split,left, right

#Search Function
def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def find(list, val):
    for i in range(len(list)):
        str = ((val.strip('[')).strip(']')).strip("'")
        if list[i] == str:
            return i
    return -1

# function to generate all the sub lists
def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists

def super_key(att, left, right):
    dup_att = att.copy()
    left_length = len(left)
    right_length = len(right)
    non_prime = []
    prime = [] 
    for i in att:
        for j in range(0,left_length):
            for k in left[j]:
                if(i == k):
                    for m in range(0, right_length):
                        result = find(dup_att,str(right[m]))

                        if(result != -1):
                            dup_att.pop(result)
    
    return dup_att

def find_closure(att, left, right):
    closure = []
    att = ((att.strip('[')).strip(']')).strip("'")
    closure.append(att) 
    
    print(att)
    for i in range(0,len(left)):
        str = ''
        counter = 0
        for j in left[i]:
            str = str + j
            counter = counter + 1
        #print("asd")
        print("---"+ str + " " + att)
        if(str == att):
            for j in right[i]:
                closure.append(j)
                closure = closure + find_closure(j, left, right)
    
    return closure


def can_key(att,left,right,super_key):
    can_key = []
    len_super_key = len(super_key)
    len_left = len(left)
    len_right = len(right)
    
    set_super_key = sub_lists(super_key)
    len_set_super_key = len(set_super_key)
    
    closure = ''
    print(set_super_key)
    for i in range(0,len_set_super_key):
        if(len(set_super_key[i]) == 1):
            closure = find_closure(str(set_super_key[i]), left, right)
            #print(closure)
        elif(len(set_super_key[i]) != 0):
            closure = []
            val = ''
            #print(set_super_key[i])
            for j in set_super_key[i]:
                #print(set_super_key[i])
                val = val + ((((str(j).strip('[')).strip(']')).strip("'")).strip(","))
                print("As" +val)
                
                closure = closure + find_closure(str(j), left, right)
                print(find_closure(str(j), left, right))
                #print("as")
                #print(closure)
            closure = closure + find_closure(val, left, right)
            closure.remove(val)
        #print(str(set_super_key[i]) + " " + str(closure))
        counter = 0
        #print(sorted(list(set(closure))))
        #print(sorted(att))
        if(sorted(list(set(closure)))  == sorted(att)):
         #   print("as " + str)
            if(counter == 0):
                can_key.append(sorted(set_super_key[i]))
            else:
                flag = 0
                for j in range(0,len(can_key)):
                    if(set(set_super_key[i]).issubset(set(can_key[j]))):
                        flag = 1
                        can_key[j] = set_super_key[i]
                if(flag != 1):
                    can_key.append(set_super_key[i])
        #print(can_key)
    return can_key  

def check_prime(att,can_key,left,right):
    prime = []
    non_prime =[]
    for i in can_key:
        for j in i:
            prime.append(j)

    non_prime = set(att) - set(prime) 
    return  prime, non_prime

def check_2nf(can_key, left, right):
    for i in can_key:
        for j in i:
            for m in left:
                for n in m:
                    #print("as" +str(j) +" " +(str(m).strip('[')).strip(']').strip("'"))
                    if(j == (str(m).strip('[')).strip(']').strip("'")) and (len(i) != len(n)):
                        return 0 
    return 1
att,left,right = file_read()

sup_key = super_key(att,left,right) 
#print(super_key(att,left,right))
can_key = can_key(att,left,right,super_key(att,left,right))
print("Relation :- " + str(att))
print("Super Key For Relation :- " + str(super_key(att,left,right)))
print("Candidate Key for the given relation :- " + str(can_key))

if(check_2nf(can_key, left, right)):
    print("Relation is  in 2 Normal Form")
else:
    print("Relation is not in 2 Normal Form")
