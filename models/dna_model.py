from sqlalchemy import Column, Integer, String, Boolean
from db.db_connection import Base


class ADNRecord(Base):
    __tablename__ = 'adn_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dna = Column(String, unique=True, nullable=False)
    is_mutant = Column(Boolean, nullable=False)
