import plotly.express as px
import pandas as pd

def abrevia_cidade(cidade):
    if len(str(cidade).split(" ")) >1:
        return ''.join([palavra[:1] for palavra in cidade.split()])
    else:
        return cidade
    

def cria_grafico_compras_dia_mes(df: pd.DataFrame):
    fig = px.line(df, x='Dia do Mês', y='Total de Compras')
    fig.update_traces(line=dict(width=3, color='#009245'))   
    fig.update_layout(
        showlegend=False,
        margin=dict(t=100, l=40, r=40),
        autosize=True,
        width = 1000
    )
    return fig.to_html(full_html=False)

def cria_grafico_compras_mes(df: pd.DataFrame):
    fig = px.line(df, x='Mês', y='Total de Compras')
    fig.update_traces(line=dict(width=3, color='#009245'))   
    fig.update_layout(
        showlegend=False,
        margin=dict(t=100, l=40, r=40),
        autosize=True,
        height=600,
        width=550
    )
    return fig.to_html(full_html=False)

def cria_grafico_pizza(df: pd.DataFrame):
    fig = px.pie(df, names=df.columns[0], values=df.columns[1], color_discrete_sequence=["#ffc107", "#009245"])
    fig.update_layout(
        showlegend=True,
        margin=dict(t=100, l=40, r=40),
        autosize=True,
        height=600,
        width=550
    )
    return fig.to_html(full_html=False)

def cria_grafico_barras(df: pd.DataFrame):
    fig = px.bar(df, 
                 x='Cidade', 
                 y='Total de Compras', 
                 color='localidade', 
                 text='Total de Compras', 
                 barmode='stack', color_discrete_sequence=["#ffc107", "#009245"])  
    
    fig.update_layout(
        showlegend=True,
        legend=dict(
            orientation="v", 
            yanchor="top",
            y=1, 
            xanchor="left",
            x=-0.2 
        ),
        autosize=True
    )
    
    return fig.to_html(full_html=False)

def cria_grafico_produtos(df: pd.DataFrame):
    fig = px.bar(df, 
                 x='Produto', 
                 y='Total de Compras', 
                 color='Produto', 
                 barmode='stack')  
    
    fig.update_layout(
        showlegend=True,
        legend=dict(
            orientation="v", 
            yanchor="top",
            y=1, 
            xanchor="left",
            x=-0.5
        ),
        autosize=True
    )
    
    return fig.to_html(full_html=False)


def mapeia_meses(mes: int):

    mapeamento = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    mes = mapeamento[mes]
    return mes

def mapeia_meses2(mes: str):

    mapeamento = {
        'Janeiro': 1,
        'Fevereiro': 2,
        'Março': 3,
        'Abril': 4,
        'Maio': 5,
        'Junho': 6,
        'Julho': 7,
        'Agosto': 8,
        'Setembro': 9,
        'Outubro': 10,
        'Novembro': 11,
        'Dezembro': 12
    }
    mes = mapeamento[mes]
    return mes