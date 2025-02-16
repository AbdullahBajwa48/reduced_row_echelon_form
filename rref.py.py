from fractions import Fraction


# Function for creating leading 1 in the equation
def createLeadingOne(list):
    try:

        atpos = 0
        try:
            for p in list:
                if (p != 0):
                    break
                else:
                    atpos +=1
        except:
            atpos = 0 
    # db = divided_by
        n=0
        db = list[atpos]
        for x in list:
            list[n] = Fraction(x,db)
            n+=1
        return list
    except:
        print("either system is inconsistent or have infinite solutions  :)")
        quit()

# In this function we are considering that higherlist has a leading one and
# below that leading one we are going to make create zero
# [1,3,4]

def underLead_makeZero(higherlist,lowerlist):
    try:
        atpos = 0
        for x in lowerlist:
            if (x!=0):
                break
            else:
                atpos+=1
                

        # mp = multiplied_by
        mp = lowerlist[atpos]
        n=0
        for x in higherlist:
            
                lowerlist[n] = (lowerlist[n]-x*mp)
                n+=1
        return lowerlist
    except:
        print("either system is inconsistent or have infinite solutions  :)")
        quit()

# In the following we are considering that lower list contains a
# leading 1 and to form reduced echelon form we are making above that leadng 1 entry = 0

def upperLead_makeZero(higherlist,lowerlist):
    try:
        atpos = 0
        try:
            for x in lowerlist:
                if (x ==1):
                    break
                else:
                    atpos+=1
        except:
            atpos = 0
        n=0
        mp = higherlist[atpos]
        for x in lowerlist:
            higherlist[n] = higherlist[n]-x*mp
            n+=1
        return higherlist
    except:
        print("either system is inconsistent or have infinite solutions  :)")
        quit()
# creating a full solve function so that user can
# just give input as list of lists and retrieve answer

def full_solve(lstoflsts):
    try:
        n=0
        for lst in lstoflsts:
            n+=1
            createLeadingOne(lst) 
            for further_lst in lstoflsts[n:]:
                try:
                    underLead_makeZero(lst,further_lst)        
                except:
                    continue
        
        n=0
        for lst in lstoflsts:
            n+=1
            for further_lst in lstoflsts[n:]:
                try:
                    upperLead_makeZero(lst,further_lst)  
                except:
                    continue
                        
        for lst in lstoflsts:
            print(lst[-1])
    except:
        print("problem occured in full solving try with different input  :)")
        quit()

# Taking inputs from the user
# Creating a function for input so that users can also experience this 
# also calling all the functions inside it to provide the answer
def give_input():
    try:
        no_rows = int(input('Enter number of equations: '))
        dic = {}
        lstoflsts = []
        for x in range(no_rows):
            key = f"lst {x+1}"
            value = list(map(int,input(f"enter equation {x+1}\n").split()))

            if (len(value)-1 > no_rows):
                print("ERROR: number of vairables cannot excceed no number of equations: Try Again")
                quit()

            dic[key] = value

        for key,value in dic.items():
            lstoflsts.append(value)
        full_solve(lstoflsts)
    except:
        print("Some thing went wrong try again with a different input  :)")
        quit()
