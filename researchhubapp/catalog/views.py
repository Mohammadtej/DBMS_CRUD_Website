from django.shortcuts import render
from catalog.models import UserDetails, UserEmail, Person, University, StudentProfessor, Student, Professor
from django.contrib import messages
import psycopg2

# Create your views here.

def dispIndex(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('password'):
            Email = request.POST.get('email')
            Password = request.POST.get('password')

            conn = psycopg2.connect(
                database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
            )
            #Creating a cursor object using the cursor() method
            c = conn.cursor()

            c.execute('''SET SEARCH_PATH TO "researchHub"''')
            c.execute(f'''
                SELECT *
                FROM "UserEmail" AS ue
                INNER JOIN "UserDetails" AS ud
                    ON ue.UserID = ud.UserID
                WHERE
                    ue.Email = '{Email}'
                    AND ud.Password = '{Password}';
            ''')

            obj = c.fetchall()
            
            conn.commit()
            #Closing the connection
            c.close()
            
            if len(obj) != 0:
                return render(request, 'home.html')
            
            else:
                messages.success(request, 'Please enter valid Email and Password')
                return render(request, 'index.html')
    else:
        return render(request, 'index.html')
def dispHome(request):
    return render(request, 'home.html')

def dispStudent(request):
    return render(request, 'student.html')

def dispProfessor(request):
    return render(request, 'professor.html')

def dispRecruitment(request):
    if request.method == 'POST':
        if request.POST.get('professorID'):
            ProfessorID = request.POST.get('professorID')
            
            conn = psycopg2.connect(
                database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
            )
            #Creating a cursor object using the cursor() method
            c = conn.cursor()

            c.execute('''SET SEARCH_PATH TO "researchHub"''')
            c.execute(f'''SELECT recruitmentStudents({ProfessorID});''')

            ls = c.fetchall()
            obj = []

            for it in range(0, len(ls)):
                str = ls[it][0]
                str2 = str[1:len(str)-1]
                obj.append(str2.split(','))
            conn.commit()
            #Closing the connection
            c.close()

            return render(request, 'recruitmentShow.html', {"data" : obj})
    else:
        return render(request, 'recruitment.html')

def studentInsert(request):
    if request.method=="POST":
        if request.POST.get('email') and request.POST.get('password') and request.POST.get('firstName') and request.POST.get('middleName') and request.POST.get('lastName') and request.POST.get('degree') and request.POST.get('year') and request.POST.get('universityID') and request.POST.get('resume'):
            Email = request.POST.get('email')
            Password = request.POST.get('password')
            FirstName = request.POST.get('firstName')
            MiddleName = request.POST.get('middleName')
            LastName = request.POST.get('lastName')
            HighestDegree = request.POST.get('degree')
            YearOfPassing = request.POST.get('year')
            UniversityID = request.POST.get('universityID')
            Resume = request.POST.get('resume')
            Followers = 0
            Role = 'Student'

            conn = psycopg2.connect(
                database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
            )
            #Creating a cursor object using the cursor() method
            c = conn.cursor()

            c.execute('''SET SEARCH_PATH TO "researchHub"''')
            c.execute('''
                SELECT MAX(ue.UserID)
                FROM "UserEmail" AS ue
            ''')
            obj = c.fetchone()
            StudentID = obj[0] + 1

            c.execute(f'''
                INSERT INTO "Student"
                VALUES ({StudentID}, {YearOfPassing}, '{Resume}');
                
                INSERT INTO "StudentProfessor"
                VALUES ({StudentID}, {Followers}, {UniversityID});

                INSERT INTO "Person"
                VALUES ({StudentID}, '{FirstName}', '{MiddleName}', '{LastName}', '{HighestDegree}');

                INSERT INTO "UserDetails"
                VALUES ({StudentID}, '{Role}', '{Password}');

                INSERT INTO "UserEmail"
                VALUES ({StudentID}, '{Email}');
            ''')

            conn.commit()
            #Closing the connection
            c.close()

            messages.success(request, f'Student Record with ID: {StudentID} Inserted Successfully')
            return render(request, 'st_insert.html')
    else:
        return render(request, 'st_insert.html')


def professorInsert(request):
    if request.method=="POST":
        if request.POST.get('email') and request.POST.get('password') and request.POST.get('firstName') and request.POST.get('middleName') and request.POST.get('lastName') and request.POST.get('degree') and request.POST.get('universityID') and request.POST.get('websiteLink'):
            Email = request.POST.get('email')
            Password = request.POST.get('password')
            FirstName = request.POST.get('firstName')
            MiddleName = request.POST.get('middleName')
            LastName = request.POST.get('lastName')
            HighestDegree = request.POST.get('degree')
            UniversityID = request.POST.get('universityID')
            WebsiteLink = request.POST.get('websiteLink')
            Followers = 0
            Role = 'Professor'

            conn = psycopg2.connect(
                database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
            )
            #Creating a cursor object using the cursor() method
            c = conn.cursor()

            c.execute('''SET SEARCH_PATH TO "researchHub"''')
            c.execute('''
                SELECT MAX(ue.UserID)
                FROM "UserEmail" AS ue
            ''')
            obj = c.fetchone()
            ProfessorID = obj[0] + 1

            c.execute(f'''
                INSERT INTO "Professor"
                VALUES ({ProfessorID}, '{WebsiteLink}');
                
                INSERT INTO "StudentProfessor"
                VALUES ({ProfessorID}, {Followers}, {UniversityID});

                INSERT INTO "Person"
                VALUES ({ProfessorID}, '{FirstName}', '{MiddleName}', '{LastName}', '{HighestDegree}');

                INSERT INTO "UserDetails"
                VALUES ({ProfessorID}, '{Role}', '{Password}');

                INSERT INTO "UserEmail"
                VALUES ({ProfessorID}, '{Email}');
            ''')

            conn.commit()
            #Closing the connection
            c.close()

            messages.success(request, f'Professor Record with ID: {ProfessorID} Inserted Successfully')
            return render(request, 'pr_insert.html')
    else:
        return render(request, 'pr_insert.html')

def studentUpdate(request):
    if request.method == "POST":
        if request.POST.get('studentID') and request.POST.get('email') and request.POST.get('password') and request.POST.get('firstName') and request.POST.get('middleName') and request.POST.get('lastName') and request.POST.get('degree') and request.POST.get('year') and request.POST.get('universityID') and request.POST.get('resume'):
            StudentID = request.POST.get('studentID')
            Email = request.POST.get('email')
            Password = request.POST.get('password')
            FirstName = request.POST.get('firstName')
            MiddleName = request.POST.get('middleName')
            LastName = request.POST.get('lastName')
            HighestDegree = request.POST.get('degree')
            YearOfPassing = request.POST.get('year')
            UniversityID = request.POST.get('universityID')
            Resume = request.POST.get('resume')
            Followers = 0
            Role = 'Student'

            conn = psycopg2.connect(
                database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
            )
            #Creating a cursor object using the cursor() method
            c = conn.cursor()

            c.execute('''SET SEARCH_PATH TO "researchHub"''')

            c.execute(f'''
                SELECT *
                FROM "Student" AS s
                WHERE
                    s.StudentID = {StudentID};
            ''')

            obj = c.fetchall()

            if len(obj) != 0:
                c.execute(f'''
                    UPDATE "Student"
                    SET YearOfPassing = {YearOfPassing},
                    Resume = '{Resume}'
                    WHERE
                        StudentID = {StudentID};

                    UPDATE "StudentProfessor"
                    SET UniversityID = {UniversityID}
                    WHERE
                        StudProfID = {StudentID};

                    UPDATE "Person"
                    SET FirstName = '{FirstName}',
                    MiddleName = '{MiddleName}',
                    LastName = '{LastName}',
                    HighestDegree = '{HighestDegree}'
                    WHERE
                        PersonID = {StudentID};

                    UPDATE "UserDetails"
                    SET Password = '{Password}'
                    WHERE
                        UserID = {StudentID};

                    UPDATE "UserEmail"
                    SET Email = '{Email}'
                    WHERE
                        UserID = {StudentID};
                    
                ''')


                messages.success(request, f'Student Record with ID: {StudentID} Updated Successfully')

            else:
                messages.error(request, 'StudentID does not exist in the Database')

            conn.commit()
            #Closing the connection
            c.close()

            return render(request, 'st_update.html')
    else:
        return render(request, 'st_update.html')


def professorUpdate(request):
    if request.method == "POST":
        if request.POST.get('professorID') and request.POST.get('email') and request.POST.get('password') and request.POST.get('firstName') and request.POST.get('middleName') and request.POST.get('lastName') and request.POST.get('degree') and request.POST.get('universityID') and request.POST.get('websiteLink'):
            ProfessorID = request.POST.get('professorID')
            Email = request.POST.get('email')
            Password = request.POST.get('password')
            FirstName = request.POST.get('firstName')
            MiddleName = request.POST.get('middleName')
            LastName = request.POST.get('lastName')
            HighestDegree = request.POST.get('degree')
            UniversityID = request.POST.get('universityID')
            WebsiteLink = request.POST.get('websiteLink')
            Followers = 0
            Role = 'Professor'

            conn = psycopg2.connect(
                database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
            )
            #Creating a cursor object using the cursor() method
            c = conn.cursor()

            c.execute('''SET SEARCH_PATH TO "researchHub"''')

            c.execute(f'''
                SELECT *
                FROM "Professor" AS p
                WHERE
                    p.ProfessorID = {ProfessorID};
            ''')

            obj = c.fetchall()

            if len(obj) != 0:
                c.execute(f'''
                    UPDATE "Professor"
                    SET WebsiteLink = '{WebsiteLink}'
                    WHERE
                        ProfessorID = {ProfessorID};

                    UPDATE "StudentProfessor"
                    SET UniversityID = {UniversityID}
                    WHERE
                        StudProfID = {ProfessorID};

                    UPDATE "Person"
                    SET FirstName = '{FirstName}',
                    MiddleName = '{MiddleName}',
                    LastName = '{LastName}',
                    HighestDegree = '{HighestDegree}'
                    WHERE
                        PersonID = {ProfessorID};

                    UPDATE "UserDetails"
                    SET Password = '{Password}'
                    WHERE
                        UserID = {ProfessorID};

                    UPDATE "UserEmail"
                    SET Email = '{Email}'
                    WHERE
                        UserID = {ProfessorID};
                    
                ''')


                messages.success(request, f'Professor Record with ID: {ProfessorID} Updated Successfully')

            else:
                messages.error(request, 'ProfessorID does not exist in the Database')

            conn.commit()
            #Closing the connection
            c.close()

            return render(request, 'pr_update.html')
    else:
        return render(request, 'pr_update.html')


def studentDelete(request):
    if request.method == "POST":
        if request.POST.get('studentID'):
            StudentID = request.POST.get('studentID')

            conn = psycopg2.connect(
                database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
            )
            #Creating a cursor object using the cursor() method
            c = conn.cursor()

            c.execute('''SET SEARCH_PATH TO "researchHub"''')

            c.execute(f'''
                SELECT *
                FROM "UserEmail" AS ue
                WHERE
                    ue.UserID = {StudentID};
            ''')

            obj = c.fetchall()

            if len(obj) != 0:
                c.execute(f'''
                    DELETE FROM "UserDetails" WHERE UserID = {StudentID};
                    DELETE FROM "UserEmail" WHERE UserID = {StudentID};
                    DELETE FROM "Person" WHERE PersonID = {StudentID};
                    DELETE FROM "StudentProfessor" WHERE StudProfID = {StudentID};
                    DELETE FROM "Student" WHERE StudentID = {StudentID};
                ''')

                messages.success(request, f'Student Record with {StudentID} deleted successfully')
            else:
                messages.error(request, 'StudentID does not exist in the Database')
            conn.commit()
            #Closing the connection
            c.close()

            return render(request, 'st_delete.html')
    else:
        return render(request, 'st_delete.html')


def professorDelete(request):
    if request.method == "POST":
        if request.POST.get('professorID'):
            ProfessorID = request.POST.get('professorID')
            conn = psycopg2.connect(
                database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
            )
            #Creating a cursor object using the cursor() method
            c = conn.cursor()

            c.execute('''SET SEARCH_PATH TO "researchHub"''')

            c.execute(f'''
                SELECT *
                FROM "UserEmail" AS ue
                WHERE
                    ue.UserID = {ProfessorID};
            ''')

            obj = c.fetchall()

            if len(obj) != 0:
                c.execute(f'''
                    DELETE FROM "UserDetails" WHERE UserID = {ProfessorID};
                    DELETE FROM "UserEmail" WHERE UserID = {ProfessorID};
                    DELETE FROM "Person" WHERE PersonID = {ProfessorID};
                    DELETE FROM "StudentProfessor" WHERE StudProfID = {ProfessorID};
                    DELETE FROM "Professor" WHERE ProfessorID = {ProfessorID};
                ''')

                messages.success(request, f'Professor Record with {ProfessorID} deleted successfully')
            else:
                messages.error(request, 'ProfessorID does not exist in the Database')
            conn.commit()
            #Closing the connection
            c.close()

            return render(request, 'pr_delete.html')
    else:
        return render(request, 'pr_delete.html')


# View to show all the student records
def showStudentDetails(request):

    sortParameter = 'StudentID'

    if request.method == "POST":
        if request.POST.get('sortParameter'):
            sortParameter = request.POST.get('sortParameter')

    conn = psycopg2.connect(
        database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
    )
    #Creating a cursor object using the cursor() method
    c = conn.cursor()

    c.execute('''SET SEARCH_PATH TO "researchHub"''')
    c.execute(f'''
        SELECT st.StudentID, ue.Email, ud.Password, p.FirstName, p.MiddleName, p.LastName, p.HighestDegree, u.Name, st.YearOfPassing, st.Resume, sp.Followers
        FROM "Student" AS st
        INNER JOIN "StudentProfessor" AS sp
            ON st.StudentID = sp.StudProfID
        INNER JOIN "University" AS u
            ON sp.UniversityID = u.UniversityID
        INNER JOIN "Person" AS p
            ON st.StudentID = p.PersonID
        INNER JOIN "UserDetails" AS ud
            ON st.StudentID = ud.UserID
        INNER JOIN "UserEmail" AS ue
            ON st.StudentID = ue.UserID
        ORDER BY {sortParameter};  
    ''')
    # Fetch all the rows using fetchone() method.
    obj = c.fetchall()
    conn.commit()
    #Closing the connection
    c.close()
    # obj = Student.objects.raw('''select * from "Student"''')
    return render(request, 'studentRecords.html', {"data":obj})


def showProfessorDetails(request):

    sortParameter = 'ProfessorID'

    if request.method == "POST":
        if request.POST.get('sortParameter'):
            sortParameter = request.POST.get('sortParameter')

    conn = psycopg2.connect(
        database="202001406_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
    )
    #Creating a cursor object using the cursor() method
    c = conn.cursor()
    c.execute('''SET SEARCH_PATH TO "researchHub"''')
    c.execute(f'''
        SELECT pf.ProfessorID, ue.Email, ud.Password, p.FirstName, p.MiddleName, p.LastName, p.HighestDegree, u.Name,  sp.Followers, pf.WebsiteLink
        FROM "Professor" AS pf
        INNER JOIN "StudentProfessor" AS sp
            ON pf.ProfessorID = sp.StudProfID
        INNER JOIN "University" AS u
            ON sp.UniversityID = u.UniversityID
        INNER JOIN "Person" AS p
            ON pf.ProfessorID = p.PersonID
        INNER JOIN "UserDetails" AS ud
            ON pf.ProfessorID = ud.UserID
        INNER JOIN "UserEmail" AS ue
            ON pf.ProfessorID = ue.UserID
        ORDER BY {sortParameter}; 
    ''')
    # Fetch all the rows using fetchone() method.
    obj = c.fetchall()
    conn.commit()
    #Closing the connection
    c.close()
    return render(request, 'professorRecords.html', {"data":obj})