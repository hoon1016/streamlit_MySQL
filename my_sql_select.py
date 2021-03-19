import streamlit as st
import mysql.connector
from mysql.connector import Error

import numpy as np
import pandas as pd
import json

def my_sql_select() :
    
    column_list = ['title', 'author_fname','author_lname','released_year', 'stock_quantity','pages']
    
    selected_column_list = st.multiselect("컬럼을 선택하세요.", column_list)

    if len(selected_column_list) == 0 :
        query = """ select * from books;  """
    else :
        column_str = ', '.join(selected_column_list)
        # st.write(column_str)
        query = "select book_id, " + column_str + ' from books;'
        # st.write(query)

    # st.write(query)

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

            # 2. 쿼리 만들어서 실행
            cursor.execute(query)

            # 3. select 이므로, fetchall 한다.
            results = cursor.fetchall()

            st.write(type(results))
            st.write(results)

            # 파이썬의 리스트+딕셔너리 조합을 => JSON 형식으로 바꾸는것.
            json_results = json.dumps(results)

            # 판다스의 데이터프레임으로 읽기.
            df = pd.read_json(json_results)

            st.dataframe(df)

            # st.write(type(json_results))
            # st.write(json_results)



            # for row in results :
            #     st.write(row)
            

    except Error as e :
            print('디비 관련 에러 발생', e)
        
    finally :
            cursor.close()
            connection.close()
            print("MySQL 커넥션 종료")
