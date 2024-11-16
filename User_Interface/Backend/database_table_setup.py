import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func, Boolean, text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Session

Base = declarative_base()

class User(Base):
    """Creates a user authentication model"""
    __tablename__ = 'users'
    user_name = Column(String, primary_key=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default = func.now())
    max_tokens = Column(Integer, default=3)

    downloads = relationship("Download", backref="user", cascade='all, delete-orphan')
    recovery_tokens = relationship('RecoveryTokens', backref='user', cascade='all, delete-orphan')

class Download(Base):
    """Creates a download tracking model"""
    __tablename__ = 'downloads'
    download_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.user_name'), index=True)
    video_url = Column(String, nullable=False, index=True)
    download_type = Column(String, nullable=False)
    artist_name = Column(String)
    song_name = Column(String)
    download_genre = Column(String)

class RecoveryTokens(Base):
    """Creates a users recovery token model"""
    __tablename__ = "recovery_tokens"
    recovery_token_id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('users.user_name'), index=True)
    hashed_token = Column(String(255),unique=True, nullable=False)
    use_status = Column(Boolean, default=False)


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Create the table
# Base.metadata.create_all(bind=engine)
# print("Tables created successfully")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
