import numpy as np

def selected_aggregation(ensembling):
    return {1:Sum1,
            2:Sum2,
            3:Sum3,
            4:Sum4,
            5:Sum5,
            6:Sum6,
            7:Sum7,
            8:Sum8,
            9:Sum9,
            10:Sum10,
            11:Sum11,
            12:Sum12,
            13:Sum13,
            14:Sum14,
            15:Sum15,
            16:Sum16}[ensembling]
#-----------------------
def scaling1(array):
    return (array - np.max(array,axis=0)) / (np.max(array,axis=0) - np.min(array,axis=0))
    
def scaling2(array):
    return ((array+1) / np.min(array+1,axis=0)) - np.max(((array+1) / np.min(array+1,axis=0)),axis=0)
#-----------------------
#def Sum1(array):
#    scaled_array = scaling1(array)
#    return np.max(scaled_array.T, axis=0)

def Sum1(array):
    scaled_array = scaling1(array)
    return np.sum(scaled_array.T, axis=0)

def Sum2(array):
    scaled_array = scaling1(array)
    return np.mean(scaled_array.T, axis=0)

def Sum3(array):
    scaled_array = scaling1(array)
    return np.min(scaled_array.T, axis=0)
#-----------------------
#def Sum5(array):
#    scaled_array = scaling2(array)
#    return np.max(scaled_array.T, axis=0)

def Sum4(array):
    scaled_array = scaling2(array)
    return np.sum(scaled_array.T, axis=0)

def Sum5(array):
    scaled_array = scaling2(array)
    return np.mean(scaled_array.T, axis=0)

def Sum6(array):
    scaled_array = scaling2(array)
    return np.min(scaled_array.T, axis=0)
#-----------------------
#def Sum5(array):
#    scaled_array = scaling1(array)
#    return np.max((scaled_array / np.mean(scaled_array,axis=0)).T, axis=0)
#
#def Sum6(array):
#    scaled_array = scaling1(array)
#    return np.sum((scaled_array / np.mean(scaled_array,axis=0)).T, axis=0)
#
def Sum7(array):
    scaled_array = scaling1(array)
    return np.mean((scaled_array / np.mean(scaled_array,axis=0)).T, axis=0)

def Sum8(array):
    scaled_array = scaling1(array)
    return np.min((scaled_array / np.mean(scaled_array,axis=0)).T, axis=0)
#-----------------------
def Sum9(array):
    scaled_array = scaling1(array)
    return np.max((scaled_array / np.std(scaled_array,axis=0)).T, axis=0)

def Sum10(array):
    scaled_array = scaling1(array)
    return np.sum((scaled_array / np.std(scaled_array,axis=0)).T, axis=0)

def Sum11(array):
    scaled_array = scaling1(array)
    return np.mean((scaled_array / np.std(scaled_array,axis=0)).T, axis=0)

def Sum12(array):
    scaled_array = scaling1(array)
    return np.min((scaled_array / np.std(scaled_array,axis=0)).T, axis=0)
#-----------------------
def Sum13(array):
    scaled_array = scaling1(array)
    return np.max((scaled_array / np.std(scaled_array,axis=0)/ np.mean(scaled_array,axis=0)).T, axis=0)

def Sum14(array):
    scaled_array = scaling1(array)
    return np.sum((scaled_array / np.std(scaled_array,axis=0)/ np.mean(scaled_array,axis=0)).T, axis=0)

def Sum15(array):
    scaled_array = scaling1(array)
    return np.mean((scaled_array / np.std(scaled_array,axis=0)/ np.mean(scaled_array,axis=0)).T, axis=0)

def Sum16(array):
    scaled_array = scaling1(array)
    return np.min((scaled_array / np.std(scaled_array,axis=0)/ np.mean(scaled_array,axis=0)).T, axis=0)