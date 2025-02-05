import os,time,re,json
import shutil

from DB import session
from DB.models import  Dirs , Files
from sqlalchemy import text



 

 


ald = session.query(Files).filter_by( fcopyd=0 ).all()


for a in ald:

    src_file_path = os.path.join( a.dirsrc, a.file)
    dst_file_path = os.path.join( a.dirdst, a.file)

    #print(src_file_path , dst_file_path )

    if not os.path.exists(dst_file_path):
                shutil.copy2(src_file_path, dst_file_path)
                print(f"Скопирован файл: {dst_file_path}")


                a.fcopyd = 1
                session.commit()

	 



