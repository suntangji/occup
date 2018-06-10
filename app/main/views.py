# -*- coding: utf-8 -*-

from flask import request, render_template, jsonify, url_for, redirect, abort
from flask_login import login_required, login_user, logout_user, current_user
from main import app
from model import User, Admin
from main import login_manager
from admin import get_close_value,set_close_value
from modify import insert_user, insert_own, to_leave, get_info, \
    query_own, temp_leave, advice, get_leave_info, \
    clear_own, insert_notice, get_notice, get_suggest, get_occup


# 存储用户id到session中， 用于保存登录信息
@login_manager.user_loader
def load_user(user_id):
    if Admin.query.get(int(user_id)):
        return Admin.query.get(int(user_id))
    return User.query.get(int(user_id))


# 首页
@app.route('/', methods=['GET','POST'])
@login_required
def index():
    # 如果是管理员
    if current_user.user_id == 1000:
        # abort(403)
        return redirect(url_for('admin_index'))

    if request.method == 'GET':
        # 获取桌子占用情况，用于渲染模板
        info = query_own()
        # print info
        return render_template('index.html', info=info)
    elif request.method == 'POST':
        if get_close_value():
            return jsonify({'ret': "已闭馆"})
        data = request.get_json()
        table = data['table_id']
        ret = insert_own(table)
        return jsonify({'ret': ret})


# 离开
@app.route('/leave/')
@login_required
def leave():
    ret = to_leave()
    return jsonify({'ret': ret})


# 暂离
@app.route('/temporary_leave/',methods=['POST'])
@login_required
def temporary_leave():
    data = request.get_json()
    leave_time = data['leave_time']
    ret = temp_leave(leave_time)
    return jsonify({'ret': ret})


# 用户信息
@app.route('/info/')
@login_required
def info():
    ret = get_info()
    return jsonify({'ret': ret})


@app.route('/leave_info/',methods=['POST'])
@login_required
def leave_info():
    data = request.get_json()
    table = data['table_id']
    ret = get_leave_info(table);
    return jsonify({'ret': ret})
#  登出
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    # flash('You have been logged out.')
    return redirect(url_for('login'))


# 登录
@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method == 'POST':
        data = request.get_json()
        user_id = data['user']
        password = data['passwd']
        # ret = verify_password(user_id,password)
        # print type(ret)
        flag = False
        user = User.query.filter_by(user_id=user_id).first()
        if user is not None and user.confirm_password(password):
            # 保存登录信息
            login_user(user,False)
            flag = True
        #if ret is not None :
        return jsonify({'ret': flag})


# 注册
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        # return "33333"
        return  render_template('register.html')
    elif request.method == 'POST':
        # get_json
        # 注册用户
        data = request.get_json()
        user = data['user']
        password = data['passwd']
        # print user,password
        ret = insert_user(user,password)
        # print ret
        return jsonify({'ret': ret})


# 反馈
@app.route('/suggest/', methods=['GET', 'POST'])
@login_required
def suggest():
    if request.method == 'POST':
        data = request.get_json()
        context = data['text']
        contact = data['contact']
        ret = advice(context, contact)
        return jsonify({'ret': ret})
    elif request.method == 'GET':
        suggest_info = get_suggest()
        lens = len(suggest_info)
        return render_template('suggest.html', suggest=suggest_info, len=lens)


# admin
@app.route('/admin/', methods=['GET', 'POST'])
@login_required
def admin_index():
    if current_user.user_id != 1000:
        abort(403)

    if request.method == 'GET':
        # 获取桌子占用情况，用于渲染模板
        info = query_own()
        # print info
        return render_template('admin.html', info=info)
    elif request.method == 'POST':
        data = request.get_json()
        table = data['table_id']
        ret = get_leave_info(table)
        return jsonify({'ret': ret})


@app.route('/admin_login/', methods=['GET','POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        data = request.get_json()
        user_id = data['user']
        password = data['passwd']
        # ret = verify_password(user_id,password)
        # print type(ret)
        flag = False
        user = Admin.query.filter_by(user_id=user_id).first()
        if user is not None and user.confirm_password(password):
            # 保存登录信息
            login_user(user,False)
            flag = True
        #if ret is not None :
        return jsonify({'ret': flag})


@app.route('/clear/', methods=['POST'])
@login_required
def clear():
    data = request.get_json()
    user = data['user_id']
    ret = False
    if current_user.user_id == user:
        ret = clear_own()
    return jsonify({'ret': ret})


@app.route('/close/')
@login_required
def close():

    ret = set_close_value()
    clear_own()
    # ret = CLOSE
    # print ret
    return jsonify({'ret': ret})


@app.route('/notice/', methods=['GET', 'POST'])
@login_required
def notice():
    if request.method == 'GET':
        notice_info = get_notice()
        lens = len(notice_info)
        return render_template('notice.html', notice=notice_info, len=lens)
    elif request.method == 'POST':
        data = request.get_json()
        title = data['title']
        context = data['context']
        ret = insert_notice(title, context)
        return jsonify({'ret': ret})


@app.route('/occup/')
@login_required
def occup():
    occup_info = get_occup()
    lens = len(occup_info)
    return render_template('occup.html',occup=occup_info, len=lens)
if __name__ == '__main__':
    app.run(port=5000,debug=True)