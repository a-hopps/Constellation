from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Text, Boolean, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector

class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(50))
    role: Mapped[Optional[str]] = mapped_column(String(50))
    company: Mapped[Optional[str]] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    state_country: Mapped[str] = mapped_column(String(50))
    latitude: Mapped[Optional[float]] = mapped_column(Float)
    longitude: Mapped[Optional[float]] = mapped_column(Float)
    starred: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc), 
        onupdate=lambda: datetime.now(timezone.utc)
    )
    email: Mapped[Optional[str]] = mapped_column(String(100))
    linkedin_url: Mapped[Optional[str]] = mapped_column(String(200))

    def __repr__(self) -> str:
        return (
            f"Contact(id={self.id!r}, name={self.first_name!r} {self.last_name!r}, "
            f"role={self.role!r}, company={self.company!r}, "
            f"city={self.city!r}, state_country={self.state_country!r})"
        )

class Interaction(Base):
    __tablename__ = "interactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"))
    interaction_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    notes: Mapped[Optional[str]] = mapped_column(Text)
    embedding: Mapped[Optional[List[float]]] = mapped_column(Vector(1536)) # Dimensions for OpenAI embeddings

    def __repr__(self) -> str:
        return (
            f"Interaction(id={self.id!r}, contact_id={self.contact_id!r}, "
            f"interaction_date={self.interaction_date!r})"
        )

class Connection(Base):
    __tablename__ = "connections"

    source_contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"), primary_key=True)
    target_contact_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"), primary_key=True)
    relationship_label: Mapped[Optional[str]] = mapped_column(String(50))

    def __repr__(self) -> str:
        return (
            f"Connection(source_contact_id={self.source_contact_id!r}, "
            f"target_contact_id={self.target_contact_id!r})"
        )