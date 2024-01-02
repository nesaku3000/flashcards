from termcolor import colored
file = open('filename')
f = file.readlines()
f[0] = f[0][:-1]
n = int(f[0])
i = 0
c = [False]*n
a = [0]*n
corr = n
while(corr):
    if (c[i%n+1] == False):
        w = f[i%n+1]
        w = w.split(" @ ")
        print(w[1],end='')
        s = input()
        if (s == "end"):
            corr = 0
        elif (s == w[0]):
            print(colored("correct!","light_green"))
            corr -= 1
            c[i%n+1] = True
        else:
            print(colored("correct anwser:","light_red"),w[0])
            a[i%n+1] += 1
    i += 1

print(colored("total number of questions:","light_blue"),i)
for it in range(n):
    if (a[it]):
        w = f[it].split(" @ ")
        w[1] = w[1][:-1]
        print(colored("failed "+str(a[it])+" times!","light_red"),colored(w[1],"light_yellow"),"->",colored(w[0],"light_yellow"))
