def main():
	path = "books/frankenstein.txt"
	print("--- Begin report of " + str(path) + " ---\n")
	print("Your Word Count is: " + str(word_count(path)))
	for x in character_count(path):
		print(f"\n The \'{x["char"]}\' character was found {x["num"]} times.")

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
	listed = [{"char": k, "num": v} for k, v in dict.items()]
	listed.sort(reverse=True, key=something_idk) 
	return listed



def something_idk(big_dic):
	return big_dic["num"]

main()

