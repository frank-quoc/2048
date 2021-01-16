import numpy as np

def check_no_indices_with_zero():
    """Test to obtain indices with zero value."""
    matrix = np.array([[2, 8, 2, 6],
                [1, 2, 3, 2],
                [1, 2, 6, 0],
                [2048, 6, 42, 4]])
    zero_indices = len(np.where(matrix == 0)[1]) 
    print(zero_indices)

check_no_indices_with_zero()