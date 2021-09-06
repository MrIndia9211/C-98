# def greet(name):
#     print('Hello, '+name)

# greet("raghav")

def countword():
    filename=input('Enter The File Name: ')
    numberofwords=0
    f=open(filename,'r')
    for line in f :
        words=line.split()
        numberofwords=numberofwords+len(words)
        
    print("no of words :")
    print(numberofwords)
 
countword()
