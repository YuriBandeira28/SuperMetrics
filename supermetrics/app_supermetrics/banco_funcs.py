import sqlalchemy
import pandas as pd
import supermetrics.config
def create_engine():
    # engine = sqlalchemy.create_engine('postgresql://postgres:postgres@192.168.6.16:5432/ppi')
    engine = sqlalchemy.create_engine(f'postgresql://postgres:postgres@{supermetrics.config.bd_url}:5432/ppi')
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
                    count(distinct s.nfnumero) as total_compras
                from 
                    supermercado s 
                inner join bairros b 
                    on b.bairro = s.trabairro and b.cidade = s.munnom 
                where 
                    b.latitude is not null
                    and b.longitude is not null
                    and s.nfforcod <> 99999
                group by 
                    s.trabairro, 
                    s.munnom,
                    b.latitude,
                    b.longitude
                having count(distinct s.nfnumero) >=200
                order by count(*) desc"""

    df = pd.read_sql(sql, engine)

    return df


def get_df_compras_dia():
    engine = create_engine()

    sql = """select 
                extract (day from s.nfdatemis) as "Dia do Mês",
                count(distinct s.nfnumero) as "Total de Compras"
            from 
                supermercado s 
            where  
                s.nfforcod <> 99999
            group by extract (day from s.nfdatemis)"""
    df = pd.read_sql(sql, engine)

    return df
