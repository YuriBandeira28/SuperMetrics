# SuperMetrics
Um projeto de relatórios para supermercados utilizando análise de dados

# Objetivos
O projeto foi todo construído para forcener uma visão estratégica de dados de supermercados

# Funcionalidades
Hoje, o projeto conta com 5 gráficos distintos e um mapa de calor, o que facilita na visualização dos dados.

São eles:
- Quantidade de compras por mês
- Total de compras dia do mês
- Receita total por localidade
- Quantidade de compras por localidade, separados por cidade
- Quantidade de compras por produto no útlmo mês, separados por produto
- Quantidade de compras por bairro 


# Tecnologias utilizadas
O projeto foi todo construído utilizando Python, com framwork Django, juntamente com algumas bibliotécas como
- [Pandas](https://pandas.pydata.org/)
  - Para análise dos dados
- [Plotly](https://plotly.com/)
  - Para plotagem de gráficos
- [Folium](https://python-visualization.github.io/folium/latest/)
  - Com o plugin de HeatMap para geração do mapa de calor
- [PostgresSQL](https://www.postgresql.org/)
  - Como banco de dados  

# Se você quiser usar
Certifique-se de ter todas as técnologias utilizadas instaladas em sua máquina

## Clonando o repositório
```bash
git clone https://github.com/YuriBandeira28/SuperMetrics.git
```

## Inicinado o projeto
Certifique-se de configurar o IP de seu banco de dados no arquivo ```config.py``` 

Após isso, rode o comando 
 ```python
python manage.py runserver
``` 


