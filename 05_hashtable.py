def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        # If the voter hasn't voted yet, let them vote and mark them as voted
        voted[name] = True
        print("let them vote!")


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        # If the page is not in cache, get it from the server and store it in cache
        data = get_data_from_server(url)
        cache[url] = data
        return data


def get_data_from_server(url):
    print("get data from server")


if __name__ == "__main__":
    book = {"apple": 0.67, "milk": 1.49, "avocado": 1.49}
    print(book)
    print(book["avocado"])

    phone_book = {"jenny": 8675309, "emergency": 911}
    print(phone_book["jenny"])

    voted = {}
    check_voter("tom")
    check_voter("mike")
    check_voter("mike")

    cache = {}
