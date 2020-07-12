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

        if RFUtilsArray.is_not_empty(ar_values):
            # Copy array
            ar_values_copy = list(ar_values)
            # Sort array low to high
            RFUtilsArray.short(ar_values_copy)

        return result
