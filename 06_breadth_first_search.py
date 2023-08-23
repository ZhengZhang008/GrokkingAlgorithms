from collections import deque


def search(name):
    search_queue = deque()
    search_queue += [name]
    # This is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person in searched:
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            # Marks this person as searched
            searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == "m"


if __name__ == "__main__":
    graph = {"you": ["alice", "bob", "clarie"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "clarie": ["thom", "jonny"], "anuj": [], "peggy": [], "thom": [], "jonny": []}
    search("you")
