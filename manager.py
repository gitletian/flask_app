# coding: utf-8
# __author__: ""
import os
from app import create_app
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
# 导入 db, 同时加载了 models 文件,
# from app import db 是无法加载 models文件, 所以无法创建 表
from app.models import db


# 创建 app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)  # 管理 app

'''
集成Python Shell:
创建表:
python manager.py shell
from hello import db
db.create_all()
db.drop_all()
db.create_all()
'''


def make_shell_context():
    '''
    每次启动Shell会话都要导入数据库实例和模型，可以配置让 Flask-script 的shell命令自动导入特定的对象
    :return:
    '''
    return dict(app=app, db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))

'''
使用Flask-Migrate进行数据库迁移
在命令行中:
python manager.py db init # 创建迁移仓库
python manager.py db migrate -m "initial migration" 创建迁移脚本
python manager.py db upgrade 更新数据库(应用迁移脚本)
python manager.py db downgrade 更新数据库(回退到上一个迁移脚本)
'''
# 第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app, db)
# manager是Flask-Script的实例，这条语句在flask-script中添加一个db命令
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
