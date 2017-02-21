import sys

def main():
	return sys.argv[1].replace(" ", "%20")

if __name__ == "__main__":
    print(main())