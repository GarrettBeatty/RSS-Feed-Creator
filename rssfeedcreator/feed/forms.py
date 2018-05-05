from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class FeedForm(FlaskForm):
    feed_url = StringField('URL',
                      validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(FeedForm, self).__init__(*args, **kwargs)
        self.feed = None