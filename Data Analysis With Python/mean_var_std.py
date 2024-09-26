"""
Author: Andrew SG
Date: 26/09/24
FreeCodeCamp python for data analysis course.
"""
import numpy as np

def calculate(list):
    # Check list length is 9
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    # Format list as numpy array
    formatted_list = np.array([[list[0:3]],
                               [list[3:6]],
                               [list[6:9]]])    

    # Create results dictionary
    calculations = {
        'mean': [np.mean(formatted_list, axis=0)[0].tolist(), np.transpose(np.mean(formatted_list, axis=2))[0].tolist(), np.mean(np.ndarray.flatten(formatted_list))],
        'variance': [np.var(formatted_list, axis=0)[0].tolist(), np.transpose(np.var(formatted_list, axis=2))[0].tolist(), np.var(np.ndarray.flatten(formatted_list))],
        'standard deviation': [np.std(formatted_list, axis=0)[0].tolist(), np.transpose(np.std(formatted_list, axis=2))[0].tolist(), np.std(np.ndarray.flatten(formatted_list))],
        'max': [np.max(formatted_list, axis=0)[0].tolist(), np.transpose(np.max(formatted_list, axis=2))[0].tolist(), np.max(np.ndarray.flatten(formatted_list))],
        'min': [np.min(formatted_list, axis=0)[0].tolist(), np.transpose(np.min(formatted_list, axis=2))[0].tolist(), np.min(np.ndarray.flatten(formatted_list))],
        'sum': [np.sum(formatted_list, axis=0)[0].tolist(), np.transpose(np.sum(formatted_list, axis=2))[0].tolist(), np.sum(np.ndarray.flatten(formatted_list))]
    }
    

    return calculations