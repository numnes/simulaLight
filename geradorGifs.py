from sys import argv
import imageio

def main():
    nciclos = int(argv[1])
    if len(argv) > 2:
        nsimulacoes = int(argv[2])
    else:
        nsimulacoes = 1
    
    filenames = []
    for i in range(nciclos):
        filename = "../Influenza/Espaciais/0/"+str(i)+".png"
        filenames.append(filename)

    with imageio.get_writer('../Influenza/Espaciais/0/movie.gif', mode='I', duration=0.05) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)


if __name__ == '__main__': main()
