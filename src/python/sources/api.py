"""
TODO
"""

from python.sources.format import JSONHandler
from python.checker.prereq import CourseChecker
from python.splitter.string import StringSplitter
from python.splitter.prereq import CourseInfoSplitter

class CourseDogAPI:
    """
    Class to help handle Course Dog's API.
    """
    
    #############################################################################
    @staticmethod
    def get_full_file_path(school_id, subject, is_honors):
        """
        Get full file path for output file.
        """

        # Set school's file path
        if school_id == 'umn_umntc_peoplesoft':
            file_path = '../../data/UMNTC/'
        else:
            file_path = '../../data/Other/'

        # Set course's file path
        if is_honors:
            file_path = file_path + 'Course/Honor/'
        else:
            file_path = file_path + 'Course/General/'

        # Set file name based on subject
        file_name = subject + '.json'

        return file_path + file_name

    #############################################################################
    @staticmethod
    def generate_url(school_id, subject):
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
            + school_id
            + '/courses/search/$filters?'  # Search courses
            + 'subjectCode=' + subject_code
            + '&returnFields=' + return_fields
            + '&limit=' + limit
        )

        return api_url

    #############################################################################
    @classmethod
    def get_json(cls, school_id, subject, is_program):
        """
        Get raw JSON data from CourseDog API.
        """

        # Request data from CourseDog API
        if is_program:
            # TODO Add work for program
            data = {'No work on program'}
        else:
            data = JSONHandler.get_from_url(cls.generate_url(school_id, subject))

        print('Data is fetched for ' + subject)
        return data

    #############################################################################
    @staticmethod
    def find_prereq_splitter(info):
        """
        The the splitter substring for prerequisites from info string.
        """

        # Possible split patterns for prerequisites
        split_patterns = [
            "prereq:",
            "prerequisite:",
            "prerequisites:",
            "prereq",
            "prerequisite",
            "prerequisites"
        ]

        # Find a split pattern in info string
        split_pattern = "\n\n\n\n\n"
        for pattern in split_patterns:
            if pattern in info:
                return pattern

        return split_pattern

    #############################################################################
    @classmethod
    def get_prereq_string(cls, info):
        """
        Get the prerequisites string from the info string.
        """

        # Split prereq from info
        info = info.lower()
        split_pattern = cls.find_prereq_splitter(info)
        splitted_info = StringSplitter.at_substring(info, split_pattern)

        # Combine all founded prereq into one string
        if len(splitted_info) > 1:
            prereq_string = '\n'.join(splitted_info[1:])
        else:
            prereq_string = ''

        return prereq_string

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

    #############################################################################
    def process_course_shell(data, is_honors):
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

        return processed_data

    #############################################################################
    def process_course_full(data, is_honors):
        """
        Process JSON data to get Course JSON.
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
                    'honors' : honors,
                    'writing' : '',
                    'name' : '',
                    'fullname' : '',
                    'info' : '',
                    'prereq' : ''
                    
                })

        return processed_data

    #############################################################################
    @classmethod
    def get_output_file(cls, school_id, subject, is_program, is_honors):
        """
        Generate output json file.
        """

        # Get raw json data from CourseDog API
        raw = cls.get_json_from_dogs(school_id, subject, is_program)
        raw = raw['data']

        # Processed json data by subject
        if subject == 'allCourses':
            if is_program:
                processed =  cls.process_program_shell(raw, is_honors)
            processed = cls.process_course_shell(raw, is_honors)
        else:
            if is_program:
                processed =  cls.process_program_full(raw, is_honors)
            processed = cls.process_course_full(raw, is_honors)

        # Write processed json data to output file
        path = cls.get_full_file_path(school_id, subject, is_honors)
        JSONHandler.write_to_path(processed, path)

    #############################################################################
    @classmethod
    def get_all_json(cls):
        """
        Get all JSON files.
        """

        cls.get_output_file('umn_umntc_peoplesoft', 'allCourses', False, False)
        # TODO get JSON from all subjects.
        # TODO get JSON from all programs.
