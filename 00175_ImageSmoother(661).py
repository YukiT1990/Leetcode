# 661. Image Smoother

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # this results in starnge behavior
        # result = [[0] * len(img[0])] * len(img)
        result = [[0 for i in range(len(img[0]))] for j in range(len(img))]
        for r in range(len(img)):
            for c in range(len(img[r])):
                sum_array = [img[r][c]]
                if r-1 >= 0 and c-1 >= 0:
                    sum_array.append(img[r-1][c-1])
                if r-1 >= 0:
                    sum_array.append(img[r-1][c])
                if r-1 >= 0 and c+1 < len(img[r]):
                    sum_array.append(img[r-1][c+1])
                if c-1 >= 0:
                    sum_array.append(img[r][c-1])
                if c+1 < len(img[r]):
                    sum_array.append(img[r][c+1])
                if r+1 < len(img) and c-1 >= 0:
                    sum_array.append(img[r+1][c-1])
                if r+1 < len(img):
                    sum_array.append(img[r+1][c])
                if r+1 < len(img) and c+1 < len(img[r]):
                    sum_array.append(img[r+1][c+1])
                # print(sum_array)
                result[r][c] = sum(sum_array) // len(sum_array)
                # print(result[r][c])
           
        # print(result)
        return result