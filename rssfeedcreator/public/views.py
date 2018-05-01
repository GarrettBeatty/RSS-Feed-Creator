# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user

from rssfeedcreator.extensions import login_manager
from rssfeedcreator.public.forms import LoginForm
from rssfeedcreator.user.forms import RegisterForm
from rssfeedcreator.user.models import User
from rssfeedcreator.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))



@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""

    if current_user and current_user.is_authenticated:
        return render_template('public/home.html')

    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('public.home')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    elif request.method == 'GET':
        return redirect(url_for('public.register'))




@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        login_user(user)
        flash('You are logged in.', 'success')
        redirect_url = request.args.get('next') or url_for('public.home')
        return redirect(redirect_url)
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/about/')
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template('public/about.html', form=form)
