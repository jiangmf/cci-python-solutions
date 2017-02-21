import sys

def main():
	chars = {}
	for c in sys.argv[1]:
		if c != ' ':
			chars[c] = chars.setdefault(c, 0) + 1
	
	odds = 0
	for key, value in chars.items():
		if value % 2 == 1:
			odds += 1

	if odds > 1:
		return False
	return True

if __name__ == "__main__":
    print(main())