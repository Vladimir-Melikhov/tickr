from app.models.base import Base, MainMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Instrument(Base, MainMixin):
    symbol: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    name: Mapped[str | None] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(default=True)
