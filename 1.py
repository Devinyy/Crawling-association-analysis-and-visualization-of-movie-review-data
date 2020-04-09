def DAG(sentence):
        DAG = {}    #DAG空字典，用来构建DAG有向无环图
        N = len(sentence)
        for k in range(N):
            tmplist = [] 
            i = k
            frag = sentence[k]
            while i < N:
                if frag in Dict:
                    tmplist.append(i) 
                i += 1      
                frag = sentence[k:i + 1] 
            if not tmplist:
                tmplist.append(k)
            DAG[k] = tmplist
        return DAG

        