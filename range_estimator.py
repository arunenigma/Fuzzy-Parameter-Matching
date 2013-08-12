# -*- coding: utf-8 -*-
__author__ = "Arunprasath Shankar"
__copyright__ = "Copyright 2012, Arunprasath Shankar"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "axs918@case.edu"

import numpy as np


class RangeCalculator:       
    def calculateFilterIRange(self, doc_param_range):
        pivots = []
        span = []
        max_doc_param_range = max(doc_param_range)
        norm_doc_param_range = []
        for value in doc_param_range:
            value /= float(max_doc_param_range)
            norm_doc_param_range.append(value)
        avg = np.mean(norm_doc_param_range, dtype=np.float128)
        below_avg_values = []
        above_avg_values = []

        for value in norm_doc_param_range:
            if value <= avg:
                below_avg_values.append(value)
            if value >= avg:
                above_avg_values.append(value)

        below_avg_values_pivot = np.mean(below_avg_values, dtype=np.float128)
        above_avg_values_pivot = np.mean(above_avg_values, dtype=np.float128)
        lowest_values = []
        highest_values = []

        for value in below_avg_values:
            if value <= below_avg_values_pivot:
                lowest_values.append(value)
        for value in above_avg_values:
            if value >= above_avg_values_pivot:
                highest_values.append(value)

        lowest_values_pivot = np.mean(lowest_values, dtype=np.float128)
        highest_values_pivot = np.mean(highest_values, dtype=np.float128)

        very_low = []
        very_high = []

        for value in lowest_values:
            if value <= lowest_values_pivot:
                very_low.append(value)
        for value in highest_values:
            if value >= highest_values_pivot:
                very_high.append(value)

        very_low_pivot = np.mean(very_low, dtype=np.float128)
        very_high_pivot = np.mean(very_high, dtype=np.float128)

        extremely_low = []
        extremely_high = []

        for value in very_low:
            if value <= very_low_pivot:
                extremely_low.append(value)

        for value in very_high:
            if value >= very_high_pivot:
                extremely_high.append(value)

        extremely_low_pivot = np.mean(extremely_low, dtype=np.float128)
        extremely_high_pivot = np.mean(extremely_high, dtype=np.float128)

        # adding overlap span (cox 1999)
        # triangle & triangle -> 25% overlap
        pivots.extend(
            [0, extremely_low_pivot, very_low_pivot, lowest_values_pivot, below_avg_values_pivot, avg,
             above_avg_values_pivot, highest_values_pivot, very_high_pivot, extremely_high_pivot, 1])
        span.append([0, 0, extremely_low_pivot])
        span.append([0, extremely_low_pivot, very_low_pivot])
        span.append([extremely_low_pivot, very_low_pivot, lowest_values_pivot])
        span.append([very_low_pivot, lowest_values_pivot, below_avg_values_pivot])
        span.append([lowest_values_pivot, below_avg_values_pivot, avg])
        span.append([below_avg_values_pivot, avg, above_avg_values_pivot])
        span.append([avg, above_avg_values_pivot, highest_values_pivot])
        span.append([above_avg_values_pivot, highest_values_pivot, very_high_pivot])
        span.append([highest_values_pivot, very_high_pivot, extremely_high_pivot])
        span.append([very_high_pivot, extremely_high_pivot, 1])
        span.append([extremely_high_pivot, 1, 1])
        return [span, pivots, max_doc_param_range]

