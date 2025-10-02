from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime,
    ForeignKey,
    Date,
    DateTime,
    UniqueConstraint
)

from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger , unique=True , nullable=False)
    name = Column(String(length=128) , nullable=False)
    contact = Column(String(length=25))
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime , onupdate=datetime.now)
    
    bookings = relationship("Booking", back_populates="user")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(String(10), nullable=False)  # "10:00" kabi saqlanadi

    created_at = Column(DateTime, default=datetime.now)

    # constraint: bir vaqt va sana uchun faqat bitta odam
    __table_args__ = (
        UniqueConstraint("date", "time", name="uq_booking"),
    )

    user = relationship("User", back_populates="bookings")

    
