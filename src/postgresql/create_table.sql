-- Subject table holds a subject's code and its name
CREATE TABLE Subject(
    code VARCHAR(10) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (code)
);

-- CourseShell is similar to our CourseShell in JSON.
-- It holds basic information of a course.
CREATE TABLE CourseShell(
    uid VARCHAR(10) NOT NULL,
    code VARCHAR(10) NOT NULL,
    subject VARCHAR(10) NOT NULL,
    number INT NOT NULL,
    honors BOOLEAN NOT NULL,
    PRIMARY KEY (uid),
    FOREIGN KEY (subject) REFERENCES Subject (code)
);

-- CourseDetail holds extra information of a course.
CREATE TABLE CourseDetail(
    uid VARCHAR(10) NOT NULL,
    writing BOOLEAN NOT NULL,
    name VARCHAR(255),
    fullname VARCHAR(255),
    info VARCHAR(3000),
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES CourseShell (uid)
);

-- Prereq holds the relationship of 2 course by a unique key (target_uid, prereq_uid)
CREATE TABLE Prereq (
    target_uid VARCHAR(10) NOT NULL,
    prereq_uid VARCHAR(10) NOT NULL,
    PRIMARY KEY (target_uid, prereq_uid),
    FOREIGN KEY (target_uid) REFERENCES CourseShell (uid),
    FOREIGN KEY (prereq_uid) REFERENCES CourseShell (uid)
);
