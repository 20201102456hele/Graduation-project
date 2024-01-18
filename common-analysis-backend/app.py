
from flask import Flask, request


from db import Database
from util import success, error

app = Flask(__name__)


# 登陆
@app.route('/api/user/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("name", None)
    password = data.get("password", None)
    if not username or not password:
        return error("用户名和密码不能为空")
    db = Database()
    sql = f"""
    select * from user where username = '{username}' and password = '{password}'
    """

    res = db.fetchall(sql)
    db.close()
    if len(res) == 0:
        return error("用户名或密码不正确")
    data = {
        "token": res[0]["id"]
    }
    return success(data)

# 获取登陆信息
@app.route('/api/user/info', methods=['POST'])
def info():
    data = request.get_json()
    user_id = data["token"]
    db = Database()
    sql = f"""
    select * from user  where id = {user_id}
    """
    res = db.fetchall(sql)
    db.close()
    return success({"info": res[0]["username"]})

# 获取用户列表
@app.route('/api/system/user/list', methods=['POST'])
def user_list():
    db = Database()
    sql = f"""
    select * from user 
    """
    res = db.fetchall(sql)
    db.close()

    return success({"list": res})

# 新增用户
@app.route('/api/system/user/add', methods=['post'])
def add_user():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)
    db = Database()
    sql = f"""
    insert into user (username, password) values ('{username}', '{password}')
    """
    db.execute(sql)
    db.close()

    return success("新增成功")

# 删除用户
@app.route('/api/system/user/del/<int:user_id>', methods=['delete'])
def delete_user(user_id):
    db = Database()
    sql = f"""
    delete  from user where id = {user_id}
    """
    db.execute(sql)
    db.close()

    return success("删除成功")




if __name__ == '__main__':
    app.run(debug=True)
