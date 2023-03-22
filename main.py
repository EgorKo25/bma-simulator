import internal.bma         as bma
import internal.graphics    as gh
import internal.randomByte  as rb

if __name__ == "__main__":
    X = []
    Y = []

    length = int(input("Enter a length of seq: "))
    seq = "1"

    while len(seq) < length:
        f_min = bma.BerlekampMasseyAlgorithm(bma.Seq2list(sequence=seq))
        X.append(len(seq))
        Y.append(max(f_min))
        seq += rb.randomByte()
        print(f"Processing: {int(len(seq) / length * 100)}%", end="\r")



    print("\nPROCESSED")
    gh.graphCreater(X, Y)







