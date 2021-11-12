def summarize_degrees(filename):
    """
    Read a census file and summarize the degrees (education)
    earned by those contained in the file.  The summary
    should be stored in a dictionary where the key is the
    degree earned and the value is the number of people that 
    have earned that degree.  The degree information is in
    the 4th column of the file.  There is no header row in the
    file.
    """ 
    degrees = dict()
    a_degrees = []
    with open(filename) as file_in:
        for line in file_in:
            # fields = line.split(",") 
            a_degrees.append(line.split(",")[3])

    for a_degree in a_degrees:
        if a_degree not in degrees:
            degrees[a_degree] = 1
        else:
            degrees[a_degree] += 1

    
    print(degrees)

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
print(summarize_degrees("census.txt")) # You might need to add a path for the file
# Results may be in a different order:
# {'Bachelors': 5355, 'HS-grad': 10501, '11th': 1175, 
# 'Masters': 1723, '9th': 514, 'Some-college': 7291, 
# 'Assoc-acdm': 1067, 'Assoc-voc': 1382, '7th-8th': 646, 
# 'Doctorate': 413, 'Prof-school': 576, '5th-6th': 333, 
# '10th': 933, '1st-4th': 168, 'Preschool': 51, 
# '12th': 433} 

def summarize_gender(filename):
    """
    Read a census file and summarize the gender
    of those contained in the file.  The summary
    should be stored in a dictionary where the key is 
    the gender and the value is the number of 
    people that have earned that degree.  The 
    degree information is in the 4th column of the 
    file.  There is no header row in the
    file.
    """ 
    genders = dict()
    a_genders = []
    with open(filename) as file_in:
        for line in file_in:
            # fields = line.split(",") 
            a_genders.append(line.split(",")[9])
    count = 1
    for a_gender in a_genders:
        if a_gender not in genders:
            genders[a_gender] = 1
            count += 1
        else:
            genders[a_gender] += 1
            count += 1

    male = (genders["Male"] / count) * 100
    female = (genders["Female"] / count) * 100
    print("There is on average of {}% males and {}% females in the census.".format(male, female))  
print("\n=========== PROBLEM 2 TESTS ===========")
print(summarize_gender("census.txt")) # You might need to add a path for the file
# There is on average of 66.91849395000307% males and 33.078434985566% females in the census.


def summarize_ethnicity(filename):
    """
    Read a census file and summarize the ethnicity
    of those contained in the file.  The summary
    should be stored in a dictionary where the key is the
    ethnicty and the value is the number of people that 
    have that ethnicity. The degree information is in
    the 9th column of the file.  There is no header row in the
    file.
    """ 
    ethnicitys = dict()
    a_ethnicitys = []
    with open(filename) as file_in:
        for line in file_in:
            # fields = line.split(",") 
            a_ethnicitys.append(line.split(",")[8])
    count = 1
    for a_ethnicity in a_ethnicitys:
        if a_ethnicity not in ethnicitys:
            ethnicitys[a_ethnicity] = 1
            count += 1
        else:
            ethnicitys[a_ethnicity] += 1
            count += 1

    print(ethnicitys) 
print("\n=========== PROBLEM 3 TESTS ===========")
print(summarize_ethnicity("census.txt")) # You might need to add a path for the file
# {'White': 27816, 'Black': 3124, 'Asian-Pac-Islander': 1039, 'Amer-Indian-Eskimo': 311, 'Other': 271}