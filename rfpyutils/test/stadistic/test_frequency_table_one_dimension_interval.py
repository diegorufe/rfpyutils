from rfpyutils.stadistic.rf_utils_stadistic import RFUtilsStadistic

ar_values = [0.5, 1, 2.5, 1, 0.6, 0.7, 0.8, 1.2, 1.1, 1.5, 1.5, 1.7, 1.8, 0.1, 0.3, 2]

result = RFUtilsStadistic.resolve_frequency_table_one_dimension_array(ar_values, calculate_with_intervals=True)

print("Test frequency table one dimension intervals")
print("Ar values: ", result.ar_values)
print("Total origin vales: ", len(result.ar_origin_values))
print("Ar origin values: ", result.ar_origin_values)
print("Ar origin values sort: ", result.ar_origin_values_sort)
print("Ar absolute frequency : ", result.ar_absolute_frequencies)
print("Ar relative frequency : ", result.ar_relative_frequencies)
print("Ar absolute cumulative frequency : ", result.ar_cumulative_absolute_frequencies)
print("Ar relative cumulative frequency : ", result.ar_cumulative_relative_frequencies)
