def solution1(phone_book):
    answer = True
    for i, p1 in enumerate(phone_book):
        for p2 in phone_book[i+1:]:
            if p2.startswith(p1):
                answer = False
    return answer

# Written by Dohyung
def solution2(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

def solution(phone_book):
    # convert list to dictionary
    d = {p: True for p in phone_book}
    for p in phone_book:
        for i in range(1, len(p)):
            if p[:i] in d:  # if key in dictionary
                return False
    return True

if __name__ == "__main__":

    tc = [["119", "97674223", "1195524421"],
          ["123","456","789"],
          ["12","123","1235","567","88"]]
    answer = [False, True, False]

    for i in range(3):
        print( solution(tc[i]) == answer[i] )
