# full_alphabet =('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')



def vaoulcheck(word):
    vauols = ['a', 'e', 'i', 'o', 'u']
    vaoulcount=0
    for i in word:
        if i in vauols:
            vaoulcount+=1
    if vaoulcount >=3:
        return 1
    elif vaoulcount <3:
        return 0
# print(vaoulcheck(word))

def doublecheck(word):
    templist=[]
    for i in word:
        templist.append(i)
    for jayz in range(0,len(templist)-1):
        if templist[jayz] == templist[jayz+1]:
            return 1
    return 0
# print(doublecheck(word))

def consecutivecheck(word):
    left_alphabet = ('a', 'c', 'p', 'x')
    right_alphabet = ('b', 'd', 'q', 'y')
    templist=[]
    for i in word:
        templist.append(i)
    i=0
    for letter in word:
        i+=1
        if letter in left_alphabet:
            x = left_alphabet.index(letter)
            if templist[i] == right_alphabet[x]:
                return 0
    return 1
# print(consecutivecheck(word))
file=open('naughtylist.txt','r')
def wordcheck(file):
    count = 0
    for i in range(0,1001):
        string = file.readline()
        tempcount=0
        tempcount+=vaoulcheck(string)
        tempcount+=doublecheck(string)
        tempcount+=consecutivecheck(string)
        if tempcount == 3:
            count+=1
    return count
# print(wordcheck(file))
word = 'nwhaaaanwxw'
def double_paircheck(word):
    templist=[]

    for i in word:
        templist.append(i)
    for i in range(len(templist)-2):
        testingstring=templist[i]+templist[i+1]
        print('testing against: ', testingstring)
        tempcount = 0
        a23 = testingstring[1] + templist[i + 2]
        if testingstring != a23:
            print('these two arn equal')
            for z in range(len(templist)-1):
                concacanat=templist[z]+templist[z+1]
                print('trying: ',concacanat)


                if testingstring == concacanat:
                    print('if you had gone this far, congratualtions, not many make it')
                    # print('major overlap return no do: ')
                    # print(a12,'equals: ',a23)
                    tempcount += 1
                    print(tempcount)
                    if tempcount > 1:
                        print('return 1: ')
                        return 1
            # elif testingstring[0]+testingstring[1] ==testingstring[1]+templist[i+2]:
            #     print('!!major overlap: ', testingstring[0], testingstring[1], templist[i + 2], '!!')
            #     print('major overlap return no do: ')

    print('returingn 0')
    return 0

print(double_paircheck(word))