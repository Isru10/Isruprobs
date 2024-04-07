class Solution:
    def simplifyPath(self, path: str) -> str:
        ps=path.split('/')
        st=[]
        for sp in ps:
            if sp and sp!="." and sp!="..":
                st.append(sp)
            else:
                if st and sp=="..":st.pop()
        return '/'+'/'.join(st)
                
