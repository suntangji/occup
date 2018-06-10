# -*- coding: utf-8 -*-
from model import User, db, Own, Suggest, Notice
from flask_login import current_user
import threading


# 注册用户
def insert_user(user_id, password):
    user_id = int(user_id)
    print user_id
    user = User(user_id, password)
    # user.user_id = user_id

    # user.password = password
    # print user.user_id,user.passwd
    db.session.add(user)
    # db.session.commit()
    try:
        db.session.commit()
        flag = True

    except:
        db.session.rollback()
        flag = False

    return flag


# 选座
def insert_own(table):
    # print user.user_id
    own = Own(table, current_user.user_id)
    db.session.add(own)
    # db.session.commit()
    try:
        db.session.commit()
        flag = True

    except:
        db.session.rollback()
        flag = False

    return flag


# 离开
def to_leave():
    user = Own.query.filter_by(user_id=current_user.user_id).first()
    flag = False
    if user is not None:
        db.session.delete(user)
        # db.session.commit()
        try:
            db.session.commit()
            flag = True

        except:
            db.session.rollback()

    return flag


# 获取用户信息
def get_info():
    # 获取用户选择座位的信息
    info = Own.query.filter_by(user_id=current_user.user_id).first()

    info_list = []
    if info is not None:
        info_list.append(info.table_id)
        info_list.append(info.user_id)
        info_list.append(info.leave_time)
        info_list.append(info.time)
    return info_list


# 获取暂离信息
def get_leave_info(table):
    info = Own.query.filter_by(table_id=table).first()
    info_list = []
    if info is not None:
        info_list.append(info.table_id)
        info_list.append(info.user_id)
        info_list.append(info.leave_time)
        info_list.append(info.time)
    return info_list
# 获取选座信息
def query_own():
    # 查询桌子占用情况
    info = Own.query.all()
    info_dict = {}
    # 用字典存储桌子id 以及 是否暂离
    for x in info:
        if x.leave_time != 0:
            info_dict[int(x.table_id)] = 1
        else:
            info_dict[int(x.table_id)] = 0
    return info_dict


# 定时器，两小时后该位置置空
def timer(_db, _Own, _user_id, leave_time):
    # print "tiemr"
    # print leave_time
    def interval():
        # print "interval"
        # print leave_time
        # print _db, _Own, _user_id

        user = _Own.query.filter_by(user_id=_user_id).first()
        if user is not None and user.leave_time != 0:
            _db.session.delete(user)
            _db.session.commit()

    t = threading.Timer(float(leave_time)* 3600,interval)
    t.start()


# 暂离
def temp_leave(leave_time):
    user = Own.query.filter_by(user_id=current_user.user_id).first()
    flag = False
    if user is not None:
        #  表示已经暂离
        if user.leave_time != 0:
            return flag
        user.leave_time = leave_time
        user.time = Own.get_time()
        db.session.add(user)
        # db.session.commit()
        try:
            db.session.commit()
            flag = True
            timer(db, Own, user.user_id, leave_time)
        except:
            db.session.rollback()

    return flag


# 建议
def advice(context,contact):
    sug = Suggest(current_user.user_id, context, contact)
    db.session.add(sug)
    try:
        db.session.commit()
        flag = True

    except:
        db.session.rollback()
        flag = False

    return flag


# 查看单个座位信息
def occup_info(table_id):
    info = Own.query.filter_by(table_id=table_id).first()

# 清空所有
def clear_own():
    infos = Own.query.all()
    for info in infos:
        db.session.delete(info)
    # db.session.commit()
    try:
        db.session.commit()
        flag = True

    except:
        db.session.rollback()
        flag = False

    return flag


def insert_notice(title, context):
    notice = Notice(title, context)
    db.session.add(notice)
    try:
        db.session.commit()
        flag = True

    except:
        db.session.rollback()
        flag = False

    return flag


def get_notice():
    notices = Notice.query.all()
    notice_list = []
    notice_lists = []
    for notice in notices:
        notice_list.append(notice.title)
        notice_list.append(notice.context)
        notice_list.append(notice.date)
        notice_lists.append(notice_list)

        notice_list = []

    return notice_lists


def get_suggest():
    suggests = Suggest.query.all()
    suggest_list = []
    suggest_lists = []
    for suggest in suggests:
        suggest_list.append(suggest.id)
        suggest_list.append(suggest.user_id)
        suggest_list.append(suggest.context)
        suggest_list.append(suggest.contact)
        suggest_lists.append(suggest_list)
        suggest_list = []

    return suggest_lists

def get_occup():
    infos = Own.query.all()
    occup_list = []
    occup_lists = []
    for info in infos:
        occup_list.append(info.user_id)
        occup_list.append(info.table_id)
        occup_list.append(info.leave_time)
        occup_list.append(info.time)
        occup_lists.append(occup_list)
        occup_list = []

    return occup_lists