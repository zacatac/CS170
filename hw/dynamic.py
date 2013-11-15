# Homework 8 Question 1:  Corrupted text document
# Here is the recursive version, which takes worst case exponential time.
def reconstruct_bad(s, word_set):
    """Uses words to find a valid reconstruction of s recursively.
    Returns the list of words of some valid reconstruction, or None if
    no such reconstruction exists.

    >>> reconstruct_bad('helloworld', set(['hello', 'world']))
    ['hello', 'world']
    >>> reconstruct_bad('helloworld', ['he', 'hell', 'hello', 'low', 'or', 'world'])
    ['hello', 'world']
    >>> reconstruct_bad('hellowor', ['he', 'hell', 'hello', 'low', 'or', 'world'])
    >>> reconstruct_bad('hellowor', ['he', 'hel', 'hello', 'low', 'or', 'world'])
    ['hel', 'low', 'or']
    """
    if len(s) == 0:
        return []
    for i in range(len(s)):
        if s[i:] in word_set:
            recurse = reconstruct_bad(s[:i], word_set)
            if recurse is not None:
                return recurse + [s[i:]]
    return None

def reconstruct(s, word_set):
    """Uses words to find a valid reconstruction of s with dynamic programming.
    Returns the list of words of some valid reconstruction, or None if
    no such reconstruction exists.

    >>> reconstruct('helloworld', set(['hello', 'world']))
    ['hello', 'world']
    >>> reconstruct('helloworld', ['he', 'hell', 'hello', 'low', 'or', 'world'])
    ['hello', 'world']
    >>> reconstruct('hellowor', ['he', 'hell', 'hello', 'low', 'or', 'world'])
    >>> reconstruct('hellowor', ['he', 'hel', 'hello', 'low', 'or', 'world'])
    ['hel', 'low', 'or']
    """
    return None

# Homework 8 Question 2:  Cutting cloth
def cut(X, Y, cloths):
    """
    Return the optimal profit from cutting a cloth of dimensions X by Y
    using products in cloths.
    cloths is a list of products in the form (a_i, b_i, c_i)
    No need to actually return the sequence of cuts
    Assume cloths can NOT be rotated
    If you assume you can rotate cloths, then the fourth doctest should
    output 37 instead of 35 and the last doctest should output
    6476541363870789573617211L.
    >>> cut(3, 3, [(2, 3, 15),(1, 1, 2)])
    21
    >>> cut(4, 4, [(1, 3, 1), (3, 2, 3), (3, 1, 1), (2, 3, 3)])
    7
    >>> cut(5, 1, [(5, 1, 20), (4, 1, 15), (3, 1, 14), (2, 1, 14)])
    28
    >>> cut(5, 5, [(5, 5, 34), (2, 1, 3), (1, 1, 1)])
    35
    >>> cut(6, 10, [(5, 2, 518), (5, 3, 166), (3, 7, 965), (2, 9, 386), (2, 2, 247), (3, 2, 275), (3, 6, -51), (3, 4, 950), (1, 6, 580), (1, 7, 458), (1, 3, 979), (5, 4, 646), (5, 3, 785), (2, 9, 55), (1, 6, 691), (1, 2, 902), (2, 2, 904), (2, 8, 762), (5, 5, 741), (3, 3, 667), (5, 9, 563), (5, 7, -48), (5, 2, 761), (4, 8, 60), (1, 2, 920), (2, 2, 865), (4, 5, 539), (3, 9, 754), (4, 8, 983), (1, 5, 30), (1, 7, 908), (3, 5, 465), (4, 6, 188), (1, 1, 18), (5, 3, 596), (1, 8, 259), (4, 9, 798), (4, 5, 741), (5, 3, 522), (1, 6, 3), (4, 9, 672), (2, 5, 72), (5, 1, 401), (3, 9, 592), (4, 9, 186), (3, 7, 777), (4, 2, -55), (5, 1, 777), (2, 4, 743), (1, 2, 293), (3, 7, 948), (3, 3, 866), (4, 6, 469), (4, 5, 812), (5, 2, 640), (4, 4, 748)])
    27600
    >>> cut(188, 104, [(92, 84, 187648262415585029354L), (24, 1, 770820623759589236054L), (1, 19, 6343331404378834058391L), (143, 41, 482805643085269536567L), (185, 10, 9166703829252251535263L), (126, 40, 6732011466279861114357L), (93, 54, 5341261317657475915062L), (137, 10, 743218864471917793600L), (62, 59, 2084288559190764250008L), (107, 88, 3934388709961969701564L), (130, 101, 9135034666819779628623L), (118, 63, 1915028646820101671280L), (136, 41, 1680777309141665114441L), (159, 6, 3520780978991090150286L)])
    6011293219412958136758942L
    """
    return 0

# Homework 8 Question 3:  Optimal Binary Search Tree
class Tree(object):
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        def f(x):
            return str(x) if x is not None else "()"
        return "(" + f(self.item) + ", " + f(self.left) + ", " + f(self.right) + ")"

def optimal_bst(words, frequencies):
    """Returns the binary search tree which minimizes the average number of
    comparisons to look up a word.
    >>> print optimal_bst(['do'], [1])
    (do, (), ())
    >>> print optimal_bst(['define', 'lambda'], [0.3, 0.7])
    (lambda, (define, (), ()), ())
    >>> print optimal_bst(['define', 'lambda'], [0.6, 0.4])
    (define, (), (lambda, (), ()))
    >>> print optimal_bst(['x', 'y', 'z'], [0.7, 0.16, 0.14])
    (x, (), (y, (), (z, (), ())))
    >>> print optimal_bst(['x', 'y', 'z'], [0.4, 0.3, 0.3])
    (y, (x, (), ()), (z, (), ()))
    >>> print optimal_bst(['begin', 'do', 'else', 'end', 'if', 'then', 'while'], [0.14, 0.14, 0.14, 0.16, 0.14, 0.14, 0.14])
    (end, (do, (begin, (), ()), (else, (), ())), (then, (if, (), ()), (while, (), ())))
    >>> print optimal_bst(['begin', 'do', 'else', 'end', 'if', 'then', 'while'], [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23])
    (do, (begin, (), ()), (while, (if, (else, (), (end, (), ())), (then, (), ())), ()))
    """
    return None

