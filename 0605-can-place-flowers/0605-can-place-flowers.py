class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if (n==0):
            return True
        i=0
        k=0
        flowerbed.append(0)
        while (i<len(flowerbed)-1):
            if (flowerbed[i+1]==0):
                if (flowerbed[i]==0):
                    k+=1
                    if (k==n):
                        return True
                i+=2
            else:
                i+=3
        return False
                