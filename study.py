def decrypt(code, k)  :
        if k == 0: return [0] * len(code)
        res = []
        
        if k > 0:

            i = 0
            while i < len(code):
            
                count = 0
                sum_k = 0
                j = i + 1    
                while count < k:

                    if j >= len(code):
                        j = 0
                    sum_k += code[j]
                    j += 1
                    count += 1
                i += 1
                res.append(sum_k)

        elif k < 0:

            i = 0
            while i < len(code):
                j = i - 1
                count = 0
                sum_k = 0
                while count < k:
                    sum_k += code[j]
                    j -= 1
                    count -= 1
                i += 1
                res.append(sum_k)
        return res    
print(decrypt([12,34,54,23,34,23,12], 3))
