from flask import request, render_template, abort, flash, redirect, url_for

from blueprints.entries import bp
from blueprints.entries.forms import CreateEntryForm, EditEntryForm
from persistence.model.entry import Entry
from persistence.repository.entry import EntryRepository


@bp.route('/')
def list_all():
    if request.args.get('search'):
        entries = EntryRepository.find_by_day(request.args.get('search'))
    else:
        entries = EntryRepository.find_all()

    return render_template('recipes/list.html', entries=entries)


@bp.route('/view/<int:recipe_id>')
def view(recipe_id):
    recipe = RecipeRepository.find_by_id(recipe_id) or abort(404)

    return render_template('recipes/view.html', recipe=recipe)


@bp.route('/create', methods=('GET', 'POST'))
@has_admin_role
def create():
    recipe = Recipe()
    form = CreateRecipeForm()

    if form.validate_on_submit():
        recipe.form_update(form)

        try:
            RecipeRepository.save(recipe)
            flash('Recipe created.')

            return redirect(url_for('recipes.list_all'))
        except Exception as err:
            flash(str(err))

    return render_template('recipes/form.html', form=form, create=True)


@bp.route('/edit/<int:recipe_id>', methods=('GET', 'POST'))
@has_admin_role
def edit(recipe_id):
    recipe = RecipeRepository.find_by_id(recipe_id) or abort(404)
    form = EditRecipeForm(obj=recipe)

    if form.validate_on_submit():
        recipe.form_update(form)

        try:
            RecipeRepository.save(recipe)
            flash('Recipe saved.')

            return redirect(url_for('recipes.edit', recipe_id=recipe.id))
        except Exception as err:
            flash(str(err))

    return render_template('recipes/form.html', form=form)


@bp.route('/delete/<int:recipe_id>', methods=('POST',))
@has_admin_role
def delete(recipe_id):
    recipe = RecipeRepository.find_by_id(recipe_id) or abort(404)

    try:
        RecipeRepository.delete(recipe)
        flash('Recipe deleted.')
    except Exception as err:
        flash(str(err))

    return redirect(url_for('recipes.list_all'))