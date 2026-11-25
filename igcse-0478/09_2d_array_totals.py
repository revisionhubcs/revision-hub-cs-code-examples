"""2D arrays: total for each row

Notes, live tools and self-marking practice:
https://revisionhub.online/igcse-computer-science-0478/programming/

Part of Revision Hub CS code examples - https://revisionhub.online
"""

def row_totals(scores):
    """Return a list with the total of each row of a 2D list."""
    totals = []
    for row in scores:
        student_total = 0            # reset INSIDE the outer loop
        for score in row:
            student_total = student_total + score
        totals.append(student_total)
    return totals


if __name__ == "__main__":
    scores = [[10, 8, 9, 7], [6, 9, 10, 8], [5, 7, 6, 9]]
    print(row_totals(scores))        # [34, 33, 27]
