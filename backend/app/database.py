from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./meetings.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    language = Column(String, nullable=True)
    transcript = Column(Text, nullable=True)
    meeting_summary = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


def init_db():
    Base.metadata.create_all(bind=engine)


def save_meeting(filename, language, transcript, meeting_summary):
    db = SessionLocal()
    try:
        meeting = Meeting(
            filename=filename,
            language=language,
            transcript=transcript,
            meeting_summary=meeting_summary
        )
        db.add(meeting)
        db.commit()
        db.refresh(meeting)
        return meeting.id
    finally:
        db.close()


def get_all_meetings():
    db = SessionLocal()
    try:
        return db.query(Meeting).order_by(Meeting.created_at.desc()).all()
    finally:
        db.close()


def get_meeting_by_id(meeting_id):
    db = SessionLocal()
    try:
        return db.query(Meeting).filter(Meeting.id == meeting_id).first()
    finally:
        db.close()