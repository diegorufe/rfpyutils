
class RFFrequencyTable:

    def __init__(self):
        """
        Class for store values for table frequencies
        """
        # Store values order low to high
        self.ar_values = []
        self.ar_absolute_frequencies = []
        self.ar_relative_frequencies = []
        self.ar_cumulative_absolute_frequencies = []
        self.ar_cumulative_relative_frequencies = []
