from pymongo import MongoClient
# 实例化client，建立连接

client = MongoClient(host='127.0.0.1',port=27017)
collection = client['douban']['t255']

# 插入一条数据
# ret1 = collection.insert({"name":"王昭君", "age":24})
# print(ret1)  # 返回_id

# 插入多条数据
# data_list = [{"name":"test{}".format(i)} for i in range(10)]
# collection.insert_many(data_list)

# 查询一个记录
# t = collection.find_one({"name":"王昭君"})
# 查询所有记录
t = collection.find({"name":"王昭君"})
print(t)  # 返回游标对象
print(list(t))

# 更新数据
collection.update({"name":"test8"},{"$set":{"name":"test100000"}})
# 更新多条
# collection.update_many()
# 删除数据
collection.delete_one({"name":"test7"})
# 删除多条数据
collection.delete_many({"name":"test2"})