import string

def optimized_z_array(s):
    """
    Compute the Z-array for string s using the Z algorithm (Gusfield Theorem 1.4.1).

    The Z-array is defined such that Z[k] is the length of the longest substring
    starting at k that matches a prefix of s.
    """
    n = len(s)
    assert n > 1, "Input string must have length > 1"
    z = [n] + [0] * (n - 1)
    
    # Compute initial z[1] by comparing s[1:] with prefix
    for i in range(1, n):
        if s[i] == s[i - 1]:
            z[1] += 1
        else:
            break

    l, r = (1, z[1]) if z[1] > 0 else (0, 0)
    
    for k in range(2, n):
        if k > r:
            # Case 1: No previous info available; match from scratch.
            while k + z[k] < n and s[z[k]] == s[k + z[k]]:
                z[k] += 1
            if z[k] > 0:
                l, r = k, k + z[k] - 1
        else:
            # Case 2: Use previously computed values.
            beta_length = r - k + 1
            z_k_l = z[k - l]
            if beta_length > z_k_l:
                z[k] = z_k_l
            else:
                # Extend the match beyond r.
                start = r + 1
                while start < n and s[start] == s[start - k]:
                    start += 1
                z[k] = start - k
                l, r = k, start - 1
    return z


def optimized_n_array(s):
    """
    Compute the N-array for string s.
    
    The N-array is constructed by reversing s, computing its Z-array, and then reversing the result.
    """
    return optimized_z_array(s[::-1])[::-1]


def optimized_big_l_prime_array(p, n):
    """
    Compute the L' array for pattern p using its N-array n.
    
    L'[i] = largest index j less than len(p) such that N[j] == |p[i:]|
    """
    m = len(p)
    lp = [0] * m
    for j in range(m - 1):
        i = m - n[j]
        if i < m:
            lp[i] = j + 1
    return lp


def optimized_big_l_array(p, lp):
    """
    Compute the L array for pattern p using the L' array.
    
    L[i] = largest index j less than len(p) such that N[j] >= |p[i:]|
    """
    m = len(p)
    l_arr = [0] * m
    l_arr[1] = lp[1]
    for i in range(2, m):
        l_arr[i] = max(l_arr[i - 1], lp[i])
    return l_arr


def optimized_small_l_prime_array(n):
    """
    Compute the small l' array from the N-array n.
    
    small_l_prime[i] gives the length of the longest substring starting at i that is also a prefix.
    """
    m = len(n)
    small_lp = [0] * m
    for i in range(m):
        if n[i] == i + 1:
            small_lp[m - i - 1] = i + 1
    for i in range(m - 2, -1, -1):
        if small_lp[i] == 0:
            small_lp[i] = small_lp[i + 1]
    return small_lp


def optimized_good_suffix_table(p):
    """
    Compute the tables needed for the good suffix rule for pattern p.
    
    Returns:
        - Big L' array,
        - Big L array,
        - Small l' array.
    """
    n = optimized_n_array(p)
    lp = optimized_big_l_prime_array(p, n)
    return lp, optimized_big_l_array(p, lp), optimized_small_l_prime_array(n)


def optimized_good_suffix_mismatch(i, big_l_prime, small_l_prime):
    """
    Given a mismatch at offset i in the pattern, determine the shift amount based on the good suffix rule.
    
    Args:
        i: The index of mismatch in the pattern.
        big_l_prime: The Big L' array.
        small_l_prime: The small l' array.
    
    Returns:
        The number of positions to shift the pattern.
    """
    m = len(big_l_prime)
    if i == m - 1:
        return 0
    i += 1  # Adjust to point to the leftmost matching position of the pattern.
    if big_l_prime[i] > 0:
        return m - big_l_prime[i]
    return m - small_l_prime[i]


def optimized_good_suffix_match(small_l_prime):
    """
    Given a full match of the pattern in the text, determine the shift amount based on the good suffix rule.
    
    Args:
        small_l_prime: The small l' array.
    
    Returns:
        The number of positions to shift the pattern.
    """
    return len(small_l_prime) - small_l_prime[1]


def optimized_dense_bad_char_tab(p, amap):
    """
    Build a dense bad character table for pattern p given an alphabet mapping (amap).
    
    The table is a list of lists, indexed by pattern position then by character index.
    """
    tab = []
    nxt = [0] * len(amap)
    for i, c in enumerate(p):
        tab.append(nxt.copy())
        nxt[amap[c]] = i + 1
    return tab


class OptimizedBoyerMoore:
    """
    An optimized implementation of the Boyer-Moore string matching algorithm.
    
    This class precomputes the bad character table and good suffix tables for a given pattern.
    """
    
    def __init__(self, p, alphabet='ACGT'):
        self.p = p
        self.alphabet = alphabet
        self.amap = {c: i for i, c in enumerate(alphabet)}
        self.bad_char = optimized_dense_bad_char_tab(p, self.amap)
        _, self.big_l, self.small_l_prime = optimized_good_suffix_table(p)
    
    def bad_character_rule(self, i, c):
        """
        Compute the shift based on the bad character rule given a mismatch at offset i with character c.
        
        Args:
            i: The index of the mismatch in the pattern.
            c: The mismatching character in the text.
        
        Returns:
            The number of positions to shift the pattern.
        """
        ci = self.amap[c]
        return i - (self.bad_char[i][ci] - 1)
    
    def good_suffix_rule(self, i):
        """
        Compute the shift based on the good suffix rule for a mismatch at offset i.
        
        Args:
            i: The index of the mismatch in the pattern.
        
        Returns:
            The number of positions to shift the pattern.
        """
        m = len(self.p)
        if i == m - 1:
            return 0
        i += 1  # Adjust to point to leftmost matching position.
        if self.big_l[i] > 0:
            return m - self.big_l[i]
        return m - self.small_l_prime[i]
    
    def match_skip(self):
        """
        Compute the shift to use when a full match of the pattern is found in the text.
        
        Returns:
            The shift amount based on the good suffix rule.
        """
        return len(self.small_l_prime) - self.small_l_prime[1]
