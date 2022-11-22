from django.db import models

# Create your models here.

class UserEmail(models.Model):
    #Model representing UserEmail

    UserID = models.IntegerField(primary_key=True, unique=True, null=False)
    Email = models.CharField(max_length=200, help_text='Enter your University email', null=False, blank=False)

    def __str__(self):
        return self.UserID

    class Meta:
        db_table="UserEmail"


class UserDetails(models.Model):
    #Model representing a User details

    UserID = models.IntegerField(primary_key=True, unique=True, null=False)
    Role = models.CharField(max_length=200, null=False, blank=False)
    Password = models.CharField(max_length=200, help_text='Enter your Password', null=False, blank=False)

    def __str__(self):
        return self.UserID

    class Meta:
        db_table="UserDetails"

class Person(models.Model):
    #Model representing a person

    PersonID = models.IntegerField(primary_key=True, unique=True, null=False)

    FirstName = models.CharField(max_length=200, help_text='Enter your first name', null=False, blank=False)

    MiddleName = models.CharField(max_length=200, help_text='Enter your middle name', null=False, blank=False)

    LastName = models.CharField(max_length=200, help_text='Enter your last name', null=False, blank=False)

    HighestDegree = models.CharField(max_length=200, help_text='Enter your highest degree obtained', null=False, blank=False)

    def __str__(self):
        return self.PersonID

    class Meta:
        db_table="Person"

class University(models.Model):
    UniversityID = models.IntegerField(primary_key=True, unique=True, null=False)

    Name = models.CharField(max_length=200, null=False, blank=False)

    WebsiteLink = models.CharField(max_length=200, null=True, blank=True)

    DomainName = models.CharField(max_length=200, null=False, blank=False)

    DiscussionLink = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.UniversityID
    
    class Meta:
        db_table="University"


class StudentProfessor(models.Model):
    StudProfID = models.IntegerField(primary_key=True, unique=True, null=False)

    Followers = models.IntegerField(null=False)

    UniversityID = models.ForeignKey(University, on_delete=models.RESTRICT, null=False, blank=False)

    def __str__(self):
        return self.StudProfID

    class Meta:
        db_table="StudentProfessor"

class Student(models.Model):
    StudentID = models.IntegerField(primary_key=True, unique=True, null=False)

    YearOfPassing = models.IntegerField(null=False, blank=False)

    Resume = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.StudentID
    
    class Meta:
        db_table="Student"

class Professor(models.Model):
    ProfessorID = models.IntegerField(primary_key=True, unique=True, null=False)

    WebsiteLink = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.ProfessorID
    
    class Meta:
        db_table="Professor"

