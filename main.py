import internal.bma         as bma
import internal.graphics    as gh
import internal.randomByte  as rb

if __name__ == "__main__":
    X = []
    Y = []

    seq = "1"

    while len(seq) <= 100:
        f_min = bma.BerlekampMasseyAlgorithm(bma.Seq2list(sequence=seq))
        X.append(len(seq))
        Y.append(max(f_min))
        seq += rb.randomByte()
        print(f"Processing: {len(seq)}%", end="\r")

    gh.graphCreater(X, Y)
    """
        print(f"Enter a sequence: {seq}")
        print(f"Minimum multiplicity: {bma.print_f(f_min)}")
        print(f"Minimum number of times: {str(max(f_min))}")
    """






