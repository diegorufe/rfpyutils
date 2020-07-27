"""
Utilities for array
"""


class RFUtilsArray:

    @staticmethod
    def is_not_empty(array):
        """
        Method to check array is not empty.
        :param array: to check
        :return: True if array is not None isinstance (list, tuple) and len > 0
        """
        return array is not None and isinstance(array, (list, tuple)) and len(array) > 0

    @staticmethod
    def is_empty(array):
        """
        Method to check array is empty
        :param array: to check
        :return: True if is None not instance (list, tuple) or len = 0
        """
        return RFUtilsArray.is_not_empty(array) is False

    @staticmethod
    def short(array):
        """
        MEthod for short array. This function check the array is not empty
        :param array: to sort
        :return: None
        """
        if RFUtilsArray.is_not_empty(array):
            array.sort()

    @staticmethod
    def is_one_dimension_array(array):
        """
        Method to check one dimension array
        :param array: to check
        :return: True if one dimension array False if not
        """
        result = False
        if RFUtilsArray.is_not_empty(array):
            try:
                result = len(array[0]) == 0
            except:
                result = True

        return result
