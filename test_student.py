from student import *


def test_winner():
    students = StudentManager()

    students.add_student('s1', "A", 9, 1)
    students.add_student('s2', "A", 9, 4)
    assert students.get_winner().name == 's2'

    students.add_student('s3', "A", 9, 5)
    assert students.get_winner().name == 's3'

    students.add_student('s4', "A", 9, 29)
    students.add_student('s5', "A", 9, 2)
    assert students.get_winner().name == 's4'

    students.add_student('s6', "A", 9, 2)
    assert students.get_winner().name != 's6'


def test_general():
    students = StudentManager()

    students.add_student('s1', "A", 9, 8)
    students.add_student('s2', "A", 9, 6)

    w = students.get_random_winners()[0]
    p = students.get_prize(w)
    print(p)


if __name__ == "__main__":
    test_general()
