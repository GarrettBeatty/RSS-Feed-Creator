from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
import feedparser
import sys

class FeedForm(FlaskForm):
    feed_url = StringField('URL',
                      validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(FeedForm, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate the form."""
        initial_validation = super(FeedForm, self).validate()
        if not initial_validation:
            return False

        return True

    def validate_feed_url(self, field):
        # count the number of user ids for that username
        # if it's not 0, there's a user with that username already
        feed = feedparser.parse(field.data)
        if len(feed.entries) == 0:
            raise ValidationError('RSS URL not valid')