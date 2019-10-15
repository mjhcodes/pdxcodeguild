# Lab 18 - Peaks & Valleys

def get_peaks(data):
  """accepts an array of numbers and iterates through the array; returns the 'peaks' (i.e. a number with a lower number on both the left and the right of it)"""
  peaks = []
  for index, num in enumerate(data):
    if index != 0 and index != (len(data) - 1):
      if num > data[index - 1] and num > data[index + 1]:
        peaks.append(index)
  return peaks

def get_valleys(data):
  """accepts an array of numbers and iterates through the array; returns the 'valleys' (i.e. a number with a greater number on both the left and the right of it)"""
  valleys = []
  for index, num in enumerate(data):
    if index != 0 and index != (len(data) - 1):
      if num < data[index - 1] and num < data[index + 1]:
        valleys.append(index)
  return valleys

def get_peaks_and_valleys(peaks, valleys):
  """accepts two lists, combines them, sorts them and returns the sorted version"""
  peaks_and_valleys = peaks + valleys
  sorted_peaks_and_valleys = sorted(peaks_and_valleys)
  return sorted_peaks_and_valleys

def main(data):
  """accepts an array of numbers and returns the indices of the peaks and valleys"""
  peaks = get_peaks(data)
  valleys = get_valleys(data)
  peaks_and_valleys = get_peaks_and_valleys(peaks, valleys)
  print(peaks_and_valleys)


# array variable to be used as test case
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

main(data)