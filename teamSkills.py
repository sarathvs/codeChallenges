# No. of teams that can be formed from array having member's skills
# each team to have exact 5 diff skills pcmbz
def perfectTeam(skills):

    count = [0] * 5
    for i in range(len(skills)):

        if skills[i] == "p":
            count[0] = count[0] + 1

        if skills[i] == "c":
            count[1] = count[1] + 1

        if skills[i] == "m":
            count[2] = count[2] + 1

        if skills[i] == "b":
            count[3] = count[3] + 1

        if skills[i] == "z":
            count[4] = count[4] + 1

    return min(count)

print(perfectTeam("mppzbmbpzcbmpbmczcz"))
