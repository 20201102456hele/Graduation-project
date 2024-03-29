from flask import Flask, request
import jieba
from db import Database
from util import success, error
from xinghuo.run import begin

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


# 获取评论数据
@app.route('/api/comment', methods=['GET'])
def get_comment():
    software_name = request.args.get("name", None)

    db = Database()

    if software_name:
        sql = f"""
        select * from comment  where name = '{software_name}'
        """
    else:
        sql = f"""
                select * from comment
                """
    res = db.fetchall(sql)
    db.close()

    return success(res)


# 获取评论数据 词云数据
@app.route('/api/ciyun', methods=['GET'])
def get_ciyun():
    software_name = request.args.get("name", None)
    db = Database()
    if software_name:
        sql = f"""
        select * from comment  where name = '{software_name}'
        """
    else:
        sql = f"""
                select * from comment
                """
    res = db.fetchall(sql)
    db.close()

    texts = ""
    for i in res:
        texts += i["info"]
    cut_ls = jieba.lcut(texts)  # 分词

    # 统计词频
    data = []
    counts = {}
    for i in cut_ls:
        if i in ["支付宝", "微信", "QQ", "爱奇艺", "抖音","APP","app","退"]:
            continue
        if len(i) > 1:
            counts[i] = counts.get(i, 0) + 1
            data.append({"value": counts.get(i, 0) + 1, "name": i})
    return success(data)


# 获取评论数据, 词云数据
@app.route('/api/ciyunData', methods=['GET'])
def get_ciyun_data():
    software_name = request.args.get("name", None)
    stop_data = []
    with open("stopwords.txt", encoding="utf8") as f:
        stop_data = f.readlines()
    good_data = []
    bad_data = []
    # 统计词频
    good_counts = {}
    bad_counts = {}
    for pl in ["好评", "差评"]:
        if software_name:
            sql = f"""
            select * from comment  where name = '{software_name}' and comment_type = '{pl}'
        """
        else:
            sql = f"""
            select * from comment where comment_type = '{pl}'
            """
        db = Database()
        res = db.fetchall(sql)
        db.close()

        texts = ""
        for i in res:
            texts += i["info"]
        cut_ls = jieba.lcut(texts)  # 分词

        stop_data = [i.replace("\n", "") for i in stop_data]
        for i in cut_ls:
            if i in["支付宝","微信","QQ","爱奇艺","抖音","APP","app"]:
                continue
            if i in stop_data or i in [" ", "\n"]:
                continue
                print(i)
            if pl == "好评":
                if i in ["特效", "购物", "色彩", "花呗", "照片", "表情", "优惠", "种树", "付款", "创业", "支付", "社交", "清晰", "弹幕"]:
                    if good_counts.get(i) is None:
                        good_counts[i] = 0
                    good_counts[i] += 1
            if pl == "差评":
                if i in ["封号", "没有声音",  "卡", "广告", "更新", "闪退", "内存"]:
                    if bad_counts.get(i) is None:
                        bad_counts[i] = 0
                    bad_counts[i] += 1

    sorted_good_data = sorted(good_counts.items(), key=lambda x: x[1], reverse=True)

    sorted_bad_data = sorted(bad_counts.items(), key=lambda x: x[1], reverse=True)


    return success({
        "godDataX": [i[0] for i in sorted_good_data[: 20]],
        "godDataY": [i[1] for i in sorted_good_data[: 20]],
        "badDataX": [i[0] for i in sorted_bad_data[: 20]],
        "badDataY": [i[1] for i in sorted_bad_data[: 20]]}

    )


# 获取评论数据 好评 差评
@app.route('/api/comment_type', methods=['GET'])
def get_comment_type():
    software_name = request.args.get("name", None)

    db = Database()
    if software_name:
        sql = f"""
        select * from comment  where name = '{software_name}'
        """
    else:
        sql = f"""
                select * from comment
                """
    res = db.fetchall(sql)
    db.close()

    good_num = 0
    bad_num = 0
    for i in res:
        if i["comment_type"] == "好评":
            good_num += 1
        if i["comment_type"] == "差评":
            bad_num += 1

    return success({"dataX": ["好评", "差评"], "dataY": [good_num, bad_num]})


# 新增评论数据
@app.route('/api/add/comment', methods=['POST'])
def add_comment():
    json_data: dict = request.get_json()
    name = json_data.get("name")
    comment_info = json_data.get("comment")
    stars = 1
    comment_type = json_data.get("commentType")

    db = Database()
    sql = f"""
    insert into comment (name, info, stars, comment_type) values ('{name}', '{comment_info}', '{stars}', '{comment_type}');
    """
    res = db.execute(sql)
    db.close()

    return success(res)


@app.route('/api/analysis/comment', methods=['POST'])
def analysis_comment():
    json_data: dict = request.get_json()
    comment = json_data.get("comment")
    comment_type = begin(comment)
    return success(comment_type)


# 新增反馈意见
@app.route('/api/add/opinion', methods=['POST'])
def add_opinion():
    json_data: dict = request.get_json()
    user = json_data.get("user")
    software = json_data.get("software")
    info = json_data.get("info")

    db = Database()
    sql = f"""
    insert into opinion (user, software, info) values ('{user}', '{software}', '{info}');
    """
    res = db.execute(sql)
    db.close()

    return success(res)


# 获取反馈意见
@app.route('/api/opinion', methods=['GET'])
def get_opinion():
    software = request.args.get("software", None)

    db = Database()
    if software:
        sql = f"""
        select * from opinion  where software = '{software}'
        """
    else:
        sql = f"""
                select * from opinion
                """
    res = db.fetchall(sql)
    db.close()

    return success(res)


if __name__ == '__main__':
    app.run(debug=True)
