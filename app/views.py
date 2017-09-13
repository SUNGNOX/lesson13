# -*- coding: utf-8 -*-
from flask import request, render_template, flash, url_for
from werkzeug.utils import secure_filename
from os import path
from markdown import markdown


def create_view(app):
    @app.route('/')
    def hello_world():
        return render_template('index.html', name="WELCOM", body="# filter")

    #正则表达式匹配路由
    @app.route('/<regex("[a-z]{3}"):user_name>')
    def regx(user_name):
        return render_template('regx.html', link=request.url)

    @app.route('/index')
    def index():
        return render_template('index.html', name="WELCOM", body="# filter")

    @app.route('/serve', methods=['GET', 'POST'])
    def serve():
        if request.method == 'GET':
            return render_template('upload.html')
        f = request.files['file']
        uploadpath = path.join('E:\python\upload', secure_filename(f.filename))
        f.save(uploadpath)
        return render_template('upload.html')

    @app.route('/login', methods=['POST', 'GET'])  # methods不要忘了s
    def login():
        from forms import LoginForm
        form0 = LoginForm()
        if request.method == 'GET':
            return render_template('login.html', title=u'登录', form0=form0, method=request.method)
        elif request.method == 'POST' and request.form.get('username')=='sunxiong':
            flash(u'登陆成功!!')
            return render_template('login_success.html',method=request.method)
        else:
            flash(u'登录失败，请重新登录！！')
            return render_template('login.html', title=u'登录失败，请重新登录！！', form0=form0, method=request.method)

    @app.route('/about')
    def about():
        return 'Hello about!'

    @app.route('/context')
    def context():
        return 'Hello context!'

    # 自定义测试函数
    @app.template_test('jump_url')
    def is_current_url(link):
        return link['href'] == url_for('context')

    #    return link['href'] == request.url


    # 自定义过滤器
    @app.template_filter('md')
    def mark2html(txt):
        return markdown(txt)

    def readfile(file):
        with open(file) as f:
            text = reduce(lambda x, y: x + y, f.readlines())
        return text.decode('utf-8')

    # 上下文处理器
    @app.context_processor
    def cntxtp():
        return dict(readfile=readfile)

    # 错误页面
    @app.errorhandler(404)
    def not_found():
        return render_template('404.html'), 404