"""
Minecart Tracks
Ted works as a computer programmer at Minecraft Inc. His boss has just given him an important assignment to update the code for the minecart tracks by the end of April. However, he has recently had to self-isolate due to Covid-19 and has left the code for the tracks BACK AT WORK!! He has the shorthand for the tracks he's supposed to look at, and where the carts are suppost to end up, but not the actual code.

He knows that:

"-->" = "Speed-Up Track" ⁠— If a minecart interacts with this track, it's velocity increases by 2.67 BPS unless it's at its maximum speed of 8 BPS.
"<-->" = "Powered Track" ⁠— If a minecart interacts with this track, it's velocity remains the same.
"<--" = "Slow-Down Track" ⁠— If a minecart interacts with this track, it's velocity decreases by 2.67 BPS unless it's velocity equals 0, at which point it stops.
"---" = "Unpowered Track" ⁠— If a minecart interacts with this track, it's velocity decreases by 1 BPS unless it's velocity equals 0, at which point it stops.
Help Ted by writing a class for the tracks that interact with the provided Minecart class as shown above. And then write a function that will take a list of the shorthand tracks and:

If the Minecart reaches the last peice of Track, return True.
Else return the index of the Track where the Minecart stops.
Examples
mine_run(["-->", "-->", "-->", "<--", "<--", "<--"]) ➞ True

mine_run(["-->", "<--", "-->", "-->", "<-->", "---"]) ➞ 1
"""


def mine_run(tracks):
    BPS = 0
    for i, track in enumerate(tracks, start=0):
        BPS += get_BPS_change(track)
        BPS = min(BPS, 8)
        if BPS <= 0: return True if i == len(tracks) - 1 else i
def get_BPS_change(track):
    return {"-->": 2.67, "<--": -2.67, "---": -1, "<-->": 0}.get(track, None)

#
# def mine_run(tracks):
#
#     index = -1
#     BPS = 0
#
#     for track in tracks:
#         index += 1
#         BPS += get_BPS_change(track)
#         BPS = min(BPS, 8)
#         if BPS > 0:
#             continue
#         else:
#             if len(tracks) - 1 == index:
#                 return True
#             else:
#                 return index
#
# def get_BPS_change(track):
#     if track == "-->":
#         return 2.67
#     elif track == "<--":
#         return -2.67
#     elif track == "---":
#         return -1
#     elif track == "<-->":
#         return 0




print(mine_run(["-->", "-->", "-->", "<--", "<--", "<--"]))
print(mine_run(["-->", "<--", "-->", "-->", "<-->", "---"]))
print(mine_run(["-->", "-->", "-->", "-->", "<-->", "<--", "<--", "<--", "<--", "---", "---", "---"]))