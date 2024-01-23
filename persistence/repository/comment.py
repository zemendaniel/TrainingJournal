from flask import g


class CommentRepository:
    @staticmethod
    def save(comment):
        g.session.add(comment)
        g.session.commit()

        return comment

    @staticmethod
    def delete(comment):
        g.session.delete(comment)
        g.session.commit()
