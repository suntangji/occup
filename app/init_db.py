# -*- coding: utf-8 -*-
from model import *


def init_table():
    for x in xrange(1,41):
        if x <= 10:
            table = Table(x, 1)
        elif x <= 20:
            table = Table(x, 2)
        elif x <= 30:
            table = Table(x, 3)
        else:
            table = Table(x, 4)
        # table.table_id = x
        db.session.add(table)
    try:
        db.session.commit()
    except:
        db.session.rollback()


def init_admin():
    admin = Admin(1000,str(1000))
    db.session.add(admin)
    try:
        db.session.commit()
    except:
        db.session.rollback()


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    init_table()
    init_admin()