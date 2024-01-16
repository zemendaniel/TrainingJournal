from flask import g

from persistence.model.entry import Entry


class EntryRepository:
    @staticmethod
    def find_all():
        statement = (
            Entry
            .select()
            .order_by(Entry.id.desc())
        )

        return g.session.scalars(statement).all()

    @staticmethod
    def find_by_id(entry_id):
        statement = (
            Entry
            .select()
            .where(Entry.id == entry_id)
        )

        return g.session.scalar(statement)

    @staticmethod
    def find_by_day(day):
        statement = (
            Entry
            .select()
            .where(Entry.day.like(f'%{day}%'))
        )

        return g.session.scalars(statement).all()

    @staticmethod
    def save(entry):
        g.session.add(entry)
        g.session.commit()

        return entry

    @staticmethod
    def delete(entry):
        g.session.delete(entry)
        g.session.commit()
        