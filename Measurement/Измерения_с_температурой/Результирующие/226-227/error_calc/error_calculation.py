import string
a=0
list=[]
form=""
with open("1.txt") as file1:
    with open("2.txt") as file2:
        with open("3.txt") as file3:
            for row in file1.readlines():
                if(a==0):
                    form=row
                arr=row.split()
                if(a>0):
                    #print(arr[0], "|", arr[1], "|", arr[2], "|", arr[3], "|", arr[4], "|", arr[5], "|", arr[6], "|", arr[7], "|",arr[8])

                    NSS1=float(arr[3])
                    NK1=float(arr[7])
                    NSS2=float(arr[8])
                    NSS3=float(arr[4])
                    P=(NSS1*NK1-NSS2*NSS3)/(NSS3*(NK1-NSS3))
                    print(P)

                    arr[0]=repr(P)
                    str='\t'.join(arr)
                    list.append(str)
                a=a+1
with open("result.txt", "w") as filew:
    filew.write("%s" % form)
    for item in list:
        filew.write("%s\n" % item)
