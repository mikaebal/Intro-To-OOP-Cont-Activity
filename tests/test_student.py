from school_schedule.student import Student

# Nominal Case
def test_new_valid_student():
    # Arrange
    name = "Mikaela"
    grade = "Senior"
    classes = ["Art", "Science"]

    # Act
    mikaela = Student(name, grade, classes)

    # Assert
    assert mikaela.name == name
    assert mikaela.grade == grade
    assert mikaela.classes == classes
    assert len(mikaela.classes) == 2

# Nominal Case
def test_add_class():
    # Arrange
    name = "Dennif"
    grade = "Senior"
    classes = ["Math"]
    new_class = "History"

    # Act
    dennif = Student(name, grade, classes)
    dennif.add_class(new_class)

    # Assert
    assert len(dennif.classes) == 2

# Edge Case
def test_get_num_classes():
    # Arrange
    name = "Mason"
    grade = "Junior"
    classes = []

    # Act
    mason = Student(name, grade, classes)
    num_classes = mason.get_num_classes()

    # Assert
    assert num_classes == 0
