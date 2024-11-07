
tuple1=(2,4,6,8)
print(tuple1)

#tuple1[0]=5

print(tuple1)
#tuple1[2]=3



tuple2=(2,4,6,8,8,10,2)
print(tuple2)
print(tuple2.index(6))
print((tuple2[3], tuple2[4]))

tuple3=(2,4,'6',8,8,10,2)
print(tuple3)
# tuple ler assigned edildikten sonra degistirilemez
# list ler manupule edilebilir
liste1=[2,4,6,8]
print(liste1)
liste1[2]=5
print(liste1) #[2, 4, 5, 8]

tuple2=(3)
print(type(tuple2))#<class 'int'>
tuple3=(3,)
print(type(tuple3))#<class 'tuple'>
liste1=[2,4,6,8,10]
print(liste1) #[2, 4, 6, 8, 10]
liste2=((2,4,6,8,10))
print(liste2) #(2, 4, 6, 8, 10)
#Eger birbirlerine donusturmek isretsek list(x)  tuble(x) yapip casting yapabiliriz

tuple1=(2,4,6,8)
tuple2=(10,12)
print(tuple1+tuple2)
print(tuple1,tuple2)
