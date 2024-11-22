def main():
	path = "books/frankenstein.txt"
	print("--- Begin report of " + str(path) + "---\n")
	print("Your Word Count is: " + str(word_count(path)))
	for x in character_count(path):
		for y in x:
			print(f"\n The \'{y}\' character was found {x[y]} times.")

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
			if x.isalpha() == False:
				None
			elif x in dict:
				dict[x] += 1
			else:
				dict[x] = 1
	listed = [{k: v} for k, v in dict.items()]
	sortess = sorted[listed, reverse=True]
	return sortess

def something_idk(big_dic):
	

main()

