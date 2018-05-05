# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from rssfeedcreator.feed.forms import FeedForm

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    feeds = reversed(current_user.feeds)
    form = FeedForm(request.form)

    return render_template('users/members.html', feeds=feeds, form=form)
