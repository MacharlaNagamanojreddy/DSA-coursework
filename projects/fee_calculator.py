#fee calculator


def calculate_fee(course, marks):
    """
    Calculate the course fee based on selected course and marks.

    Args:
        course (str): Course name (e.g., "AI").
        marks (int): Student marks.

    Returns:
        int | None: The fee amount, or None if the course is invalid.
    """

    course = course.strip().upper()

    if course == "AI":
        fee = 50000
    else:
        # Add more courses here if needed
        return None

    # Apply a discount for high marks
    if marks > 90:
        fee -= 5000

    return fee


def main():
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    fee = calculate_fee(course, marks)

    if fee is None:
        print("Invalid Course Selected")
    else:
        print("Final fee:", fee)


if __name__ == "__main__":
    main()