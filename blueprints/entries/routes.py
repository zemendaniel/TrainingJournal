from flask import request, render_template, abort, flash, redirect, url_for

from persistence.model.comment import Comment
from blueprints.entries import bp
from blueprints.entries.forms import CreateEntryForm, EditEntryForm
from blueprints.comments.forms import CreateCommentForm
from persistence.repository.comment import CommentRepository
from persistence.model.entry import Entry
from persistence.repository.entry import EntryRepository


@bp.route('/')
def list_all():
    if request.args.get('search'):
        entries = EntryRepository.find_by_day(request.args.get('search'))
    else:
        entries = EntryRepository.find_all()

    return render_template('entries/list.html', entries=entries)


@bp.route('/view/<int:entry_id>', methods=('GET', 'POST'))
def view(entry_id):
    entry = EntryRepository.find_by_id(entry_id) or abort(404)
    comment = Comment()
    comment_form = CreateCommentForm()

    if comment_form.validate_on_submit():
        comment.form_update(comment_form)

        try:
            CommentRepository.save(comment)
            flash("Comment created.")

        except Exception as err:
            flash(str(err))

    return render_template('entries/view.html', entry=entry)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    entry = Entry()
    form = CreateEntryForm()

    if form.validate_on_submit():
        entry.form_update(form)

        try:
            EntryRepository.save(entry)
            flash('Entry created.')

            return redirect(url_for('entries.list_all'))
        except Exception as err:
            flash(str(err))

    return render_template('entries/form.html', form=form, create=True)


@bp.route('/edit/<int:entry_id>', methods=('GET', 'POST'))
def edit(entry_id):
    entry = EntryRepository.find_by_id(entry_id) or abort(404)
    form = EditEntryForm(obj=entry)

    if form.validate_on_submit():
        entry.form_update(form)

        try:
            EntryRepository.save(entry)
            flash('Entry saved.')

            return redirect(url_for('entries.edit', entry_id=entry.id))
        except Exception as err:
            flash(str(err))

    return render_template('entries/form.html', form=form)


@bp.route('/delete/<int:entry_id>', methods=('POST',))
def delete(entry_id):
    entry = EntryRepository.find_by_id(entry_id) or abort(404)

    try:
        EntryRepository.delete(entry)
        flash('Entry deleted.')
    except Exception as err:
        flash(str(err))

    return redirect(url_for('entries.list_all'))

