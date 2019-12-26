def continuous_subsequence(s):
    mem = [[0 for i in range(2)] for j in range(len(s)+1)]
    result = []
    sum = 0
    for i in range(len(s)):
        m_i = i+1
        if s[i] < 0:
            if mem[i][0] != 0:
                mem[m_i][0] = max(mem[i][0]+s[i],s[i])
        else:
            mem[m_i][0] = mem[i][0]+s[i]

        mem[m_i][1] = max(mem[i][1],mem[m_i][0])
        print(mem)

    print("Memory:")
    print("Solution:")
    print(result)
    return 0;

a = [-1,52,-10,9,48,8]
continuous_subsequence(a)
