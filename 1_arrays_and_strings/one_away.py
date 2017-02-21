import sys

def main():
	chars = {}
	chars2 = {}

	s1 = sys.argv[1]
	s2 = sys.argv[2]

	if len(s1) - len(s2) ==  0 :
		found = False
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				if not found:
					found = True
				else:
					return False
		return True
	elif len(s1) - len(s2) == 1:
		j = 0
		for i in range(len(s2)):
			if s1[j] != s2[i]:
				if j == i and s1[j+1] == s2[i]:
					j += 1
				else:
					return False
			j += 1
		return True
	elif len(s1) - len(s2) == -1:
		j = 0
		for i in range(len(s1)):
			if s1[i] != s2[j]:
				if j == i and s1[i] == s2[j+1]:
					j += 1
				else:
					return False
			j += 1
		return True
	return False

if __name__ == "__main__":
    print(main())