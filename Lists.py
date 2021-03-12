if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(0,N):
        value = input().split(" ")
        if value[0] == "insert":
            l.insert(int(value[1]),int(value[2]))
        elif value[0] == "append":
            l.append(int(value[1]))
        elif value[0] == "remove":
            l.remove(int(value[1]))
        elif value[0] == "pop":
            l.pop()
        elif value[0] == "reverse":
            l = l[::-1]
        elif value[0] == "sort":
            l.sort()
        elif value[0] == "print":
            print(l)
            
