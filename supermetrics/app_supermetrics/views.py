from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponse
import folium.map
from .banco_funcs import get_df_mapa, get_df_compras_dia, get_df_pizza, get_df_brarras, get_compras_produto
import folium
from folium.plugins import HeatMap
from folium import plugins
from .utils.processamento_dados import abrevia_cidade, cria_grafico_compras_dia_mes, cria_grafico_pizza, cria_grafico_barras, cria_grafico_produtos

def dashboard(request: HttpRequest):

    df_mapa = get_df_mapa()
    
    map = folium.Map(location=[-27.358563288481317, -53.39957273825672], zoom_start=13, height='100%')
    dados_mapa = df_mapa[['latitude', 'longitude', 'total_compras']].values.tolist()
    HeatMap(dados_mapa, radius=40).add_to(map)
    mapa = map._repr_html_()
    df_relatorio = df_mapa

    df_relatorio['cidade_abreviada'] = df_relatorio['munnom'].apply(abrevia_cidade)
    df_relatorio = df_relatorio.sort_values(by='total_compras', ascending=False)
    realtorio_mapa = df_relatorio.to_dict('records')

    df_grafico_dias_mes = get_df_compras_dia()
    grafico = cria_grafico_compras_dia_mes(df_grafico_dias_mes)
    df_grafico_pizza = get_df_pizza()
    grafico_pizza = cria_grafico_pizza(df_grafico_pizza)

    df_grafico_barras = get_df_brarras()
    grafico_barras = cria_grafico_barras(df_grafico_barras)

    df_grafico_produtos = get_compras_produto()
    grafico_produtos = cria_grafico_produtos(df_grafico_produtos)
    dados = {
        'mapa':mapa,
        'grafico': grafico,
        'grafico_pizza': grafico_pizza,
        'realtorio_mapa': realtorio_mapa,
        'grafico_barras': grafico_barras,
        'grafico_produtos': grafico_produtos,
    }
    return render(request , "dashboard.html", dados)
