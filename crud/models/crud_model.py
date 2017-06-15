from crud import db


class Emp(db.Model):
    __tablename__ = 'emp'
    id = db.Column(db.Integer(), primary_key=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    dept = db.Column(db.String(30))
    sal = db.Column(db.Integer())

    def __init__(self, fname, lname, dept, sal):
        self.fname = fname
        self.lname = lname
        self.dept = dept
        self.sal = sal

    def __repr__(self):
        return '<Emp %r>' % self.id
