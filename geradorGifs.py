from sys import argv
from pygifsicle import optimize
import imageio

def main():
    nciclos = int(argv[1])
    if len(argv) > 2:
        nsimulacoes = int(argv[2])
    else:
        nsimulacoes = 1
        
    for simulacao in range(nsimulacoes):
        filenames = []
        for ciclo in range(nciclos):
            filename = "../Influenza/Espaciais/"+str(simulacao)+"/"+str(ciclo)+".png"
            filenames.append(filename)

        gif_path = "../Influenza/Espaciais/"+str(simulacao)+"/movie.gif"

        with imageio.get_writer(gif_path, mode='I', duration=0.3) as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
        optimize(gif_path)


if __name__ == '__main__': main()
