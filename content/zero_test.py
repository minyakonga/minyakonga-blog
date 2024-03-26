from typing import List


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """如果行/列中存在0，则整行or整列set 0

    Args:
        matrix (List[List[int]]): _description_

    Returns:
        List[List[int]]: _description_
    """
    # param validate

    # 1st, find the index of zeros
    zero_idxes = []
    for ridx in range(len(arr)):
        for cidx in range(len(arr[0])):
            if arr[ridx][cidx] == 0:
                zero_idxes.append([ridx, cidx])
    print(f'Debug: zero-indexes {zero_idxes}')
    
    # 2nd, summarize the zero-indexes, get the row/col indexes
    row_indexes, col_indexes = set(), set()
    for zi in zero_idxes:
        row_indexes.add(zi[0])
        col_indexes.add(zi[1])
    
    # 3rd, zero it
    for ri in row_indexes:  # row set 0
        arr[ri] = [0] * len(arr[0])
    for ci in col_indexes:  # col set 0
        for ridx in range(len(arr)):
            arr[ridx][ci] = 0
    
    return arr

if __name__ == '__main__':
    arr = [
        [1, 0, 0, 3, 4],
        [2, 0, 4, 5, 6],
        [7, 8, 2, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    expected_arr = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [7, 0, 0, 4, 5],
        [1, 0, 0, 4, 5]
    ]
    res = zero_matrix(arr)
    # print(f'Debuf: res arr {res}')
    assert arr == expected_arr

