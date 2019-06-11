class Pairs:
    def __init__(self, left, right):        #konstruktor
        self.left = left
        self.right = right

    def __repr__(self):                     #printa parove
         return "%s --> %s " % (self.left, self.right)
    
    def GetLeftPairLen(self):               #vraca duzinu lijeve strane funkcionalne ovisnosti
        cnt = 0
        for i in self.left:
            if(i.isalpha()):
                cnt = cnt + 1
        return cnt
        
    def GetRightPairLen(self):              #vraca duzinu desne strane funkcionalne ovisnosti
        cnt = 0
        for i in self.right:
            if(i.isalpha()):
                cnt = cnt + 1
        return cnt        

    def GetListLen(self, lst):
        cnt = 0
        for i in lst:
            if i.isalpha():
                cnt += 1
        return cnt

    def CheckIfRightSubsetLeft(self):       #gleda je li desna strana podskup lijeve
        cnt = 0
        for i in self.right:
            if i in self.left and i.isalpha():
                cnt = cnt + 1
        if cnt == self.GetRightPairLen():
            return 1
        return 0

    def CheckIfSuperKey(self, key):         #gleda je li kljuc podskup lijeve strane
        cnt = 0
        cnt1 = 0
        for i in key:
            for j in i:
                if j in self.left and j.isalpha():
                    cnt = cnt + 1
            if cnt == len(i)-(len(i)/2 - 1):
                cnt1 += 1
            cnt = 0
        if cnt1 == len(key):
            return 1
        return 0

    def CheckIfLeftSubsetRight(self):       #gleda je li lijeva strana podskup desne
        cnt = 0
        for i in self.left:
            if i in self.right and i.isalpha():
                cnt = cnt + 1
        if cnt == self.GetLeftPairLen():
            return 1
        return 0

    def CheckIfTrivial(self):               #provjerava trivijalnost na osnovu funckije CheckIfRightSubsetLeft
        if self.CheckIfRightSubsetLeft():
            return 1
        return 0

    def CheckIfBasicAttribute(self, key):   #gleda je li desna strana osnovni atribut (dio kljuca)
        cnt = 0
        for j in key:
            for i in self.right:
                if i in j and i.isalpha():
                    cnt = cnt + 1
            if len(i) == cnt:
                return 1
            cnt = 0
        return 0

    def Extract (self):                     #izvlaci ovisnosti i sprema ih u listu u A,B,C formatu
        lst = []
        string = ''
        for i in self.left:
            if i.isalpha():
                string += i
                lst.append(string)
                string = ''
        for i in self.right:
            if i.isalpha():
                string += i
                lst.append(string)
                string = ''
        return lst

class Fmin: 
    def __init__ (self, FminLst = []):      #konstruktor
        self.FminLst = FminLst

    def __repr__(self):                     #printa listu parova
         return (self.FminLst)

    def __iter__(self):
        pass 

    def GetLen (self):                      #daje duzinu liste parova
        return len(self.FminLst)

    def CheckIfInThirdNormalForm(self, key):
        TrivialCnt = 0
        BasicAttCnt = 0
        SuperKeyCnt = 0     
        CheckForAllCnt = 0                                  #provjerava je li relacija u 3.NF 
        for i in self.FminLst:                                   #na osnovu funckija gore opisanih
            if i.CheckIfTrivial():
                TrivialCnt += 1

            if i.CheckIfBasicAttribute(key):
                BasicAttCnt += 1

            if i.CheckIfSuperKey(key):
                SuperKeyCnt += 1

            if SuperKeyCnt > 0 or BasicAttCnt > 0 or TrivialCnt > 0:
                CheckForAllCnt += 1
        if CheckForAllCnt == self.GetLen():
            return 1
        return 0

    
    def CheckIfKeyExist(self, key , lst):   
        cnt = 0                               #provjerava postoji li kljuc u listi parova u svrhu POPRAVIT OVU VJV
        for k in lst:
            for i in key:
                if i in k and i.isalpha():                               #njegovog dodavanja ili ne dodavanja
                    cnt = cnt + 1
            if cnt == len(key):
                return 0
            cnt = 0
        lst.append('[' + key + ']')
        return 1

    def Normalize(self,key):                    #normalizira listu parova na osnovu extracta
        lst = []
        for i in range(0, self.GetLen()):
            lst.append(self.FminLst[i].Extract())
        for i in key:
            self.CheckIfKeyExist(i, lst)
        return lst
    
    def GO(self,key):                           #interface
        if self.CheckIfInThirdNormalForm(key):
            print ("\n --------------------- \n")
            print("ρ = ",self.FminLst)
            print ("\n\nThis relation is already within the 3rd normal form\n")
        else:
            print ("\n --------------------- \n")
            print(self.FminLst)
            print("\nThis relation is not within the 3rd normal form\n\n\n")
            print("Normalizing...\n\n\n")
            lst = self.Normalize(key)
            print("Relation is normalized\n")
            print("ρ = ",lst,"\n")
            print ("\n --------------------- \n")
            


def main1():
    key = ['AE']
    rel1 = Pairs('A','B,C')
    rel2 = Pairs('B', 'D')
    rel3 = Pairs('C','D')

    PairLst = Fmin()
    PairLst.FminLst.append(rel1)
    PairLst.FminLst.append(rel2)
    PairLst.FminLst.append(rel3)
    
    PairLst.GO(key)


def main():
    key = input("Enter the key\n")
    PairLst = Fmin() 
    NumOfRelations = input("Enter the number of relations you want.\n")
    cnt = int(NumOfRelations)

    while cnt > 0:
        
        left = input("left: ")
        right = input ("right: ")
        print("\n")
        relations = Pairs(left,right) 
        PairLst.FminLst.append(relations)
        cnt = cnt - 1
    PairLst.GO(key)
    
#main()
main1()