from sqlalchemy import create_engine , URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_HOST , DB_PORT , DB_USER , DB_PASSWORD , DB_NAME


url = URL.create(
    drivername="postgresql+psycopg2",
    host=DB_HOST,
    port=DB_PORT,
    username=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME   
)

engine = create_engine(url)
Base = declarative_base()
LocalSession = sessionmaker(bind=engine , autoflush=True , autocommit=False)