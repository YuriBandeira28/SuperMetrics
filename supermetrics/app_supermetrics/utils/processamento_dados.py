import plotly.express as px


def abrevia_cidade(cidade):
    if len(str(cidade).split(" ")) >1:
        return ''.join([palavra[:1] for palavra in cidade.split()])
    else:
        return cidade
    

def cria_grafico(df):
    fig = px.line(df, x='Dia do Mês', y='Total de Compras')
    fig.update_traces(line=dict(width=3, color='#009245'))   
    fig.update_layout(
        title='Quantidade de compras por dia do mês',
        showlegend=False,
        margin=dict(t=100, l=40, r=40),
        autosize=True,
        height=600,
        width=550
    )
    return fig.to_html(full_html=False)


