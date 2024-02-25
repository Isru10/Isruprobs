class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def decomp_prime(n):
            if n<=1:return set()
            elif( n==2):return set([2])
            sm=math.ceil(math.sqrt(n))
            for i in range(sm, 1, -1):
                if n%i==0:
                    return decomp_prime(n//i).union(decomp_prime(i))
            return set([n])
        prime_decomposition=[]
        for num in nums:
            prime_decomposition.append(list(decomp_prime(num)))
        graph=collections.defaultdict(set)
        for n,pds in enumerate(prime_decomposition):
            if len(pds)>0:
                graph[pds[0]].add(nums[n])
                graph[nums[n]].add(pds[0])
            for i in range(1, len(pds)):
                graph[pds[0]].add(pds[i])
                graph[pds[i]].add(pds[0])
        seen=set()
        def dfs(node):
            seen.add(node)
            for next_node in graph[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    dfs(next_node)
        dfs(nums[0])
        if 1 in seen :return len(nums)==1
        for num in nums :
            if num not in seen : return False 
        return True
            