# -*- coding: utf-8 -*-
"""Feed models."""
from rssfeedcreator.database import Model, Column
from rssfeedcreator.extensions import db


class Feed(Model):
    __tablename__ = 'feeds'
    
    url = Column(db.Text, primary_key=True)
    title = Column(db.Text)
    subtitle = Column(db.Text)

    def __init__(self, url, title, subtitle, **kwargs):
        """Create instance."""
        db.Model.__init__(self, url=url, title=title, subtitle=subtitle, **kwargs)
