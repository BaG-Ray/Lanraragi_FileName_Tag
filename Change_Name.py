import os
from re import T
import sqlite3

db = sqlite3.connect(r"") #这里填上Ehviewer导出数据库的绝对地址


def Get_Token(Gid):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT token FROM galleries where gid = " + str(Gid) + ";"
    try:
        cursor.execute(sql)
        token = ((cursor.fetchall())[0])[0]
    except:
        token = None

    print(token)
    return token

if __name__ == "__main__":
    for RootPath, DirPath, FileList in os.walk(r""):    #这里填上漫画目录的绝对地址
        for FileName in FileList:

            Re_FileName_List = FileName.split("-")

            Gid = Re_FileName_List[0]
            print(Gid)

            Token = Get_Token(Gid)

            Re_Name = Re_FileName_List[1:]
            Re_Name_s = '-'.join(Re_Name)

            new_Name = str(Gid) + "-" + str(Token) + "-" + str(Re_Name_s) + ".zip"



            Old_File_Path = os.path.join(RootPath, FileName)
            New_File_Path = os.path.join(RootPath, new_Name)


            try:
                os.rename(Old_File_Path, New_File_Path)
            except:
                continue

