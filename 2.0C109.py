import csv
import pandas as pd
import statistics

df = pd.read_csv("C:\Python\StudentsPerformance.csv")

math_list = df["math score"].to_list()
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()

math_mean = statistics.mean(math_list)
reading_mean = statistics.mean(reading_list)
writing_mean = statistics.mean(writing_list)

math_median = statistics.median(math_list)
reading_median = statistics.median(reading_list)
writing_median = statistics.median(writing_list)

math_mode = statistics.mode(math_list)
reading_mode = statistics.mode(reading_list)
writing_mode = statistics.mode(writing_list)

print("mean, median & mode OF MATH is {}, {} & {}".format(math_mean, math_median, math_mode))
print("mean, median & mode OF READING is {}, {} & {}".format(reading_mean, reading_median, reading_mode))
print("mean, median & mode OF WRITING is {}, {} & {}".format(writing_mean, writing_median, writing_mode))


math_std_deviation = statistics.stdev(math_list)
reading_std_deviation = statistics.stdev(reading_list)
reading_std_deviation = statistics.stdev(writing_list)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-writing_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

reading_list_of_data_within_1_std_deviation = [result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_list_of_data_within_1_std_deviation = [result for result in writing_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list)))
print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))
print("{}% of data for writing lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for writing lies within 2 standard deviations".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for writing lies within 3 standard deviations".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))