import random

import sample


def test_bug(bug: sample.Bug):
    pos = (
        bug.position.copy()
    )  # initial position; this will be used to keep track of expected position

    for i in range(random.randint(3, 5)):  # random number of times it will be moved
        r = random.randint(1, 4)  # direction is chosen randomly
        units = random.randint(1, 5)
        if r == 1:  # moving up
            bug.move_up(units)
            print(f"\nMoved UP {units} units")
            pos[1] += units
            print("\tExpected new position:", pos)
            print("\tTrue position:", bug.position)
            print("\tTest passed?", pos == bug.position)
        elif r == 2:  # moving down
            bug.move_down(units)
            print(f"\nMoved DOWN {units} units")
            # updating the expected position
            pos[1] -= units
            print("\tExpected new position:", pos)
            print("\tTrue position:", bug.position)
            print("\tTest passed?", pos == bug.position)
        elif r == 3:  # moving right
            bug.move_right(units)
            print(f"\nMoved RIGHT {units} units")
            # updating the expected position
            pos[0] += units
            print("\tExpected new position:", pos)
            print("\tTrue position:", bug.position)
            print("\tTest passed?", pos == bug.position)
        else:
            bug.move_left(units)
            print(f"\nMoved LEFT {units} units")
            pos[0] -= units
            print("\tExpected new position:", pos)
            print("\tTrue position:", bug.position)
            print("\tTest passed?", pos == bug.position)


print("Welcome to the Sample PA Tester")
while True:
    user_in = input(
        "\n"
        + "-" * 50
        + "\nWhich problem would you like to test?\n1.  Problem 1: hello(subject)\n2.  Problem 2: Bug class\n3.  Quit\n\nEnter your selection: "
    )
    if user_in == "1":

        subjects = [
            "CECS 229 student",
            "Darth Vader",
            "Darkness, my old friend",
            "it's me",
            "Yellow",
        ]
        subject = subjects[random.randint(0, len(subjects) - 1)]
        print(f'\nTesting hello("{subject}")...\n')
        expected = f"Hello, {subject}!"
        received = sample.hello(subject)
        print(sample.hello(3))
        print(f"Expected string: {expected}\nReceived string: {received}")
        if expected == received:
            print("\nTest passed!")
        else:
            print("\nTest failed.")
    elif user_in == "2":
        print(f"\nTesting Bug class...")
        names = ["Tom", "Jerry", "Chandler", "Tina", "Rachel", "Joey", "Ross", "Monica"]
        name = names[random.randint(0, len(names) - 1)]
        bug = sample.Bug(name)
        position = [random.randint(0, 3), random.randint(0, 3)]
        print(f"Created the bug:\n{bug}")
        test_bug(bug)

    elif user_in == "3":
        break
    else:
        print("\nInvalid selection.  Please try again.")

