import sys

m = int(sys.stdin.readline().strip())
S = set()

for _ in range(m):
    commands = sys.stdin.readline().strip().split()

    # num이 없는 경우 -> all, empty
    if len(commands) == 1:
        # all
        if commands[0] == "all":
            S = set(list(range(1, 21)))
        # empty
        else:
            S = set()

    # num이 있는 경우
    else:
        command, num = commands[0], commands[1]
        num = int(num)

        # add
        if command == "add":
            S.add(num)
        # remove
        elif command == "remove":
            S.discard(num)
        # check
        elif command == "check":
            print(1 if num in S else 0)
        # toggle
        elif command == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
