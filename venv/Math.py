from numpy import loadtxt, array, max
from scipy import signal

# Шаг 1: Заменяем запятые на точки в файле
filename = "resonator measurements/58.03.23В.txt"
processed_filename = "processed.txt"

with open(filename, 'r') as infile, open(processed_filename, 'w') as outfile:
    for line in infile:
        outfile.write(line.replace(',', '.'))

# Шаг 2: Читаем обработанный файл
data = loadtxt(processed_filename, delimiter='\t')

# Проверяем результат
print(data[:, 1])

dataset_0 = data[:, 1]
b, a = signal.butter(3, 0.1) #b, a параметры фильтра
datafilt = signal.filtfilt(b, a, dataset_0) #datafilt - фильтрованные данные, dataset_0 - исходные

peaks_max, _ = signal.find_peaks(datafilt, prominence=max(datafilt)/2) #поиск пиков среди фильтрованных данных, выдает массив координат пиков
print(peaks_max)