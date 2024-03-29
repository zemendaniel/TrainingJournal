import datetime
from typing import List

from alchemical import Model
from sqlalchemy import Integer, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Entry(Model):
    __tablename__ = "entries"

    description: Mapped[str] = mapped_column(Text, nullable=False)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    day: Mapped[Date] = mapped_column(Date, default=datetime.datetime.today(), nullable=False)
    comments: Mapped[List["Comment"]] = relationship(
        back_populates="entry", cascade="all, delete", passive_deletes=True
    ) # TODO: kérdés, itt reversben?

    def form_update(self, form):
        self.description = form.description.data.strip()

    def __repr__(self):
        return f'<Entry {self.description}>'


from persistence.model.comment import Comment
