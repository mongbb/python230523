# db2.py
import sqlite3

# 연결객체 생성 (물리적인 DB파일에 저장)
con = sqlite3.connect("c:\\WORK\\sample.db")
# 커서객체 리턴 
cur = con.cursor()
# 테이블 구조 생성
cur.execute("create table if not exists PhoneBook " + " (id integer primary key autoincrement, name text, phoneNum text);")
# autoincrement : 자동 번호 생성 명령어

# 1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values " + " ('홍길동','010-111');")

# 파라미터 입력
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values " + " (?,?);", (name, phoneNumber))

# 여러개의 레코드 입력
datalist = (("박문수", "01-023"), ("김길동", "010-567"))
cur.executemany("insert into PhoneBook (name, phoneNum) values " + " (?,?);", datalist)

# 수정 ("update tableName set columnName = ")
cur.execute("update PhoneBook set name = '이길동', PhoneNum='010-189' " + " where id=1;")

# 삭제
cur.execute("delete from PhoneBook where id=2;")

# 검색
cur.execute("select * from PhoneBook;")
'''
for row in cur:
    print(row)
print("----- fetchone() ------")
print( cur.fetchone() )
print("----- fetchmany(2) ------")
print( cur.fetchmany(2) )
print("----- fetchall() ------")
'''
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )

# 작업을 정상적으로 완료
con.commit()