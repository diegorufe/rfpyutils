from rfpyutils.array.rf_utils_array import RFUtilsArray
from rfpyutils.stadistic.rf_frequency_table import RFFrequencyTable
import math


class RFUtilsStadistic:

    @staticmethod
    def resolve_frequency_table_one_dimension_array(ar_values, calculate_with_intervals: bool = False):
        """
        Method for resolve frequency table from one dimension array
        :param ar_values: to resolve frequency table
        :param calculate_with_intervals: if True calculate frequencies with intervals for values
        :return: a object type RFFrequencyTable with resolve frequency table
        """
        result = RFFrequencyTable()

        if RFUtilsArray.is_not_empty(ar_values) and RFUtilsArray.is_one_dimension_array(ar_values):
            # Copy array
            ar_values_copy = list(ar_values)
            # Sort array low to high
            RFUtilsArray.short(ar_values_copy)

            num_records = len(ar_values_copy)

            map_array_values_frequency_absolute = {}
            ar_values_frequency_table = []

            # Add frency absloute values
            ar_absolute_frequencies = []
            ar_relative_frequencies = []
            ar_cumulative_absolute_frequencies = []
            ar_cumulative_relative_frequencies = []

            total_cumulative_absolute_frequencies = 0
            total_cumulative_relative_frequencies = 0

            if calculate_with_intervals:
                # map for intervals
                map_intervals = {}
                # path for intervals
                result.path = ar_values_copy[-1] - ar_values_copy[0]
                result.number_of_intervals = int(round(math.sqrt(len(ar_values_copy)), 0))
                result.number_of_intervals = 1 if result.number_of_intervals <= 0 else result.number_of_intervals
                # Add 0.02 in interval
                result.interval_width = round(result.path / result.number_of_intervals, 2) + 0.02
                # Start interval
                start_interval = ar_values_copy[0] - 0.05
                end_interval = start_interval + result.interval_width

                for interval in range(0, result.number_of_intervals):
                    ar_values_frequency_table.append((start_interval, end_interval))
                    start_interval = end_interval
                    end_interval = start_interval + result.interval_width
                    ar_absolute_frequencies.append(0)

                data_interval = (0, 0)
                for value in ar_values_copy:
                    for index, value_interval in enumerate(ar_values_frequency_table):
                        if value_interval[0] <= value < value_interval[1]:
                            # absolute frequency
                            ar_absolute_frequencies[index] = ar_absolute_frequencies[index] + 1

                            break

                for index, value_interval in enumerate(ar_values_frequency_table):
                    # relative frequency
                    ar_relative_frequencies.append(ar_absolute_frequencies[index] / num_records)

                    # absolute cumulative frequency
                    total_cumulative_absolute_frequencies = total_cumulative_absolute_frequencies + \
                                                            ar_absolute_frequencies[index]
                    ar_cumulative_absolute_frequencies.append(total_cumulative_absolute_frequencies)

                    # relative cumulative frequency
                    total_cumulative_relative_frequencies = total_cumulative_relative_frequencies + \
                                                            ar_absolute_frequencies[index] / num_records
                    ar_cumulative_relative_frequencies.append(total_cumulative_relative_frequencies)

            else:
                old_value = None

                # Count frequency absolutes
                for value in ar_values_copy:
                    if value != old_value:
                        map_array_values_frequency_absolute[value] = 0
                        old_value = value
                        ar_values_frequency_table.append(value)

                    map_array_values_frequency_absolute[value] += 1

                for value in ar_values_frequency_table:
                    # absolute frequency
                    ar_absolute_frequencies.append(map_array_values_frequency_absolute[value])

                    # relative frequency
                    ar_relative_frequencies.append(map_array_values_frequency_absolute[value] / num_records)

                    # absolute cumulative frequency
                    total_cumulative_absolute_frequencies = total_cumulative_absolute_frequencies + \
                                                            map_array_values_frequency_absolute[value]
                    ar_cumulative_absolute_frequencies.append(total_cumulative_absolute_frequencies)

                    # relative cumulative frequency
                    total_cumulative_relative_frequencies = total_cumulative_relative_frequencies + \
                                                            map_array_values_frequency_absolute[value] / num_records
                    ar_cumulative_relative_frequencies.append(total_cumulative_relative_frequencies)

            # ar values frequency table origin and sort values
            result.ar_values = ar_values_frequency_table
            result.ar_origin_values = ar_values
            result.ar_origin_values_sort = ar_values_copy

            # ar values frequency values
            result.ar_absolute_frequencies = ar_absolute_frequencies
            result.ar_relative_frequencies = ar_relative_frequencies
            result.ar_cumulative_absolute_frequencies = ar_cumulative_absolute_frequencies
            result.ar_cumulative_relative_frequencies = ar_cumulative_relative_frequencies

        return result
