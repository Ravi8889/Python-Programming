#alphabhet_pos  =("The sun sets at twelve o' clock.")
#index = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
def aplha():
    alphabhet_pos  ="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    index = ("20, 8, 5, 19, 21, 14, 19, 5, 20, 19, 5, 20, 19, 1, 20, 20, 23, 5, 12, 22, 5, 15, 3, 12, 15, 3, 11")
    alpha1 =alphabhet_pos.split(',')
    d1= dict((key,value) for key,value in enumerate(alpha1,start=1))
    print(d1)

aplha()
alphabhet = aplha()

def replace_input(index_str):
    return " ".join([str(alphabhet[itr.upper()]) for itr in index_str if itr.upper() in alphabhet]) 
replace_input("20, 8, 5, 19, 21, 14, 19, 5, 20, 19, 5, 20, 19, 1, 20, 20, 23, 5, 12, 22, 5, 15, 3, 12, 15, 3, 11")
