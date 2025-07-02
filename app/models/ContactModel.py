from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from uuid import uuid4

from ...extensions import db

class Contact(db.Model):
  __tablename__ = "contacts"

  id: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid4()), primary_key=True)
  name: Mapped[str] = mapped_column(String, nullable=False)
  email: Mapped[str] = mapped_column(String, nullable=False)
  message: Mapped[str] = mapped_column(String, nullable=False)