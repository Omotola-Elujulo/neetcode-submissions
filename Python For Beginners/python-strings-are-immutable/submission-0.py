def remove_fourth_character(word: str) -> str:
    beforef = word[:3]
    afterf = word[4:]
    return beforef + afterf


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
