'''
#lets imnclude tuple in about list (yuples are immutable)
batch.insert(2,("viza","hyd","vijayawada"))
print(batch)
#print(len(batch))
#as we have a tuple inside a listt
print(len(batch[2])
print(batch[2][:2]))#("vizag","hyd")
print(batch[2][1])#this reture 'hyd'-->string
print(batch[2][:2])#returns ("vizag","vijayawada")             
print(batch[2].index('hyd'))#tuplue will have only count,index
#index-->first occrance
#count-->reture the count of objects
print(batch[2].index('codegana'))#reture count as 0
#index will raise error,where as count will reture 0

batch.insert(3,['pfs','da','jfs'])
pint(batch)
#now let us apply some of list function in aboue batch list
print(batch[3])
print(batch[3][1])
#to convert only jfs as upper case-->jfs
print[3][2]=batch[3][2],upper()
print(batch[3][2])
#now to wanted to add new course in batch[3]position -->aaa
batch[3].append ('aaa')
print(batch[3])
print(len(batch))

print(batch)
batch.romove('akash')
print(batch)
#remove-->value,pop-->index
batch.pop()#pop by default remove last index value
print(batch)
#batch[2].remove('hyd')# raises attribute error
#del batch[2][1]#tuple is immuable so we cant inseet/remove
#we want to remove entire data but keep the list as it is-->clear()
batch.clear()
print(batch)
'''
#lets work on dictionaries
#dict-->{k:v},keys must be unique
#keys can be int'float,strin,list

details(len['batch']=['PFS6']
#print(details)
details['course']=['python']
#ptint(len(details))
#print(details)
details['students']=['sai','hema']
#we want to update the dictionary
details.update({'branch':('hyd','vizag'),
                'subject':{'python','Aptititude','softskills'}})
        
print(details)
print(len(details))
#first always check the type-->dict-->keys()        
#keys(),values(),items()        
#print(details.keys())#returns only keys
#print(details['batch'])
details ['batch'].extend(['PFS6','da'])
#print(details)
detaisls['students'].extent(['anil','sana','akash'])
print(details)#here key should be checked
details['subjects'].add('DSA')#SET IS unique and unorderd
print(details)




