# # 书上练习题 5-1
# def func(*args):
#     v1=sum(args)/len(args)
#     return (v1,) + tuple ({k for k in args if k > v1})

# k=func(*(i for i in range(10)))
# print(k)
            

# #    5-2
# def func (s):
#     a=[0,0]
#     for i in s:
#         if i.isupper() == 1:
#             a[0]+=1
#         else:
#             a[1]+=1
#     return tuple(a)

# s="asdasdAASDXCasdasd"
# print(func(s))
# print(len(s))

# #5-6 
# def func (x):
#     a=[]
#     n=0
#     b=[]
#     for i in range(1,x+1):
#         for k in range(1,i):
#             if k == 1:
#                 continue
#             elif i%k==0:
#                 break
#             elif k==i-1:
#                 a.append(i)
#                 n+=1
#     for i in range(n):
#         for k in range(i+1,n):
#             if a[i]+a[k]==x:
#                 b.append(a[i])
#                 b.append(a[k])

#     return tuple(b)

# print(func(456))

# 5-7
# def func (a ,b):
#     if a <= b:
#         a,b=b,a 
#     x,y=a,b
#     d=a%b
#     while d!=0:
#         d=b%d
#         b=d
#     i=[]
#     i.append(b)
#     i.append(x*y/b)
#     return tuple(i)
# print(func(54,21))


