import requests
import itertools

def with_dash():
    try:
        check_url = input("do you want to check for known urls? y/n: ")

        if check_url == "y":
            start_of_url = input("start of url: ")
            string = input("enter string here: ")
            split = string.split("-")

            permutations = ["".join(p) for p in itertools.permutations(split)]
            url_list = [start_of_url + letters for letters in permutations]


            for urls in url_list:
                response = requests.get(urls)
                print(f"{urls} ==> {response}")

        elif check_url == "n":
            string = input("enter string here: ")
            split = string.split("-")

            permutations = ["".join(p) for p in itertools.permutations(split)]
            for i in permutations:
                print(i)

        else:
            print("you did not select a valid option! please try again.")

    except KeyboardInterrupt:
        print('ctrl-c pressed!')

def without_dash():
    try:
        string = input("enter a set of letters or numbers: ")
        combo = itertools.permutations(string)
        for values in combo:
            print(*values)
    except KeyboardInterrupt:
        print('ctrl-c pressed!')


user_input = input("do you want to Permutate or combine? ").lower()
if user_input == "permutate":
    with_dash()
elif user_input == "combine":
    without_dash()
else:
    print("you did not select a valid option! please try again.")