import os,time,re,json
import shutil

from DB import session
from DB.models import  Dirs , Files
from sqlalchemy import text



 


f  =  open("data.json")
dj =  json.loads(f.read() )
f.close()


ald = session.query(Dirs).filter_by(deny=0,created=0).all()


for a in ald:

	if not os.path.exists(a.dstp):
            os.makedirs(a.dstp)
            print(f"Создана директория: {a.dstp}")

            a.created = 1
            session.commit()
	else:
		a.created = 1
		session.commit()

