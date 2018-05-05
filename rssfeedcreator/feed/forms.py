from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import feedparser
import sys

class FeedForm(FlaskForm):
    feed_url = StringField('URL',
                      validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(FeedForm, self).__init__(*args, **kwargs)
        self.feed = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(FeedForm, self).validate()
        if not initial_validation:
            return False

        self.feed = feedparser.parse(self.feed_url.data)
        if len(self.feed.entries) == 0:
            return False

        return True