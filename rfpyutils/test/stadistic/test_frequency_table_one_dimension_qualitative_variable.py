from rfpyutils.stadistic.rf_utils_stadistic import RFUtilsStadistic

ar_values = ["SP", "AP", "SP", "SP", "NT", "SB", "NT", "SB", "MH", "AP", "AP", "AP"]

result = RFUtilsStadistic.resolve_frequency_table_one_dimension_array(ar_values,
                                                                      calculate_with_qualitative_variables=True)

print("Test frequency table one dimension qualitative variable")
print("Ar values: ", result.ar_values)
print("Total origin vales: ", len(result.ar_origin_values))
print("Ar origin values: ", result.ar_origin_values)
print("Ar absolute frequency : ", result.ar_absolute_frequencies)
print("Ar relative frequency : ", result.ar_relative_frequencies)
print("Ar absolute cumulative frequency : ", result.ar_cumulative_absolute_frequencies)
print("Ar relative cumulative frequency : ", result.ar_cumulative_relative_frequencies)
