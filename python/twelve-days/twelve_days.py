def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse + 1)]


def verse(index):
    st = f"On the {ordinals[index - 1]} day of Christmas my true love gave to me: "
    if index != 1:
        st += f"{', '.join(sentences[-index:-1])}, and {sentences[-1]}"
    else:
        st += sentences[-1]

    return st


sentences = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
    "a Partridge in a Pear Tree.",
]

ordinals = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]
