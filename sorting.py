import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {"series_1": [], "series_2": [], "series_3": []}
        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))
    return data


def selection_sort(numbers_list):
    for numbers in range(len(numbers_list)):
        for i in range(numbers+1, len(numbers_list)):
            if numbers_list[i] < numbers_list[numbers]:
                numbers_list[i], numbers_list[numbers] = numbers_list[numbers], numbers_list[i]
    return numbers_list


def main():
    numbers = read_data("numbers.csv")
    numbers2 = numbers["series_3"]
    sorted_numbers = selection_sort(numbers2)
    print(sorted_numbers)



if __name__ == '__main__':
    main()
