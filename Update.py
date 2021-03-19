import streamlit as st
import mysql.connector
from mysql.connector import Error


def run_Update():
    
    book_id_list = []
    
    try :
        # 1. 커넉터로부터 커넥션을 받는다.
        connection = mysql.connector.connect(
        host = 'database-1.c8incbwwf4p9.us-east-2.rds.amazonaws.com',
        database = 'yhbe',
        user = 'streamlit',
        password = 'djaak1234'
    )
            
        if connection.is_connected() :
            cursor = connection.cursor(dictionary= True)        
        
            query = """ select *
                        from books limit 5;"""
            cursor.execute(query)

            results = cursor.fetchall()

            

            for row in results:
                st.write(row)
                book_id_list.append(row['book_id'])

    except Error as e :
        print('디비 관련 에러 발생', e)
        
    finally :
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")
    

    
    book_id = st.number_input('책 아이디 입력',min_value=book_id_list[0],max_value=book_id_list[-1])
    
    stock_quantity = st.number_input('수량 입력',min_value=0)

    pages = st.number_input('페이지 입력',min_value=1)

    author_fname = st.text_input('작가 이름 입력')

    author_lname = st.text_input('작가 성 입력')

    title = st.text_input('책 제목 입력') 
    
    
    if st.button('책 정보 업데이트'):
        
        try :
            # 1. 커넉터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.c8incbwwf4p9.us-east-2.rds.amazonaws.com',
                database = 'yhbe',
                user = 'streamlit',
                password = 'djaak1234'
            )
            
            if connection.is_connected() :
                            
                # 2. 커서를 가져온다.
                cursor = connection.cursor()           
                query =  '''update books
                            set pages = %s, stock_quantity = %s,author_fname = %s,author_lname = %s, title = %s
                            where book_id = 1;'''

                pages = 201
                stock_quantity = 51
                book_id =2        
                data = (pages,stock_quantity,author_fname,author_lname,title)

                cursor.execute(query,data)

                connection.commit()



        except Error as e :
            print('디비 관련 에러 발생', e)
        
        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
            #    커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print("MySQL 커넥션 종료")
