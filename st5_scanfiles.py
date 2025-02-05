# сканим папки - фалы в базу  - свойсва 
# + исходная папка - папка назначения 


import os,time,re,json
import shutil

from DB import session
from DB.models import  Dirs , Files
from sqlalchemy import text



 
session.execute( text("TRUNCATE `files`; ") )
session.commit()


f  =  open("data.json")
dj =  json.loads(f.read() )
f.close()


ald = session.query(Dirs).filter_by( created=1 ).all()


for a in ald:

	for f in os.listdir(a.dirp):
		#print(f)
		ff =  os.path.join(a.dirp, f)
		if os.path.isfile(ff):

			file_size = os.path.getsize(ff)

			if f =="package-lock.json":continue


			nx = Files(

			 	dirsrc      = a.dirp,

			    dirdst      = a.dstp,

			    file        = f,

			    bytess      = file_size,

			    #fcopyd      = Column( Boolean , server_default="0" )  # типа  скопированы файлы
			
			)

			session.add(nx)
			session.commit()





