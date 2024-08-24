from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponse, JsonResponse
import folium.map
from .banco_funcs import get_df_mapa, get_df_compras_dia, get_df_pizza, get_df_brarras, get_compras_produto, get_df_compras_mes
import folium
from folium.plugins import HeatMap
from folium import plugins
from .utils.processamento_dados import abrevia_cidade, cria_grafico_compras_dia_mes, cria_grafico_pizza, cria_grafico_barras, cria_grafico_produtos, cria_grafico_compras_mes, mapeia_meses

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


    df_grafico_pizza = get_df_pizza()
    grafico_pizza = cria_grafico_pizza(df_grafico_pizza)

    df_grafico_compras_mes = get_df_compras_mes()

    df_grafico_compras_mes['Mês'] = df_grafico_compras_mes['Mês'].astype(int)
    df_grafico_compras_mes['mes_string'] = df_grafico_compras_mes['Mês'].apply(mapeia_meses)
    meses = df_grafico_compras_mes['mes_string'].to_list()


    grafico_compras_mes = cria_grafico_compras_mes(df_grafico_compras_mes)


    print(df_grafico_compras_mes)
    df_grafico_barras = get_df_brarras()
    grafico_barras = cria_grafico_barras(df_grafico_barras)

    df_grafico_produtos = get_compras_produto()
    grafico_produtos = cria_grafico_produtos(df_grafico_produtos)
    dados = {
        'mapa':mapa,
        'meses':meses,
        'grafico_mes': grafico_compras_mes,
        'grafico_pizza': grafico_pizza,
        'realtorio_mapa': realtorio_mapa,
        'grafico_barras': grafico_barras,
        'grafico_produtos': grafico_produtos,
    }
    return render(request , "dashboard.html", dados)


def compras_dia(request: HttpRequest):

    if request.method == 'POST':
        mes = request.POST.get('mes')
        df_grafico_dias_mes = get_df_compras_dia(mes)
        grafico_compras_dia = cria_grafico_compras_dia_mes(df_grafico_dias_mes)

        return JsonResponse(grafico_compras_dia, safe=True)