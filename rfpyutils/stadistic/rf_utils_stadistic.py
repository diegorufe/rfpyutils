from rfpyutils.array.rf_utils_array import RFUtilsArray
from rfpyutils.stadistic.rf_frequency_table import RFFrequencyTable


class RFUtilsStadistic:

    @staticmethod
    def resolve_frequency_table_one_dimension_array(ar_values):
        """
        Method for resolve frequency table from one dimension array
        :param ar_values: to resolve frequency table
        :return: a object type RFFrequencyTable with resolve frequency table
        """
        result = RFFrequencyTable()

        if RFUtilsArray.is_not_empty(ar_values) and RFUtilsArray.is_one_dimension_array(ar_values):
            # Copy array
            ar_values_copy = list(ar_values)
            # Sort array low to high
            RFUtilsArray.short(ar_values_copy)

            map_array_values_frequency_absolute = {}
            ar_values_frequency_table = []

            old_value = None

            # Count frequency absolutes
            for value in ar_values_copy:
                if value != old_value:
                    map_array_values_frequency_absolute[value] = 0
                    old_value = value
                    ar_values_frequency_table.append(value)

                map_array_values_frequency_absolute[value] += 1

            result.ar_values = ar_values_frequency_table

            # Add frency absloute values
            ar_absolute_frequencies = []
            ar_relative_frequencies = []
            ar_cumulative_absolute_frequencies = []
            ar_cumulative_relative_frequencies = []

            num_records = len(ar_values_copy)
            total_cumulative_absolute_frequencies = 0
            total_cumulative_relative_frequencies = 0

            for value in result.ar_values:
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

            result.ar_absolute_frequencies = ar_absolute_frequencies
            result.ar_relative_frequencies = ar_relative_frequencies
            result.ar_cumulative_absolute_frequencies = ar_cumulative_absolute_frequencies
            result.ar_cumulative_relative_frequencies = ar_cumulative_relative_frequencies

        return result
