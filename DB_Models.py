from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Post.db',pool_size=1000, max_overflow=1000)
Base = declarative_base()

# Association table between User and Raffle


class Post(Base):
    __tablename__ = 'posts'

    id = Column(String, primary_key=True, unique=True)

    type = Column(String) # MSG / EMBED / REPLY / ASIAN_MSG
    messageText = Column(String)
    messageText_reply = Column(String)
    channel_id_RA = Column(String)
    channel_id_other = Column(String)
    image = Column(Boolean)
    header_number = Column(Integer)


Base.metadata.create_all(engine)
