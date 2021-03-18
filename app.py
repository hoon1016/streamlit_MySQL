import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date,time


def main():

    # name = st.text_input('이름을 입력하세요')
    # birth_date = st.date_input('생년월일')
    # birth_time = st.time_input('시간입력')
    # date_time = datetime.combine(birth_date,birth_time)
    # print(birth_date)
    # print(birth_time)
    # print(date_time) 
    
    if st.button('저장하기'):
    
        try :
            # 1. 커넥터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.c8incbwwf4p9.us-east-2.rds.amazonaws.com',
                database = 'yhbe',
                user ='streamlit',
                password = 'djaak1234'
            ) 

            if connection.is_connected() :
                print('연결됬을때')
                be_info = connection.get_server_info()
                print("MySQL servar version : ",be_info)

                #2.커서를 가져온다.
                cursor = connection.cursor()

                print('커서 가져온것 후')
                #3. 우리가 원하는거 실행 가능
            
                query = '''insert into cats4 (name,age)
                            values (%s,%s);'''
            
                record = [('냐옹이',1),('나비',3),('또기',5)]
                print(datetime.now())
                
                cursor.executemany(query,record)
                connection.commit()
            
                print("{}개 적용됨".format(cursor.rowcount))
           
                #4. 실행 후 커서에서 결과를 빼낸다.
                # record = cursor.fetchone()
                # print('Connected to be : ', record)
    
        except Error as e :
            print('디비 관련 에러 발생',e)
        finally :
            #5. 모든 데이터 베이스 실행 명령을 전부 끝냈으며,
            #       커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print("MySQL 커넥션 종료")




if __name__ =='__main__':
    main()