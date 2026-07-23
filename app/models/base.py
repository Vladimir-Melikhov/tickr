import uuid
from sqlalchemy import Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    pass


class MainMixin:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    public_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        unique=True,
        index=True,
        default=uuid.uuid4,
        primary_key=True)
