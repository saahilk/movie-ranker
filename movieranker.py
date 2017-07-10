##Made using api found at https://github.com/theapache64/movie_db
import os
import operator
import json,urllib.request

class Movie(object):

    mcount=0
    
    def __init__(self,name,m_rating):
        self.name=name
        self.m_rating=m_rating
        Movie.mcount+=1

    def __repr__(self):
        return "<name:%s, rating:%s" % (self.name,self.m_rating)
    

movielist=os.listdir('f:\Movies')
length=len(movielist)
mlist=[]
ini="http://theapache64.xyz:8080/movie_db/search?keyword="

for i in range(length):
    movie=str(movielist[i])
    b1=movie.find('(')
    b2=movie.find('[')
    if b1==-1 and b2==-1:
        ind=len(movielist[i])
    elif b1==-1:
        ind=b2
    elif b2==-1:
        ind=b1
    else:
        ind=min(b1,b2)
    movielist[i]=movie[:ind]
    with urllib.request.urlopen(ini+movielist[i].strip().replace(' ','+')) as url:
        data=json.loads(url.read().decode())
        if data.get('error_code')==0:
            mlist.append(Movie(movielist[i],data.get('data').get('rating')))
            print(movielist[i]+"-------\t"+data.get('data').get('rating')+"\n")
        else:
            mlist.append(Movie(movielist[i],"-1"))
            print(movielist[i]+"-------\tN/A\n")

cmp=operator.attrgetter("m_rating")
sort_list=sorted(mlist,key=cmp,reverse=True)

f1=open('Movies.txt',"w")

for m in sort_list:
    f1.write("{:<80} {:<5}\n".format(m.name,m.m_rating))
f1.close()

        
