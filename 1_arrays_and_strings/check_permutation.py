import sys

def main():
	chars = {}
	chars2 = {}
	for c in sys.argv[1]:
		chars[c] = chars.setdefault(c, 0) + 1
	for c in sys.argv[2]:
		chars2[c] = chars2.setdefault(c, 0) + 1
	for key, value in chars.items():
		if chars2.get(key) != value:
			return False
	return True

if __name__ == "__main__":
    print(main())