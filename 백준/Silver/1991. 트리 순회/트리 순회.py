def preDfs(node):
    if node < 0:
        return

    preResult.append(chr(node+bias))
    preDfs(bt[node][0])
    preDfs(bt[node][1])

def inDfs(node):
    if node < 0:
        return

    inDfs(bt[node][0])
    inResult.append(chr(node + bias))
    inDfs(bt[node][1])

def postDfs(node):
    if node < 0:
        return
    postDfs(bt[node][0])
    postDfs(bt[node][1])
    postResult.append(chr(node + bias))

bias = 65
N = int(input())
bt = [[] for _ in range(N+1)]
preResult = []
inResult = []
postResult = []


for i in range(1, N + 1):
    idx, ch1, ch2 = map(ord, input().split())
    idx -= bias
    bt[idx].append(ch1 - bias)
    bt[idx].append(ch2 - bias)


preDfs(0)
inDfs(0)
postDfs(0)
print("".join(preResult))
print("".join(inResult))
print("".join(postResult))
