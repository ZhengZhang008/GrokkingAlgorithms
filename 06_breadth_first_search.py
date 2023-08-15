from collections import deque


def search(name):
    search_queue = deque()
    search_queue += [name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == "m"


if __name__ == "__main__":
    graph = {"you": ["alice", "bob", "clarie"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "clarie": ["thom", "jonny"], "anuj": [], "peggy": [], "thom": [], "jonny": []}
    search("you")
