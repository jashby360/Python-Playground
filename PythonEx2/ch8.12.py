def bioInfo(bio):
    geneSearch = 0
    found = False

    for i in range(len(bio) - 2):
        triple = bio[i: i + 3]  # how to initiate a substring
        if triple == "ATG":
            geneSearch = i + 3
        elif triple == "TAG" or triple == "TAA" or triple == "TGA" and geneSearch != 0:
            gene = bio[geneSearch: i]
            if len(gene) % 3 == 0:
                found = True
                print(gene)
                geneSearch = 0

    if not found:
        print("no gene is found")


def main():
    genome = input("Enter a genome string: ")
    bioInfo(genome)


main()
