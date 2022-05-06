class Solution:

    def compress(self, originalString: str) -> str:

        l = len(originalString)
        if l <= 2:
            return originalString

        length = 1
        res = ""
        for i in range(1, l):
            if originalString[i] != originalString[i - 1]:
                res = res + originalString[i - 1] + str(length)
                length = 1
            else:
                length += 1

        if originalString[-1] != originalString[-2]:
            res = res + originalString[-1] + "1"
        else:
            res = res + originalString[i - 1] + str(length)

        if len(originalString) <= len(res):
            return originalString
        else:
            return res








