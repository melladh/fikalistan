#!/usr/bin/env python
from fikalistan import app, db

if __name__ == "__main__":
    db.drop_all(app=app)
    db.create_all(app=app)