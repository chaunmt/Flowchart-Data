-- Example: Create a view that holds all CSCI courses' info
CREATE VIEW CSCI AS
SELECT *
FROM CourseShell, CourseDetail
WHERE subject = "CSCI";
