import os,time,re,json
import shutil

from DB import session
from DB.models import  Dirs , Files
from sqlalchemy import text




session.execute( text("TRUNCATE `dirs`;  ") )
session.execute( text("TRUNCATE `files`; ") )
session.commit()


f  =  open("data.json")
dj =  json.loads(f.read() )
f.close()

#
def ch_venv(root):

	ch = os.listdir(root)

	v=0
	if "bin" in ch  and "include" in ch and "lib" in ch:
		v=1

	return v
#
def ch_end_dir(root):

	#print("----",root,"-----")

	#ch = os.listdir(root)
	#ch = [ f for f in os.listdir(root+"/") if os.path.isdir(f) ]

	ch = []
	for f in os.listdir(root):
		#print(f)
		if os.path.isdir( os.path.join(root, f)): ch.append(f)

	ed = 0
	if len(ch)==0 : ed=1
	#print(ch)

	return ed

#
def fcount(root):

	co=0
	for f in os.listdir(root):
		#print(f)
		if os.path.isfile( os.path.join(root, f) ): co+=1



	return co #fcount 



# init fold
for d in os.listdir(dj["src"]):
	

	e=0
	t_p = os.path.join( dj["src"], d)
	if os.path.isdir(t_p):
		print( d , end="    " )

		ex=0
		scn  = 0

		v=0
		if ch_venv(t_p):
			v  = 1
			ex = 1
			scn  = 1

		pch=0
		if d=="__pycache__":
			pch = 1
			ex  = 1
			scn  = 1

		nm=0
		if d=="node_modules" or d=="vendor" or d==".venv" or d=="venv":
			nm = 1
			ex = 1
			scn  = 1

		edr=0
		if ch_end_dir(t_p):
			edr = 1
			scn  = 1

		print(t_p ,v,pch,nm,edr,ex)
		e=1

		relative_path = os.path.relpath( t_p , dj["src"] )
		target_path   = os.path.join(dj["dst"], d)


		#print(t_p ,v,pch,nm,edr,ex ,relative_path ,target_path)
		#e=1


		nx = Dirs(
				
				root        = dj["src"],

				dirrlp      = relative_path,

				dirn        = d,

			    dirp        = t_p,

			    deny        = ex,

			    end         = edr,

			    scaned      = scn,

			    dstp        = target_path,

			    fcount      = fcount(t_p) 
			
			)
		session.add(nx)
		session.commit()
		



	if e==0:print()
	


#####   second -aall
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


def sca():

	al = session.query(Dirs).filter_by( deny=0 , scaned=0 ).all()


	for a in al:

		ddd = a.dirp

		for d in os.listdir( ddd ):
		

			e=0
			t_p = os.path.join( ddd, d)

			if os.path.isdir(t_p):
				print( d , end="    " )
				scn  = 0

				ex=0

				v=0
				if ch_venv(t_p):
					v  = 1
					ex = 1
					scn =1

				pch=0
				if d=="__pycache__":
					pch = 1
					ex  = 1
					scn =1

				nm=0
				if d=="node_modules" or d=="vendor" or d==".venv" or d=="venv":
					nm = 1
					ex = 1
					scn =1

				if d==".git":
					edr  = 1
					scn  = 1
					ex   = 1


				edr=0
				if ch_end_dir(t_p):
					edr = 1
					scn  = 1

				#print(t_p ,v,pch,nm,ex)
				#e=1

				relative_path = os.path.relpath(t_p, dj["src"] )
				target_path   = os.path.join(dj["dst"], relative_path )


				print(t_p ,v,pch,nm,edr,ex ,relative_path ,target_path)
				e=1

				nx = Dirs(
						
						root        = ddd,

						dirrlp      = relative_path,

						dirn        = d,

					    dirp        = t_p,

					    deny        = ex,

					    end         = edr,

					    scaned      = scn,

				    	dstp        = target_path,

				    	fcount      = fcount(t_p) 
					
					)
				session.add(nx)
				session.commit()


				session.query(Dirs).filter_by( dirp = ddd).update( {"scaned":1})
				session.commit()

				



		if e==0:print()


while True:
	ch = session.query(Dirs).filter_by(scaned=0).first()
	if ch:
		sca()
	else:
		break

	#time.sleep(1)
	