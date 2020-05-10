import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx
from sys import argv
import sys
'''
    Gera as imagens com as visualizações dos dados espaciais
    recebe em:
    argv[1] <- o numero de ciclo nas simulações
    argv[2] <- o numero de simulações
'''
def main():
    if len(argv) == 1:
        print("Erro: insira o numero de ciclos e o numero de simulações")
        sys.exit(0)
    nciclos = int(argv[1])
    if len(argv) == 3:
        nsimulacoes = int(argv[2])
    else:
        nsimulacoes = 1

    # Leitura do shapefile do mapa, que é armzenado em um geodataframe
    map_df = gpd.read_file("cascavel/cascavelPol.shp")

    # numero de colunas antes das colunas dos ciclos, referentes as coordenadas
    base = 2
    # vetor com os codigos referentes aos individuos infectados
    infectdCodes = [2044, 2054, 2014, 2024, 2034, 2064]

    #geração das visualizações para cada simulação
    for simulacao in range(nsimulacoes):
        # Carrega a tabela com os dados espaciais da simulação
        path_tabela = "../Influenza/Saidas/MonteCarlo_"+str(simulacao)+"/Simulacao_0/Espacial_Humanos.csv"
        tabela = pd.read_csv(filepath_or_buffer=path_tabela, sep=";", header=None)
        # Carrega o ultimo ciclo para plota-lo de forma invisivel em todos os ciclos 
        #  apenas para manter o enquadramento
            #############################
        coordenadasEnquadramentoE = [list(filter(lambda x: tabela[(nciclos-1)+base][x[0]] in infectdCodes, enumerate(tabela[0].tolist()))), list(filter(lambda x: tabela[(nciclos-1)+base][x[0]] in infectdCodes, enumerate(tabela[1].tolist())))]
        coordenadasEnquadramento = [[item[1] for item in coordenadasEnquadramentoE[0]], [item[1] for item in coordenadasEnquadramentoE[1]]]
        enquadramento = pd.DataFrame({'latitude': coordenadasEnquadramento[0],'longitude': coordenadasEnquadramento[1]})
        geo_enquadramento = gpd.GeoDataFrame(enquadramento, geometry=gpd.points_from_xy(enquadramento.latitude, enquadramento.longitude))
        geo_enquadramento.crs = {'init' :'epsg:31982'}
        geo_enquadramento_t = geo_enquadramento.to_crs({'init': 'epsg:3857'})
        enquadra = geo_enquadramento_t.buffer(30)
            #############################
        for ciclo in range(nciclos):
            # filtra somente as coordenadas dos individuos que tem codigo de infectado
            coordenadasFE = [list(filter(lambda x: tabela[ciclo+base][x[0]] in infectdCodes, enumerate(tabela[0].tolist()))), list(filter(lambda x: tabela[ciclo+base][x[0]] in infectdCodes, enumerate(tabela[1].tolist())))]
            coordenadasF = [[item[1] for item in coordenadasFE[0]], [item[1] for item in coordenadasFE[1]]]
            # passa as coordenadas para uma estrutura de dataframe
            df = pd.DataFrame({
                'latitude': coordenadasF[0],
                'longitude': coordenadasF[1]
            })
            # transforma o CRS (Sitetma de refencimento de coordenadas) do mapa e dos pontos
            gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.latitude, df.longitude))
            gdf.crs = {'init' :'epsg:31982'}
            gdft = gdf.to_crs({'init': 'epsg:3857'})
            df = map_df.to_crs(epsg=3857)
            # configura o estilo do mapa e dos pontos, o tamanho dos pontos no parametro 'buffer' e plota ambos
            ax = df.plot(figsize=(5, 5), alpha=0.5, edgecolor='green', color='white')
            circles = gdft.buffer(30)
            circles.plot(ax=ax, color='red', alpha=1)
            # Plota o ultimo ciclo para garantir o enquadramento
            enquadra.plot(ax=ax, color='red', alpha=0)
            # remove os eixos e as bordas
            ax.set_axis_off()
            plt.axis('off')
            # adiciona o OpenStreetMap ao fundo
            ctx.add_basemap(ax)
            path = "../Influenza/Espaciais/"+str(simulacao)+"/"+str(ciclo)+".png"
            # salva a figura com bordas reduzidas
            plt.savefig(path, dpi=300, bbox_inches='tight')
            # limpa a imagem e fecha os dados carregados para evitar estouro de memoria
            plt.clf()
            plt.close()
if __name__ == '__main__': main()