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
    engine.dispose()

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
                    and s.trabairro not in ('INTERIOR', 'RURAL')
                group by 
                    s.trabairro, 
                    s.munnom,
                    b.latitude,
                    b.longitude
                having count(distinct s.nfnumero) >=200
                order by count(*) desc"""

    df = pd.read_sql(sql, engine)
    engine.dispose()

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
    engine.dispose()

    return df

def get_df_pizza():
    engine = create_engine()

    sql = """select 
                (select 
                    count(distinct s2.nfnumero) 
                from 
                    supermercado s2
                where 
                    s2.trabairro not in ('INTERIOR', 'RURAL')
                    and s2.nfforcod <> 9999
                ) as "Compras na cidade",
                (select 
                    count(distinct s3.nfnumero) 
                from 
                    supermercado s3
                where 
                    s3.trabairro in ('INTERIOR', 'RURAL')
                    and s3.nfforcod <> 99999
                ) as "Compras no interior"
            from 
                supermercado s 
            limit 1"""
    df = pd.read_sql(sql, engine)
    df = df.melt(var_name='Nome', value_name='Valor')
    engine.dispose()
    return df
def get_df_brarras():
    engine = create_engine()

    sql = """select
                s.munnom as "Cidade",
                count(distinct s.nfnumero) as "Total de Compras",
                case
                    when s.trabairro in ('INTERIOR', 'RURAL') then 'Interior'
                    when s.trabairro not in ('INTERIOR', 'RURAL') then 'Cidade'
                end as tipo
            from 
                supermercado s 
            where s.nfforcod <> 99999
            group by
                s.munnom,
                tipo
            having count(distinct s.nfnumero) >=200"""
    df = pd.read_sql(sql, engine)
    engine.dispose()
    return df

def get_compras_produto():
    engine = create_engine()

    sql = """select 
                s.subnom as "Produto",
                count(distinct s.nfnumero) as "Total de Compras"
            from supermercado s
            where 
                s.nfforcod <> 99999
                and extract (month from s.nfdatemis) = 6
            group by 
                s.subnom
            having count(distinct s.nfnumero) >=500
            order by "Total de Compras" desc"""
    df = pd.read_sql(sql, engine)
    engine.dispose()
    return df