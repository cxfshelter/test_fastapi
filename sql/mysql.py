TORTOISE_ORM = {
    # 数据库连接信息
    "connections": {"default": "mysql://root:123654@127.0.0.1:3306/testdb"},
    # 指定有哪些应用
    "apps": {
        "models": {
            # 指明应用下存放模型类的位置，比如test.models就是在test包下的models文件中存放了模型类
            # 这里可以写自己模型类存放位置。
            "models": ["aerich.models", "sql.models"],  # aerich.models是必须写的，写了之后会去找到对应的模型类然后创建一个迁移记录表。
            "default_connection": "default",
        },
    },
}


### 常用指令说明 ###

# 初始化ORM
# aerich init -t sql.mysql.TORTOISE_ORM

# 初始化数据库 (迁移记录)
# aerich init-db

######

# orm代码 -> db
# aerich migrate

# 执行
# aerich upgrade

######

# db -> orm代码
# aerich --app models inspectdb

# 指定表
# aerich inspectdb -t user > models.py

