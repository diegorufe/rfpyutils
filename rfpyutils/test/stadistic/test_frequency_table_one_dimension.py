from rfpyutils.stadistic.rf_utils_stadistic import RFUtilsStadistic

ar_values = [0.5, 1, 8, 1, 0.6]

result = RFUtilsStadistic.resolve_frequency_table_one_dimension_array(ar_values)

print("Test frequency table one dimension")
print("Ar values: ", result.ar_values)
print("Ar absolute frequency : ", result.ar_absolute_frequencies)
print("Ar relative frequency : ", result.ar_relative_frequencies)
print("Ar absolute cumulative frequency : ", result.ar_cumulative_absolute_frequencies)
print("Ar relative cumulative frequency : ", result.ar_cumulative_relative_frequencies)
