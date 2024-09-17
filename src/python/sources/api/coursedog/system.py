"""
Classes to help handle Course Dog's API.
"""

from python.sources.format import JSONHandler
from python.checker.course import CourseChecker
from python.splitter.course import CourseInfoSplitter
from python.extractor.course import PrereqExtractor

class CourseSystem:
    """
    Handling Course Dog's API works for Courses.
    """

    def __init__(self, school_id: str) -> None:
        """
        Initalize a CourseSystem object.
        """

        if school_id != 'umn_umntc_peoplesoft':
            raise ValueError('This system only works with UMNTC data from CourseDog.')

        self._school_id = school_id
        self._data_path = "../data/UMNTC/"
        self._general_path = "Course/General/"
        self._honors_path = "Course/Honors/"

    #############################################################################
    def generate_url(self, subject: str) -> str:
        """
        Generate CourseDog's API URL for Course.
        """

        # Set fields
        subject_code = subject
        if subject == 'allCourses':
            subject_code = ''

        limit = 'infinity'

        return_fields = (
            'institutionId,'
            + 'code,'
            + 'subjectCode,'
            + 'courseNumber,'
            + 'name,'
            + 'longName,'
            + 'description'
        )

        # Set URL
        api_url = (
            'https://app.coursedog.com/api/v1/cm/'  # API
            + self._school_id
            + '/courses/search/$filters?'  # Search courses
            + 'subjectCode=' + subject_code
            + '&returnFields=' + return_fields
            + '&limit=' + limit
        )

        return api_url

    #############################################################################
    def get_full_file_path(self, subject: str, is_honors: bool) -> str:
        """
        Get full file path for output file.
        """

        if is_honors:
            return (
                self._data_path + self._honors_path + subject + ".json"
            )
        else:
            return (
                self._data_path + self._general_path + subject + ".json"
            )

    #############################################################################
    def get_all_subjects_list_json(self):
        """
        Get a JSON file with a list of all subjects' code and their name.
        """

        data = JSONHandler.get_from_path(self._data_path + 'allSubjects.json')

        print('Data is fetched for list of all subjects.')
        return data

    #############################################################################
    def get_subject_courses_input_json(self, subject: str):
        """
        Get raw JSON data for a subject's all courses from CourseDog API.
        """

        # Request data from CourseDog API
        data = JSONHandler.get_from_url(self.generate_url(subject))

        print('Data is fetched for ' + subject)
        return data

    #############################################################################
    def get_subject_courses_output_json(self, subject: str, is_honors: bool):
        """
        Generate output json file for courses by subject and honors type.
        """

        # Get raw json data from CourseDog API
        raw = self.get_subject_courses_input_json(subject)
        raw = raw['data']

        # Processed json data by subject
        if subject == 'allCourses':
            processed = self.process_course_shell(raw, is_honors)
        else:
            processed = self.process_course_full(raw, is_honors)

        # Write processed json data to output file
        path = self.get_full_file_path(subject, is_honors)
        JSONHandler.write_to_path(path, processed)
    
    def get_general_courses_output_json(self):
        """
        Generate output json for general courses.
        """
        
        # Get raw json data from CourseDog API
        raw = self.get_subject_courses_input_json('allCourses')
        raw = raw['data']
        
        processed = self.process_course_full(raw, False)
        
        # Write processed json data to output file
        path = self.get_full_file_path('general', False)
        JSONHandler.write_to_path(path, processed)

    #############################################################################
    def process_course_shell(self, data, is_honors: bool) -> list:
        """
        Process JSON data to get CourseShell JSON.
        """

        processed_data = []

        for course in data:
            # Split a course's number and its suffix
            number, suffix = CourseInfoSplitter.split_num_suf(course['courseNumber'])

            # Check course's type
            honors = CourseChecker.is_honors_suf(suffix)

            # Only get required courses
            if honors == is_honors:
                # Map value to corresponding key
                processed_data.append({
                    'uid' : course['institutionId'],
                    'code' : course['code'],
                    'subject' : course['subjectCode'],
                    'number' : number,
                    'honors' : honors
                })
            # TODO modify course shell to either get all courses honors or general depend on a parameter maybe?

        return processed_data

    #############################################################################
    def process_course_full(self, data, is_honors: bool) -> list:
        """
        Process JSON data to get Course JSON.
        """

        processed_data = {}

        for course in data:
            # Split a course's number and its suffix
            number, suffix = CourseInfoSplitter.split_num_suf(course['courseNumber'])

            # Check course's type
            honors = CourseChecker.is_honors_suf(suffix)
            writing = CourseChecker.is_writing_suf(suffix)

            # Process info string into a logical dictionary of prerequisite courses
            prereq = PrereqExtractor(course['description'], course['subjectCode'], is_honors)
            prereq.extract()
            prereq = prereq.get_prereq()

            # Only get required courses
            if honors == is_honors:     # TODO this is true for general but not for honors
                # Map value to corresponding key
                processed_data[course['institutionId']] = {
                    'uid' : course['institutionId'],
                    'code' : course['code'],
                    'subject' : course['subjectCode'],
                    'number' : number,
                    'honors' : honors,
                    'writing' : writing,
                    'name' : course['name'],
                    'fullname' :  course['longName'],
                    'info' : course['description'],
                    'prereq' : prereq           
                }
            # TODO for honors courses
            # if course is honors --> get
            # if course's prereq includes honors courses -> get

        return processed_data

class ProgramSystem:
    """
    """

    #############################################################################
    @staticmethod
    def get_full_file_path(self, school_id: str, type: str, is_honors: bool):
        """
        """

    #############################################################################
    @classmethod
    def get_subject_courses_input_json(cls, school_id, type):
        """
        Get raw JSON data from CourseDog API.
        """

        # TODO Request data from CourseDog API
        data = {'No work on program'}

        print('Data is fetched for ' + type)
        return data

    #############################################################################
    @classmethod
    def get_subject_courses_output_json(cls, school_id, type, is_honors):
        """
        Generate output json file.
        """

        # Get raw json data from CourseDog API
        raw = cls.get_subject_courses_input_json(school_id, type)
        raw = raw['data']

        # Processed json data by type
        if type == 'allCourses':
            processed =  cls.process_program_shell(raw, is_honors)
        else:
            processed =  cls.process_program_full(raw, is_honors)

        # Write processed json data to output file
        path = cls.get_full_file_path(school_id, type, is_honors)
        JSONHandler.write_to_path(processed, path)

    #############################################################################
    def process_program_shell(data, is_honors):
        """
        TODO
        """

    #############################################################################
    def process_program_full(data, is_honors):
        """
        Process JSON data to get Course JSON.
        """

        processed_data = []

        for course in data:
            # Split a course's number and its suffix
            number, suffix = CourseInfoSplitter.split_num_suf(course['courseNumber'])

            # Check course's type
            honors = CourseChecker.is_honors_suf(suffix)
            writing = CourseChecker.is_writing_suf(suffix)

            # Get prereq
            prereq = [] # TODO

            # Only get required courses
            if honors == is_honors:
                # Map value to corresponding key
                processed_data.append({
                    'uid' : course['institutionId'],
                    'code' : course['code'],
                    'subject' : course['subjectCode'],
                    'number' : number,
                    'honors' : honors,
                    'writing' : writing,
                    'name' : course['name'],
                    'fullname' : course['longname'],
                    'info' : course['description'],
                    'prereq' : prereq
                })

        return processed_data
