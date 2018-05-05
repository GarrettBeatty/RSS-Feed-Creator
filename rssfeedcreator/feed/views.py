# -*- coding: utf-8 -*-
"""User views."""
import feedparser
from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import current_user

from rssfeedcreator.extensions import db
from rssfeedcreator.feed.forms import FeedForm
from rssfeedcreator.feed.models import Feed
from rssfeedcreator.utils import flash_errors

blueprint = Blueprint('feed', __name__, url_prefix='/feed', static_folder='../static')


@blueprint.route('/')
@blueprint.route('/<path:feed_url>')
def index(feed_url=None):
    if feed_url is None:
        feed_url = request.args['feed_url']
        return redirect(url_for('feed.index', feed_url=feed_url))

    f = feedparser.parse(feed_url)
    if len(f.entries) == 0:
        return redirect(url_for('public.home'))

    return render_template('feed/index.html', f=f)


@blueprint.route('/get/', methods=['POST'])
def get():
    form = FeedForm(request.form)
    if not form.validate_on_submit():
        flash_errors(form)
        return redirect(url_for('public.home'))

    feed_url = form.feed_url.data
    return redirect(url_for('feed.index', feed_url=feed_url))


@blueprint.route('/add/', methods=['POST'])
def add():
    form = FeedForm(request.form)
    if not form.validate_on_submit():
        flash_errors(form)
        return redirect(url_for('public.home'))

    url = form.feed_url.data
    f = feedparser.parse(url)
    feed = Feed.query.filter_by(url=url).first() or Feed.create(url=url, title=f.feed.title, subtitle=f.feed.subtitle)
    current_user.feeds.append(feed)
    db.session.commit()
    return redirect(url_for('feed.index', feed_url=url))
