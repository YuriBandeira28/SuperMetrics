from sqlalchemy import create_engine
import pandas as pd

def create_engine():
    engine = create_engine('postgresql://postgres:postgres@192.168.6.16:5432/ppi')
    return engine
def get_df():

    engine = create_engine()
    sql = """select 
                * 
            from 
                supermercado s 
            where
                extract (month from s.nfdatemis) = 6"""
    # sql = "select * from supermercado"

    df = pd.read_sql(sql, engine)

    return df

def get_df_mapa():
    engine = create_engine()

    sql = """select 
                s.munnom, trabairro, count(*)
            from 
                supermercado s 
            group by 
                s.trabairro, s.munnom
            order by 
                count(*) desc"""

    df = pd.read_sql(sql, engine)

    return df
