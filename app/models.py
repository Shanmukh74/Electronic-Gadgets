from flask_mysqldb import MySQL

# Initialize MySQL
mysql = MySQL()

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get_user_by_username(username):
        cur = mysql.connection.cursor()
        try:
            cur.execute("SELECT * FROM User WHERE username = %s", [username])
            user_data = cur.fetchone()
            if user_data:
                return User(id=user_data[0], username=user_data[1], email=user_data[2], password=user_data[3])
            return None
        except Exception as e:
            print(f"Error fetching user: {str(e)}")
            return None
        finally:
            cur.close()

    @staticmethod
    def create_user(username, email, hashed_password):
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO User (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error creating user: {str(e)}")
            return False
        finally:
            cur.close()

class Course:
    def __init__(self, id, title, description, content):
        self.id = id
        self.title = title
        self.description = description
        self.content = content

    @staticmethod
    def get_all_courses():
        cur = mysql.connection.cursor()
        try:
            cur.execute("SELECT * FROM Course")
            courses = cur.fetchall()
            return [Course(id=course[0], title=course[1], description=course[2], content=course[3]) for course in courses]
        except Exception as e:
            print(f"Error fetching courses: {str(e)}")
            return []
        finally:
            cur.close()

    @staticmethod
    def get_course_by_id(course_id):
        cur = mysql.connection.cursor()
        try:
            cur.execute("SELECT * FROM Course WHERE id = %s", [course_id])
            course_data = cur.fetchone()
            if course_data:
                return Course(id=course_data[0], title=course_data[1], description=course_data[2], content=course_data[3])
            return None
        except Exception as e:
            print(f"Error fetching course: {str(e)}")
            return None
        finally:
            cur.close()

    @staticmethod
    def create_course(title, description, content):
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO Course (title, description, content) VALUES (%s, %s, %s)", (title, description, content))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error creating course: {str(e)}")
            return False
        finally:
            cur.close()
