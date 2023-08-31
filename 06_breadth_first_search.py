from collections import deque


def search(name):
    # Initialize a queue with the starting name
    search_queue = deque()
    search_queue += [name]
    # This is how you keep track of which people you've searched before.
    searched = []
    # Continue searching while the queue is not empty
    while search_queue:
        # Pop a person from the left of the queue
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person in searched:
            continue
        # If the person is a seller, print their name and return True
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            # If the person is not a seller, add their neighbors to the queue
            search_queue += graph[person]
            # Marks this person as searched
            searched.append(person)
    # If no seller is found, return False
    return False


def person_is_seller(name):
    return name[-1] == "m"


if __name__ == "__main__":
    graph = {"you": ["alice", "bob", "clarie"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "clarie": ["thom", "jonny"], "anuj": [], "peggy": [], "thom": [], "jonny": []}
    search("you")
