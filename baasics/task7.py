buttons = ["Like", "Dislike", "Dislike", "Like"]
def like_or_dislike(buttons):
    state = "Nothing"
    for button in buttons:
        if button == "Like":
            if state == "Like":
                state = "Nothing"
            else:
                state = "Like"
        elif button == "Dislike":
            if state == "Dislike":
                state = "Nothing"
            else:
                state = "Dislike"
    return state
print(like_or_dislike(buttons))