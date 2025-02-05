"""Declare models and relationships."""
from sqlalchemy import Column, DateTime, Integer,BigInteger, String, Text, Date ,DECIMAL ,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime, Integer,BigInteger, String, Text, Date ,Float ,Boolean

from DB import engine

Base = declarative_base()



class Dirs(Base):
    __tablename__ = 'dirs'
     
    id          = Column( Integer, primary_key=True )  
    
    root        = Column( Text()     )

    dirrlp      = Column( Text()     ) # Дир  

    dirn        = Column( Text()     ) # Дир имя для создания
 
    dirp        = Column( Text()     ) # дир путь для скана 

    deny        = Column( Boolean , server_default="0" )  

    end         = Column( Boolean , server_default="0" )  # типа тут нет поддиректорий  

    scaned      = Column( Boolean , server_default="0" )  # типа отсканированно и директории получены  


    dstp        = Column( Text()     ) # дир путь создания

    created     = Column( Boolean , server_default="0" )  # типа  созданно

    fcopyd      = Column( Boolean , server_default="0" )  # типа  скопированы файлы
  

    fcount     = Column( BigInteger() , server_default="0" )  # типа  скопированы файлы

class Files(Base):
    __tablename__ = 'files'
     
    id          = Column( Integer, primary_key=True )  
    
    #root       = Column( Text()     )

    dirsrc      = Column( Text()     )

    dirdst      = Column( Text()     ) # дир путь создания

    file        = Column( Text()     )

    bytess      = Column( BigInteger()  , server_default="0"    )

    fcopyd      = Column( Boolean , server_default="0" )  # типа  скопированы файлы
 

Base.metadata.create_all(engine)  
 
 