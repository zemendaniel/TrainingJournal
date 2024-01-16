import click
from alchemical.flask import Alchemical
from flask import g

db = Alchemical()


def init_app(app):
    app.cli.add_command(__install_command)
    app.before_request(__on_before_request)
    app.teardown_appcontext(__on_teardown_appcontext)

    db.init_app(app)


def install():
    db.drop_all()
    db.create_all()


@click.command('install')
def __install_command():
    install()
    click.echo('Application installation successful.')


def __on_before_request():
    if 'session' not in g:
        g.session = db.Session()


def __on_teardown_appcontext(e):
    if 'session' in g:
        g.pop('session').close()

