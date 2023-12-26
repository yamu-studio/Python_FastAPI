import sqlite3

con = sqlite3.connect("db/common.db")
cur = con.cursor()


def get_user(user_id: int):
  print(111222)
  sql = 'select * from users where userID = ? '
  query = (user_id, )
  print(cur.execute(sql,query))
  return cur.execute(sql,query)


def get_user_by_name(name: str):
  sql = 'select * from users where name = ? '
  query = (name, )
  return cur.execute(sql,query)


def create_user(user_id:int):
  cur.execute('INSERT INTO users(userID) values(${user_id})')
  con.commit()

  # データベースへコミット。これで変更が反映される。
  return user_id


def close_db():
  # データベースへのコネクションを閉じる。(必須)
  cur.close()
  con.close()