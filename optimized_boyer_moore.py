def optimized_boyer_moore(p, p_bm, t):
    """Do Boyer-Moore matching (optimized version).

    Args:
        p (str): The pattern string.
        p_bm (BoyerMoore): A preprocessed Boyer-Moore object for the pattern.
        t (str): The text in which to search for the pattern.

    Returns:
        list: A list of starting indices where the pattern is found in the text.
    """
    m = len(p)
    n = len(t)
    i = 0
    occurrences = []
    
    while i <= n - m:
        shift = 1
        mismatched = False
        # Compare pattern p and text t from rightmost end of p
        for j in range(m - 1, -1, -1):
            if p[j] != t[i + j]:
                skip_bc = p_bm.bad_character_rule(j, t[i + j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            # On a full match, determine shift based on the match skip rule.
            shift = max(shift, p_bm.match_skip())
        i += shift
    return occurrences