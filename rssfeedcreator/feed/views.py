# -*- coding: utf-8 -*-
"""User views."""
import feedparser
from flask import Blueprint, render_template, request, url_for, redirect

blueprint = Blueprint('feed', __name__, url_prefix='/feed', static_folder='../static')


@blueprint.route('/')
@blueprint.route('/<path:feedurl>')
def index(feedurl=None):
    if feedurl is None:
        return redirect(url_for('feed.index', feedurl=request.args['feedurl']))

    f = feedparser.parse(feedurl)

    return render_template('feed/index.html', f=f)
