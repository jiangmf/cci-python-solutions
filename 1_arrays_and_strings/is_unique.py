import sys

def main():
	chars = {}
	for c in sys.argv[1]:
		if c in chars:
			return False
		else:
			chars[c] = True
	return True

if __name__ == "__main__":
    print(main())