import pandas as pd
import folium
import kagglehub
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import math

def format_population(num):
    if num < 1000:
        return str(int(num))
    
    # Descobre a magnitude (3 para milhares, 6 para milhões)
    magnitude = int(math.floor(math.log10(num) / 3) * 3)
    
    if magnitude == 3:
        suffix = "k"
    elif magnitude >= 6:
        suffix = "M"
    else:
        suffix = ""
        
    val = num / (10 ** magnitude)
    
    # Se o número terminar em .0, remove o ponto flutuante
    return f"{int(val)}{suffix}" if val.is_integer() else f"{val:.1f}{suffix}"

path = kagglehub.dataset_download("juanmah/world-cities") + r"\worldcities.csv"
df = pd.read_csv(path)
cols = ["city", "country", "lat", "lng", "population", "capital"]
geo = df[cols]
geo["population"] = geo["population"].fillna(0)
geo = geo.dropna(subset="capital")
geo = geo[geo["capital"] != "minor"]
geo = geo[geo["capital"] != "admin"]


# Criação do mapa
m = folium.Map(
    location=[20, 0], 
    zoom_start=3, 
    min_zoom=2,
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}", 
    attr="Esri",
    world_copy_jump=True
)

limites_manuais = [[-85, -18000], [85, 18000]]
m.options['maxBounds'] = limites_manuais

# Adiciona os markers triplicados para cobrir o mundo central e os vizinhos imediatos
for i in range(len(geo)):
    lat = geo.iloc[i]["lat"]
    lng = geo.iloc[i]["lng"]
    city = geo.iloc[i]["city"]
    country = geo.iloc[i]["country"]
    pop = format_population(geo.iloc[i]["population"])
    
    texto_popup = f"{city} in {country}, {pop} habitants"
    
    # Marcador no Mundo Central (0)
    folium.Marker(
        location=[lat, lng],
        popup=texto_popup
    ).add_to(m)
    
    # Marcador no Mundo Leste (+1) -> Deslocado 360 graus para a direita
    folium.Marker(
        location=[lat, lng + 360],
        popup=texto_popup
    ).add_to(m)
    
    # Marcador no Mundo Oeste (-1) -> Deslocado 360 graus para a esquerda
    folium.Marker(
        location=[lat, lng - 360],
        popup=texto_popup
    ).add_to(m)

m.save("meu_mapa.html")

# Transforma o mapa em texto HTML/JavaScript puro
mapa_html = m._repr_html_()

# Inicializa a janela Desktop do PyQt
app = QApplication(sys.argv)
janela = QMainWindow()
janela.setWindowTitle("Meu Mapa Desktop")

# Cria o componente de navegação e joga o HTML do mapa lá dentro
visualizador = QWebEngineView()
visualizador.setHtml(mapa_html)

janela.setCentralWidget(visualizador)

# Define o tamanho na proporção ideal que você escolheu
janela.setFixedSize(1280, 720)

janela.show()

sys.exit(app.exec_())