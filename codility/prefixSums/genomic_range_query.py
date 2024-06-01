def genomic_range_query(S: str, P: list[int], Q: list[int]):
    """
    A,C, G, T
    impact factor range: 1-4
    You are going to answer several queries of the form:
    What is the minimal impact factor of nucleotides contained in a
    particular part of the given DNA sequence?
    DNA sequence
      * Non-empty string S of N characters
      * M queries, which give a non-empty Array P and Q consisting of M integers
      * The K-th query (0 <= K <= M)
        * find the minimal impact factor of nucleotides contained in the DNA
        sequence between positions P[K] and Q[K] (inclusive)
    Boundaries:
        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P and Q is an integer within the range [0..N - 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T. (no
        need to enforce or validate, will assume all uppercase letters)
    """

    """
     This function preprocesses the DNA sequence S to create prefix sums for each nucleotide,
     allowing for constant-time queries of the minimal impact factor in any given range.
     """
    N = len(S)
    M = len(P)
    # Initialize prefix sums for each nucleotide; each entry holds counts up to that position.
    prefix_sums = {'A': [0] * (N + 1), 'C': [0] * (N + 1), 'G': [0] * (N + 1),
                   'T': [0] * (N + 1)}
    # Build the prefix sums for each nucleotide
    for i, nucleotide in enumerate(S, start=1):
        for key in prefix_sums:
            prefix_sums[key][i] = prefix_sums[key][i - 1] + (1 if nucleotide == key else 0)

    impact_table = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    minimal_impact_factors = []
    # For each query, find the minimal impact factor of nucleotides in the given range
    for i in range(M):
        start, end = P[i], Q[i] + 1  # Adjust end for inclusive range
        # Check each nucleotide in the order of increasing impact factor
        if prefix_sums['A'][end] - prefix_sums['A'][start] > 0:
            minimal_impact_factors.append(1)
        elif prefix_sums['C'][end] - prefix_sums['C'][start] > 0:
            minimal_impact_factors.append(2)
        elif prefix_sums['G'][end] - prefix_sums['G'][start] > 0:
            minimal_impact_factors.append(3)
        elif prefix_sums['T'][end] - prefix_sums['T'][start] > 0:
            minimal_impact_factors.append(4)

    return minimal_impact_factors