# Homework 8 Question 4:  Exon Chaining
def chain(triples):
    """Returns a list of triples that do not overlap and have maximum weight,
    sorted in ascending order.
    triples is a list of tuples of the form (l_i, r_i, w_i)
    The triples (1, 2, 100) and (2, 3, 100) are considered overlapping.
    Note that you can calculate n = max_i r_i
    
    >>> chain([])
    []
    >>> chain([(1, 5, 3)])
    [(1, 5, 3)]
    >>> chain([(3, 4, 5), (2, 3, 8), (1, 2, 5)])
    [(1, 2, 5), (3, 4, 5)]
    >>> chain([(3, 4, 5), (2, 3, 12), (1, 2, 5)])
    [(2, 3, 12)]
    >>> chain([(3, 7, 5), (5, 6, 2), (2, 4, 3), (1, 4, 4), (6, 9, 5), (9, 10, 2)])
    [(1, 4, 4), (6, 9, 5)]
    >>> chain([(3, 7, 5), (5, 6, 2), (2, 4, 3), (1, 4, 2), (6, 9, 5), (9, 10, 2)])
    [(2, 4, 3), (6, 9, 5)]
    >>> chain([(3, 7, 5), (5, 6, 2), (2, 4, 3), (1, 2, 2), (6, 9, 5), (9, 10, 2)])
    [(1, 2, 2), (3, 7, 5), (9, 10, 2)]
    """
    return []

# Homework 8 Question 5:  Timesheets (part 2)
def timesheets_bad(jobs, T):
    """Returns a list of job IDs in the order that they should be run.
    jobs is a list of tuples, in the form (i, v_i, r_i, p_i).
    Since it is implemented naively, it cannot handle the last doctest
    of timesheets - it can only handle around 20 jobs at the most.
    i is the job ID
    v_i is the bonus
    r_i is the time taken
    p_i is the penalty.

    >>> timesheets_bad([(0, 1, 1, 4), (1, 2, 2, 3), (2, 3, 3, 2)], 100)
    []
    >>> timesheets_bad([(0, 100, 2, 2), (1, 100, 4, 1), (2, 100, 1, 2)], 7)
    [2, 0, 1]
    >>> timesheets_bad([(0, 100, 2, 2), (1, 100, 4, 1), (2, 100, 1, 2)], 6)
    [2, 1]
    >>> timesheets_bad([(0, 6, 2, 2), (1, 7, 4, 1), (2, 4, 1, 2)], 7)
    [2, 1]
    >>> timesheets_bad([(0, 6, 2, 2), (1, 7, 4, 1), (2, 4, 1, 2)], 4)
    [1]
    >>> timesheets_bad([(0, 6, 2, 2), (1, 7, 4, 1), (2, 4, 1, 2)], 1)
    [2]
    """
    subs = subsets(list(range(len(jobs))))
    bestBenefit, bestSchedule = 0, []
    for order in subs:
        s = [jobs[i] for i in order]
        s.sort(key=lambda job: (job[2] * 1.0 / job[3]))
        benefit, t = 0, 0
        for job in s:
            t += job[2]
            benefit += job[1] - job[3]*t
        if benefit > bestBenefit and t <= T:
            bestBenefit, bestSchedule = benefit, [job[0] for job in s]
    return bestSchedule

def subsets(lst):
    """Returns a list of all possible subsets of lst.
    >>> subsets([])
    [[]]
    >>> x = subsets([1, 2, 3])
    >>> x.sort()
    >>> x
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    # Algorithm:  Either we use the first number in our subset, or we don't.
    # So, find the subsets of lst[1:], and for each one, either add the first
    # number, or don't add it.
    if len(lst) == 0:
        return [[]]
    small_subsets = subsets(lst[1:])
    return small_subsets + [[lst[0]] + x for x in small_subsets]

def timesheets(jobs, T):
    """Returns a list of job IDs in the order that they should be run.
    jobs is a list of tuples, in the form (i, v_i, r_i, p_i).
    i is the job ID
    v_i is the bonus
    r_i is the time taken
    p_i is the penalty.

    >>> timesheets([(0, 1, 1, 4), (1, 2, 2, 3), (2, 3, 3, 2)], 100)
    []
    >>> timesheets([(0, 100, 2, 2), (1, 100, 4, 1), (2, 100, 1, 2)], 7)
    [2, 0, 1]
    >>> timesheets([(0, 100, 2, 2), (1, 100, 4, 1), (2, 100, 1, 2)], 6)
    [2, 1]
    >>> timesheets([(0, 6, 2, 2), (1, 7, 4, 1), (2, 4, 1, 2)], 7)
    [2, 1]
    >>> timesheets([(0, 6, 2, 2), (1, 7, 4, 1), (2, 4, 1, 2)], 4)
    [1]
    >>> timesheets([(0, 6, 2, 2), (1, 7, 4, 1), (2, 4, 1, 2)], 1)
    [2]
    >>> len(timesheets([(i, 101, 2, 1) for i in range(100)], 100))
    50
    """
    return []

# Run doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
