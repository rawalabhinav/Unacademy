import sys

def run_program(m):
    print('1 ' + str(m))
    sys.stdout.flush()
    r = int(input())
    if r == 0:
        return False
    elif r == 1:
        return True
    exit()

def find_memory_limit():
    start = 1
    end = 10**9 -1 
    mid  =  start + (end - start)//2   
    while end - start >= 2:
        call = run_program(mid)
        if call == True :                       
            start = mid      
        else :
            end = mid-1
        mid  =  start + (end - start)//2
    if start ==  end :
        return start
    elif run_program(end) :
        return end
    else :
        return start
    
print("2 " + str(find_memory_limit()))
    