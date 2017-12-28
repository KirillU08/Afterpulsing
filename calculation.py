import string
a=0
list=[]
form=""
with open("C:\Projects\Afterpulsing\Measurement\/6\Измерения_Цикл_N2.txt") as file:
    for row in file.readlines():
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
with open("C:\Projects\Afterpulsing\Measurement\/6\Result3.txt", "w") as filew:
    filew.write("%s" % form)
    for item in list:
        filew.write("%s\n" % item)