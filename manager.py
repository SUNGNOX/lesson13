# -*- coding: utf-8 -*-
from app import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)


if __name__ == '__main__':
    # app.config['DEBUG'] = False
    #'0.0.0.0'让操作系统监听所有公用IP
    # app.run(host='0.0.0.0', port=8000, debug=True)
   manager.run()
#     from livereload import Server
#     lvrld = Server(app.wsgi_app)
#     lvrld.watch('**/*.*')
#     lvrld.serve(open_url=True)
#
#
@manager.command
def dev():
    from livereload import Server
    lvrld = Server(app.wsgi_app)
    lvrld.watch('**/*.*')
    lvrld.serve(open_url=False)