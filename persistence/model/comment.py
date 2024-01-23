from alchemical import Model
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Comment(Model):
    __tablename__ = "comments"

    username: Mapped[str] = mapped_column(String(180), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    entry_id: Mapped[int] = mapped_column(ForeignKey('entries.id'),
                                          nullable=False, index=True)
    entry: Mapped["Entry"] = relationship(back_populates="comments", cascade="all, delete")

    datetime: Mapped[DateTime] = mapped_column(
            DateTime, nullable=False,
            default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    def form_update(self, form):
        self.content = form.content.data.strip()

    def __repr__(self):
        return f'<Comment {self.content}>'


from persistence.model.entry import Entry
