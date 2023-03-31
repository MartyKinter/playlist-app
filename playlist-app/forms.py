"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length



class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField(
        "name", validators=[InputRequired(), Length(min=1, max=100)]
    )
    description = StringField("description", validators=[Length(max=100)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField(
        "title", validators=[InputRequired(), Length(min=1, max=100)]
    )
    artist = StringField("artist", validators=[Length(max=100)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
