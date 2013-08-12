# Fuzzy Parameter Scoring Demo
from random import randrange
from range_estimator import *
from dom import *
from math import fabs
from operator import itemgetter


class FuzzyParamMatching(object):
    def __init__(self):
        pass

    def rangeFinder(self, min_R, max_R):
        if max_R == min_R + 1:
            l = [min_R, max_R]
        else:
            l = range(min_R, max_R)
        if len(l) > 1 and not l is None:
            return l

if __name__ == '__main__':
    search_results = {}
    fpm = FuzzyParamMatching()
    query_param = '34 to 58'
    Q_min_R = query_param.split(' ')[0]
    Q_max_R = query_param.split(' ')[2]
    sample_doc_params = [(randrange(34, 58), randrange(34, 58)) for i in range(100)]
    sample_doc_params_sorted_pairs = []
    for param_pair in sample_doc_params:
        if not sorted(param_pair)[0] == sorted(param_pair)[1]:
            sample_doc_params_sorted_pairs.append(sorted(param_pair))
    r = RangeCalculator()
    span_and_pivots = r.calculateFilterIRange(fpm.rangeFinder(int(Q_min_R), int(Q_max_R)))
    dom = DegreeOfMembership()
    print 'Math Derivation Verification using Test Cases for Case I'
    print
    for param_pair in sample_doc_params_sorted_pairs:
        print param_pair, '\t>', dom.findFuzzySet(param_pair[0], param_pair[1], span_and_pivots[0], span_and_pivots[1], span_and_pivots[2])
        dom_data = dom.findFuzzySet(param_pair[0], param_pair[1], span_and_pivots[0], span_and_pivots[1], span_and_pivots[2])
        fs = (dom_data[0][0] * dom_data[0][1]) + (dom_data[0][2] * dom_data[0][3]) - ((dom_data[1][0] * dom_data[1][1]) + (dom_data[1][2] * dom_data[1][3]))
        search_results[tuple(param_pair)] = fabs(fs)
    max_value = max(search_results.values())
    norm_search_results = {}
    for param, value in search_results.iteritems():
        value /= max_value
        norm_search_results[param] = value

    sorted_search_results = sorted(norm_search_results.iteritems(), key=itemgetter(1), reverse=True)
    print
    print
    print 'Matched Ranked Doc Fuzzy Parameter Ranges (Case I)'
    print '------------------------------------------------'
    print 'Query Fuzzy Parameter Range = ', query_param
    print
    for rank, result in enumerate(sorted_search_results):
        print 'Rank', rank+1, '> ', result[0], result[1]
