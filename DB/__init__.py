"""Create SQLAlchemy engine and session objects."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from config import SQLALCHEMY_DATABASE_URI

SQLALCHEMY_DATABASE_URI="mysql+pymysql://fbk:wbhhknz5@localhost:6033/fbk"

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)

# Create database session
Session = sessionmaker(bind=engine)
session = Session()