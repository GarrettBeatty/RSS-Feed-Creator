# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template

blueprint = Blueprint('feed', __name__, url_prefix='/feed', static_folder='../static')


@blueprint.route('/')
def members():
    """List members."""
    return render_template('feed/index.html')
