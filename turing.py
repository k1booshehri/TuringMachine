
machine=input()
n=int(input())
inlist=[]
for i in range(n):
    inlist.append(input())
for i in range(n):
    head=0
    status=""
    state="1"
    input=inlist[i]
    if input=='':
        input='1'
#    final='11'
    inputlist=input.split('0')
    tape={}
    for x in range(-50,+50):
        tape[x]='1'
    for x in range(len(inputlist)):
        tape[x]=inputlist[x]

    transitions=[]
    trDetailed=[]
    transitions=machine.split('00')

    for i in transitions:
        trDetailed.append((i.split('0')))
    comparelist=[]
    for x in trDetailed:
        comparelist.append(x[0])
        comparelist.append(x[2])
    final=max(comparelist)
    while(True):   
        switch="off"
        for item in trDetailed:
            if (item[0]==state and item[1]==tape[head]):
                switch="on"
                state=item[2]
                tape[head]=item[3]
                if(item[4])=='1':
                    head=head-1
                else:
                    head=head+1
        if switch=="off":
            break



    if state==final:
        print("Accepted")
    else:
        print("Rejected")