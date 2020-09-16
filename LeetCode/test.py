n = 6
def GPDFS(l, r, s):
	if len(s) == 2*n:
		print(''.join(s))
		pass
	if l < n:
		s.append('(')
		GPDFS(l+1, r, s)
		s.pop()
	if r < l:
		s.append(')')
		GPDFS(l, r+1, s)
		s.pop()
if __name__ == '__main__':
	GPDFS(0,0,[])
