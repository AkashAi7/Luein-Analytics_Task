
def ap():
    arr=[]
    for i in range(0,3):
        le=int(input())
        arr.append(le)

    if arr[1]-arr[0] != arr[2]-arr[1]:
        print("Not a AP")
    else:
        print(arr[2]+arr[2]-arr[1])


ap()