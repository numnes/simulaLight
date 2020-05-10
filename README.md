# Simula Light
Versão simplificada do gerador de visualizações espaço temporarais
de simulações de espalhamento de Influenza geradas em [Influenza](https://github.com/matheusnunesismael/Influenza).

## Utilização
Para utilizar clone o projeto para uma pasta ao lado da pasta do repositorio Influenza.

### Pacotes
Execute o comando abaixo para instalar os pacotes nescessarios para rodar o projeto:
```
pip install pandas geopandas matplotlib geopandas contextily imageio pygifsicle
```
### Execução

Nas descrições abaixo onde **X** representa o indice da simulação.

O arquivo geradorImagens.py gera as imagens a partir do arquivo .csv gerado na simulação, localizado na pasta Influenza/Saidas/MonteCarlo_**X**/Simulacao_0/Espacial_Humanos.csv, as imagens são salvas por padrão na pasta Influenza/Espaciais/**X**/. O arquivo recebe dois parametros de entrada sendo o primeiro o numero de ciclos das simulações a serem processadas e o segundo o numero de simulações.

Já o arquivo geradorGifs.py gera gifs a partir das imagens geradas pelo arquivo geradorImagens.py os gifs são salvos na pasta InfluenzaEspaciais/gifs e identificados por **X**.gif. O arquivo também recebe dois parametros que representam os valores de numero de ciclos e de simulações, assim como o arquivo anterior.

O arquivo launcher.sh serve para automatizar o processo de geração dos resultados, quando executado ele exclui a pasta Espaciais executa a geração de imagens e gifs para todas as simulações, ele recebem como parametros o numero de simulações e o numero de ciclos que elas pssuem.
