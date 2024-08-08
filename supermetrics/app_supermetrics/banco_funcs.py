import sqlalchemy
import pandas as pd

def create_engine():
    engine = sqlalchemy.create_engine('postgresql://postgres:postgres@192.168.6.16:5432/ppi')
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
                s.munnom, 
                s.trabairro,
                b.latitude,
                b.longitude,
                count(*) as total_compras
            from 
                supermercado s 
            inner join bairros b 
                on b.bairro = s.trabairro and b.cidade = s.munnom 
            where 
                b.latitude is not null
                and b.longitude is not null
            group by 
                s.trabairro, 
                s.munnom,
                b.latitude,
                b.longitude
            having count(*) > 500
            order by count(*) desc"""

    df = pd.read_sql(sql, engine)

    return df
