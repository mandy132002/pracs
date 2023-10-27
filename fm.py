items=[1,2,3,4,1,3,4,1,2,4,1,2,3]

def hash(x):
    x=(6*x)+1
    return x%5

def binary(x):
    return bin(x)[2:]

hashed=list(map(hash,items))
binaries=list(map(binary,hashed))

def count_0s(x):
    final_out,temp_out = 0,0
    out=False
    
    for ch in x[::-1]:
        if ch=='1':
            out=True
            break
        
        temp_out+=1
        
    if out:
        final_out=temp_out
    return final_out
        
counts=list(map(count_0s,binaries))
print("number of uniques:",2**max(counts))