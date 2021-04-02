import numpy as np

def selected_aggregation(ensembling):
    return {1:Min1,
            2:Min2,
            3:Min3,
            4:Min4,
            5:Sum1,
            6:Sum2,
            7:Sum3,
            8:Sum4,
            9:WeightedSum1,
            10:WeightedSum2,
            11:WeightedSum3,
            12:WeightedSum4,
            13:ThresholdSum1,
            14:ThresholdSum2,
            15:ThresholdSum3,
            16:ThresholdSum4,
            17:WeightedSumOther1,
            18:WeightedSumOther2,
            19:WeightedSumOther3,
            20:WeightedSumOther4,
            21:ThresholdSumOther1,
            22:ThresholdSumOther2,
            23:ThresholdSumOther3,
            24:ThresholdSumOther4}[ensembling]

#-----------------------
def scaling1(array):
    return (array - np.max(array, axis=0)) / (np.max(array, axis=0) - np.min(array, axis=0))
    
def scaling2(array):
    return (array - np.mean(array, axis=0)) / np.std(array, axis=0)
    
def scaling3(array):
    return array / abs(np.min(array, axis=0) + 0.001)
    
def scaling4(array):
    order = array.argsort(axis=0)
    ranks = order.argsort(axis=0)
    return ranks

#-----------------------
def Min1(array):
    scaled_array = scaling1(array)
    return np.min(scaled_array.T, axis=0)

def Min2(array):
    scaled_array = scaling2(array)
    return np.min(scaled_array.T, axis=0)

def Min3(array):
    scaled_array = scaling3(array)
    return np.min(scaled_array.T, axis=0)

def Min4(array):
    scaled_array = scaling4(array)
    return np.min(scaled_array.T, axis=0)
#-----------------------

def Sum1(array):
    scaled_array = scaling1(array)
    return np.sum(scaled_array.T, axis=0)

def Sum2(array):
    scaled_array = scaling2(array)
    return np.sum(scaled_array.T, axis=0)

def Sum3(array):
    scaled_array = scaling3(array)
    return np.sum(scaled_array.T, axis=0)

def Sum4(array):
    scaled_array = scaling4(array)
    return np.sum(scaled_array.T, axis=0)
#-----------------------

def WeightedSum1(array):
    scaled_array = scaling1(array)
    positive_array = array - array.min(axis=0)
    weights = positive_array.max(axis=0) / positive_array.mean(axis=0)
    scaled_array = scaled_array * weights
    return np.sum(scaled_array.T, axis=0)

def WeightedSum2(array):
    scaled_array = scaling2(array)
    positive_array = array - array.min(axis=0)
    weights = positive_array.max(axis=0) / positive_array.mean(axis=0)
    scaled_array = scaled_array * weights
    return np.sum(scaled_array.T, axis=0)

def WeightedSum3(array):
    scaled_array = scaling3(array)
    positive_array = array - array.min(axis=0)
    weights = positive_array.max(axis=0) / positive_array.mean(axis=0)
    scaled_array = scaled_array * weights
    return np.sum(scaled_array.T, axis=0)

def WeightedSum4(array):
    scaled_array = scaling4(array)
    positive_array = array - array.min(axis=0)
    weights = positive_array.max(axis=0) / positive_array.mean(axis=0)
    scaled_array = scaled_array * weights
    return np.sum(scaled_array.T, axis=0)
#-----------------------

def WeightedSumOther1(array):
    scaled_array = scaling1(array)
    positive_array = array - array.min(axis=0)
    weights = positive_array.max(axis=0) / np.median(positive_array, axis=0)
    scaled_array = scaled_array * weights
    return np.sum(scaled_array.T, axis=0)

def WeightedSumOther2(array):
    scaled_array = scaling2(array)
    positive_array = array - array.min(axis=0)
    weights = positive_array.max(axis=0) / np.median(positive_array, axis=0)
    scaled_array = scaled_array * weights
    return np.sum(scaled_array.T, axis=0)

def WeightedSumOther3(array):
    scaled_array = scaling3(array)
    positive_array = array - array.min(axis=0)
    weights = positive_array.max(axis=0) / np.median(positive_array, axis=0)
    scaled_array = scaled_array * weights
    return np.sum(scaled_array.T, axis=0)

def WeightedSumOther4(array):
    scaled_array = scaling4(array)
    positive_array = array - array.min(axis=0)
    weights = positive_array.max(axis=0) / np.median(positive_array, axis=0)
    scaled_array = scaled_array * weights
    return np.sum(scaled_array.T, axis=0)
#-----------------------

def ThresholdSum1(array):
    scaled_array = scaling1(array)
    threshold = np.mean(scaled_array, axis=0)
    lower_threshold_indices = scaled_array > threshold
    scaled_array[lower_threshold_indices] = 0
    return np.sum(scaled_array.T, axis=0)

def ThresholdSum2(array):
    scaled_array = scaling2(array)
    threshold = np.mean(scaled_array, axis=0)
    lower_threshold_indices = scaled_array > threshold
    scaled_array[lower_threshold_indices] = 0
    return np.sum(scaled_array.T, axis=0)

def ThresholdSum3(array):
    scaled_array = scaling3(array)
    threshold = np.mean(scaled_array, axis=0)
    lower_threshold_indices = scaled_array > threshold
    scaled_array[lower_threshold_indices] = 0
    return np.sum(scaled_array.T, axis=0)

def ThresholdSum4(array):
    scaled_array = scaling4(array)
    threshold = np.mean(scaled_array, axis=0)
    lower_threshold_indices = scaled_array > threshold
    scaled_array[lower_threshold_indices] = 0
    return np.sum(scaled_array.T, axis=0)

#-----------------------

def ThresholdSumOther1(array):
    scaled_array = scaling1(array)
    threshold = np.median(scaled_array, axis=0)
    lower_threshold_indices = scaled_array > threshold
    scaled_array[lower_threshold_indices] = 0
    return np.sum(scaled_array.T, axis=0)

def ThresholdSumOther2(array):
    scaled_array = scaling2(array)
    threshold = np.median(scaled_array, axis=0)
    lower_threshold_indices = scaled_array > threshold
    scaled_array[lower_threshold_indices] = 0
    return np.sum(scaled_array.T, axis=0)

def ThresholdSumOther3(array):
    scaled_array = scaling3(array)
    threshold = np.median(scaled_array, axis=0)
    lower_threshold_indices = scaled_array > threshold
    scaled_array[lower_threshold_indices] = 0
    return np.sum(scaled_array.T, axis=0)

def ThresholdSumOther4(array):
    scaled_array = scaling4(array)
    threshold = np.median(scaled_array, axis=0)
    lower_threshold_indices = scaled_array > threshold
    scaled_array[lower_threshold_indices] = 0
    return np.sum(scaled_array.T, axis=0)

#def ThresholdSumOther4(array):
#    scaled_array = scaling4(array)
#    threshold = np.median(scaled_array, axis=0)
#    lower_threshold_indices = scaled_array > threshold
#    for i in lower_threshold_indices:
#        scaled_array[lower_threshold_indices[:, i], i] = threshold[i]
#    return np.sum(scaled_array.T, axis=0)
    
    