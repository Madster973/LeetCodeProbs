class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c : return mat
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(mat[i][j])
        
        reshape_arr = [[0 for _ in range(c)]for _ in range(r)]
        k = 0
        for i in range(len(reshape_arr)):
               for j in range(len(reshape_arr[i])):
                    reshape_arr[i][j] = arr[k]
                    k+=1
        return reshape_arr
        