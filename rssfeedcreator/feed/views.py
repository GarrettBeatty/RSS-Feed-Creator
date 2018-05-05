# -*- coding: utf-8 -*-
"""User views."""
import feedparser
from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import current_user

from rssfeedcreator.extensions import db
from rssfeedcreator.feed.forms import FeedForm
from rssfeedcreator.feed.models import Feed

blueprint = Blueprint('feed', __name__, url_prefix='/feed', static_folder='../static')


@blueprint.route('/')
@blueprint.route('/<path:feedurl>')
def index(feedurl=None):
    if feedurl is None:
        url = request.args['feedurl']
        return redirect(url_for('feed.index', feedurl=url))

    f = feedparser.parse(feedurl)

    return render_template('feed/index.html', f=f)


@blueprint.route('/add/', methods=['POST'])
def add():

    form = FeedForm(request.form)
    url = form.feed_url.data
    f = feedparser.parse(url)
    feed = Feed.create(url=url, title=f.feed.title, subtitle=f.feed.subtitle)
    current_user.feeds.append(feed)
    db.session.commit()
    return redirect(url_for('feed.index', feedurl=url))
