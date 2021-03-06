

def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    
    """
    houses = set() 
    cohort_unique_houses = open(filename)
    for line in cohort_unique_houses:
        cohort1_unique_houses = line.split("|")
        if cohort1_unique_houses[2] == "":
            continue 
        house = cohort1_unique_houses[2]
        houses.add(house)

    print houses 
    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohortself.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    students_by_cohort = open(filename)
    for line in students_by_cohort:
        student = line.split("|")
        student_first_name = student[0]
        student_last_name = student[1]
        student_full_name = student_first_name + " " + student_last_name
        if student[4].rstrip() == "TA":
            tas.append(student_full_name)
        elif student[4].rstrip() == "Winter 2015":
            winter_15.append(student_full_name)
        elif student[4].rstrip() == "Spring 2015":
            spring_15.append(student_full_name)
        elif student[4].rstrip() == "Summer 2015":
            summer_15.append(student_full_name)


    all_students.append(winter_15)
    all_students.append(spring_15)
    all_students.append(summer_15)
    all_students.append(tas)

    # print winter_15
    # print spring_15
    # print summer_15
    # print tas

    print all_students
    # Code goes here

    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    students_by_house = open(filename)
    for line in students_by_house:
        student = line.split("|")
        last_name = student[1]
        house = student[2].rstrip()
        if house == "Gryffindor":
            gryffindor.append(last_name)
        elif house == "Hufflepuff":
            hufflepuff.append(last_name)
        elif house == "Slytherin":
            slytherin.append(last_name)
        elif house == "Dumbledore's Army":
            dumbledores_army.append(last_name)
        elif house == "Ravenclaw":
            ravenclaw.append(last_name)
        elif house == "Order of the Phoenix":
            order_of_the_phoenix.append(last_name)
        elif student[4].rstrip() =="TA":
            tas.append(last_name)
        elif student[4].rstrip() == "I":
            instructors.append(last_name)

    all_students.append(gryffindor)
    all_students.append(hufflepuff)
    all_students.append(slytherin)
    all_students.append(dumbledores_army)
    all_students.append(order_of_the_phoenix)
    all_students.append(ravenclaw)
    all_students.append(tas)
    all_students.append(instructors)

    print all_students

    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """
    students = open(filename)
    student_list = []
    for student in students:
        student_information = student.split("|")
        if student_information[4].rstrip() == "I" or student_information[4].rstrip() == "TA":
            continue 

        student_list.append(student_information)

#    print student_list 

    # Code goes here

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here
    student_data = all_students_tuple_list("cohort_data.txt")
    #print student_data
    #print "****************"
    for s_list in student_data:
    #    print s_list 
        if student_list[0] == s_list[0]:
            return s_list[4].rstrip()
    # user_input = raw_input("Enter a first and last name: ")

    # # first_name = student_list[0]
    # # last_name  = student_list[1]
    # # cohort = student_list[4]
    # student_info = open("cohort_data.txt")





    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()
    student_list = []
    students = open(filename)
    for student in students:
        student_information = student.split("|") #["Peggy", "Zheng", ]\
        first_name = student_information[0]
        student_list.append(first_name)

    for i in range(1, len(student_list)-1):
        if student_list[i] == student_list[i+1]:
            # print student_list[i]
            duplicate_names.add(student_list[i])

    print duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and returns everyone in their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)

#students_by_house("cohort_data.txt")

find_name_duplicates("cohort_data.txt")
