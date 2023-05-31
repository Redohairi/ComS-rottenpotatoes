from . import db
from sqlalchemy.sql import func


class Movie(db.Model):
    __tablename__ = "movie"     #will change to "lesson"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    rating = db.Column(db.String)
    description = db.Column(db.String)
    #professor= db.Column(db.String, db.ForeignKey("user.id"), nullable=False)
    #professor = db.relationship("User", backref="movie", lazy=True)
    discipline = db.Column(db.String)

    
    
    release_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        #return "<Movie %r>" % self.id
        return "<Lesson %r>" % self.id
