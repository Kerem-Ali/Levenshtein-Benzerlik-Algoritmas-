import numpy

def minimum(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=c and b<=a:
        return b
    elif c<=a and c<=b:
        return c

def max(a,b):
    if(a<b):
        return b
    else:
        return a


def normalize(X,size):
    if len(X)<size:
        fark=size-len(X)
        for i in range(fark):
            X=X+" "
    return X

def LevenshteinMesafesi(A,B):
    K=numpy.zeros( (len(A)+1 , len(B)+1) )
    
    A_len=len(A)
    B_len=len(B)

    for i in range(A_len+1):
        K[i][0]=i
    for i in range(B_len+1):
        K[0][i]=i
    
    silme=0
    ekleme=0
    yerdegistirme=0


    for i in range(1,A_len+1):
        for j in range(1,B_len+1):
            if A[i-1]==B[j-1]:
                K[i][j]=K[i-1][j-1]
            
            else:
                silme=K[i-1][j] +1
                ekleme=K[i][j-1]+1
                yerdegistirme=K[i-1][j-1]+1
                K[i][j]=minimum(silme,ekleme,yerdegistirme)
    return K[B_len][A_len]

if __name__=="__main__":
    
    kelime_1=input("1.kelimeyi girin: ")
    kelime_2=input("2.kelimeyi girin: ")

    max_len=max(len(kelime_1),len(kelime_2))

    

    kelime_1=normalize(kelime_1,max_len)
    kelime_2=normalize(kelime_2,max_len)

    mesafe=LevenshteinMesafesi(kelime_1,kelime_2)
    benzerlik_oran=(max_len-mesafe)/max_len

    print(f"'{kelime_1}' ve '{kelime_2}' arasındaki Levenshtein Mesafesi: {mesafe}\nBenzerlik Oranı:{benzerlik_oran}")
    

