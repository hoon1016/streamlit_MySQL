import streamlit as st
import mysql.connector
from mysql.connector import Error

from my_sql_select import my_sql_select
from insert import run_insert
from Update import run_Update
from Delete import run_Delete
from my_sql_pyplot import run_my_sql_pyplot

def main() :

    menu = ['Select', 'Insert', 'Update', 'Delete','Pyplot']
    choie = st.sidebar.selectbox('메뉴', menu)

    if choie == 'Select' :
        my_sql_select()
    elif choie == 'Insert':
        run_insert()
    elif choie == 'Update':
        run_Update()
    elif choie == 'Delete':
        run_Delete()
    elif choie == 'Pyplot':
        run_my_sql_pyplot()

if __name__ == '__main__' :
    main()




