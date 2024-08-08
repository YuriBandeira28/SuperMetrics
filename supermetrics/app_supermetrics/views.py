from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponse
import folium.map
from .banco_funcs import get_df, get_df_mapa
import folium
from folium.plugins import HeatMap
from folium import plugins

def dashboard(request: HttpRequest):

    df_mapa = get_df_mapa()
    
    map = folium.Map(location=[-27.358563288481317, -53.39957273825672], zoom_start=12)
    dados_mapa = df_mapa[['latitude', 'longitude', 'total_compras']].values.tolist()
    HeatMap(dados_mapa, radius=20).add_to(map)
    mapa = map._repr_html_()
    dados = {
        'mapa':mapa
    }
    return render(request , "dashboard.html", dados)
