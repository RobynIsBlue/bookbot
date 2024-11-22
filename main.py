def main():
	path = "books/frankenstein.txt"
	print(get_book_text(path))
	print("Your Word Count is: " + str(word_count(path)))
	print(character_count(path))
	print(f"\n The \'{letter}\' character was found {number} times.\n")

def get_book_text(path):
	with open(path) as f:
		return f.read()



def word_count(path):
	with open(path) as f:
		return len(str(f.read()).split())



def character_count(path):
	dict = {}
	with open(path) as f:
		book = f.read().lower()
		for x in book:
			if x in dict:
				dict[x] += 1
			else:
				dict[x] = 1
	listed = [{k: v} for k, v in dict.items()]
	listed.sort(key=sort_on)
	while len(listed):

main()

