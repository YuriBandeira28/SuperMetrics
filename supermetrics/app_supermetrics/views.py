from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponse
import folium.map
from .banco_funcs import get_df_mapa, get_df_compras_dia
import folium
from folium.plugins import HeatMap
from folium import plugins
from .utils.processamento_dados import abrevia_cidade, cria_grafico

def dashboard(request: HttpRequest):

    df_mapa = get_df_mapa()
    
    map = folium.Map(location=[-27.358563288481317, -53.39957273825672], zoom_start=13, height='100%')
    dados_mapa = df_mapa[['latitude', 'longitude', 'total_compras']].values.tolist()
    HeatMap(dados_mapa, radius=20).add_to(map)
    mapa = map._repr_html_()
    df_relatorio = df_mapa
    # df_relatorio['cidade_abreviada'] = df_relatorio['munnom'].str.strip(' ')[0]

    df_relatorio['cidade_abreviada'] = df_relatorio['munnom'].apply(abrevia_cidade)
    df_relatorio = df_relatorio.sort_values(by='total_compras', ascending=False)
    realtorio_mapa = df_relatorio.to_dict('records')
    # df_grafico = df_mapa[['trabairro', 'munnom', 'total_compras']]
    # df_grafico = df_grafico.rename(columns={
    #     'trabairro': 'Bairro',
    #     'munnom': 'Cidade',
    #     'total_compras': "Total de Compras"
    # })
    df_grafico_dias_mes = get_df_compras_dia()
    grafico = cria_grafico(df_grafico_dias_mes)
    dados = {
        'mapa':mapa,
        'grafico': grafico,
        'realtorio_mapa': realtorio_mapa
    }
    return render(request , "dashboard.html", dados)
