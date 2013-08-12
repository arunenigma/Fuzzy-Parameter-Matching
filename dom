# -*- coding: utf-8 -*-
from __future__ import division

__author__ = "Arunprasath Shankar"
__copyright__ = "Copyright 2012, Arunprasath Shankar"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "axs918@case.edu"


class DegreeOfMembership(object):
    def findFuzzySet(self, D_min_R, D_max_R, span, pivots, norm_max):
        fuzzy_param_score_lst = []
        D_min_R /= norm_max
        D_max_R /= norm_max
        D_pivots = [D_min_R, D_max_R]
        fuzzy_set_intervals = [pivots[i:i + 2] for i in range(len(pivots) - 1)]
        for pivot in D_pivots:
            fuzzy_sets = []
            for interval in fuzzy_set_intervals:
                if interval[0] <= pivot <= interval[1]:
                    for i, s in enumerate(span):
                        if not (i + 1) >= len(span):
                            if (interval[0] in span[i] and interval[1] in span[i]) and (
                                        interval[0] in span[i + 1] and interval[1] in span[i + 1]):
                                fuzzy_sets.append([pivot, i, span[i], i + 1, span[i + 1]])
            fuzzy_param_score_lst.append(self.findDOM(fuzzy_sets))
        return fuzzy_param_score_lst

    def findDOM(self, fuzzy_sets):
        dom_1 = self.triangularFunction(fuzzy_sets[0][0], fuzzy_sets[0][2][0], fuzzy_sets[0][2][1], fuzzy_sets[0][2][2])
        dom_2 = self.triangularFunction(fuzzy_sets[0][0], fuzzy_sets[0][4][0], fuzzy_sets[0][4][1], fuzzy_sets[0][4][2])
        return [fuzzy_sets[0][1], dom_1, fuzzy_sets[0][3], dom_2]

    def triangularFunction(self, pivot, a, b, c):
        dom = 0.0
        if pivot <= a:
            dom += 0
        elif a <= pivot <= b:
            dom += (pivot - a) / (b - a)
        elif b <= pivot <= c:
            dom += (c - pivot) / (c - b)
        elif c <= pivot:
            dom += 0
        return dom
