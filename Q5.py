def k_mer(dna, k):
    dictionary = {}

    for count in dna:
        kmer = read[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer]+=1
    return counts


if __name__ == "__main__":
    dna_input = input("Enter DNA:")
    k_mers = int(input("Enter Kmers:"))
    print(k_mer(dna_input, k_mers))
                






