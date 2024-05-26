from Helper.json_handler import *
from Helper.Checker.course_checker import *
from Helper.string_splitter import *
from Filter.prereq_filter import *

###############################################################################
def get_full_filepath(schoolId, subject, isHonor):
  """
  Get full file path for output file.
  """

  # Set school's file path
  if schoolId == 'umn_umntc_peoplesoft':
    filePath = '../../data/UMNTC/'
  else:
    filePath = '../../data/Other/'

  # Set course's file path
  if isHonor:
    filePath = filePath + 'Course/Honor/'
  else:
    filePath = filePath + 'Course/General/'

  # Set file name based on subject
  fileName = subject + '.json'

  return filePath + fileName

###############################################################################
def generate_Dog_URL(schoolId, subject):
  """
  Generate CourseDog's API URL for Course.
  """

  # Set fields
  subjectCode = subject
  if subject == 'allCourses':
    subjectCode = ''
  
  limit = 'infinity'

  returnFields = (
    'institutionId,'
    + 'code,'
    + 'subjectCode,'
    + 'courseNumber,'
    + 'name,'
    + 'longName,'
    + 'description'
  )

  # Set URL
  apiURL = (
    'https://app.coursedog.com/api/v1/cm/'  # API
    + schoolId
    + '/courses/search/$filters?'  # Search courses
    + 'subjectCode=' + subjectCode
    + '&returnFields=' + returnFields
    + '&limit=' + limit
  )

  return apiURL

###############################################################################
def get_JSON_from_Dogs(schoolId, subject, isProgram):
  """
  Get raw JSON data from CourseDog API.
  """

  # Request data from CourseDog API
  if isProgram:
    # TODO Add work for program
    data = {'No work on program'}
  else:
    data = JSONHandler.get_from_url(generate_Dog_URL(schoolId, subject))

  print('Data is fetched for ' + subject)
  return data

###############################################################################
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

###############################################################################
def get_prereq_string(info):
  """
  Get the prerequisites string from the info string.
  """
  
  # Split prereq from info
  info = info.lower()
  split_pattern = find_prereq_splitter(info)
  splitted_info = StringSplitter.at_substring(info, split_pattern)

  # Combine all founded prereq into one string
  if len(splitted_info) > 1:
    prereq_string = '\n'.join(splitted_info[1:])
  else:
    prereq_string = ''

  return prereq_string

###############################################################################
def process_program_shell(data, getHonors):
  """
  """

  # TODO

###############################################################################
def process_program_full(data, getHonors):
  """
  Process JSON data to get Course JSON.
  """

  processed_data = []

  for course in data:
    # Split a course's number and its suffix
    number, suffix = StringSplitter.separate_number_suffix(course['courseNumber'])

    # Check course's type
    honors = CourseChecker.is_honor(suffix)
    writing = CourseChecker.is_writing(suffix)

    # Get prereq
    prereq = [] # TODO

    # Only get required courses
    if honors == getHonors:
      # Map value to corresponding key
      processed_data.append({
        'uid' : course['institutionId'],
        'code' : course['code'],
        'subject' : course['subjectCode'],
        'number' : number,
        'honors' : honors,
        'writingIntensive' : writing,
        'name' : course['name'],
        'fullname' : course['longname'],
        'info' : course['description'],
        'prereq' : prereq
      })

  return processed_data

###############################################################################
def process_course_shell(data, getHonors):
  """
  Process JSON data to get CourseShell JSON.
  """

  processed_data = []

  for course in data:
    # Split a course's number and its suffix
    number, suffix = StringSplitter.separate_number_suffix(course['courseNumber'])

    # Check course's type
    honors = CourseChecker.is_honor(suffix)

    # Only get required courses
    if honors == getHonors:
      # Map value to corresponding key
      processed_data.append({
        'uid' : course['institutionId'],
        'code' : course['code'],
        'subject' : course['subjectCode'],
        'number' : number,
        'honors' : honors
      })

  return processed_data

###############################################################################
def process_course_full(data, getHonors):
  """
  Process JSON data to get Course JSON.
  """
  
  # TODO

###############################################################################
def get_output_file(schoolId, subject, isProgram, isHonor):
  """
  Generate output json file.
  """

  # Get raw json data from CourseDog API
  raw = get_JSON_from_Dogs(schoolId, subject, isProgram)
  raw = raw['data']

  # Processed json data by subject
  if subject == 'allCourses':
    if isProgram:
      processed =  process_program_shell(raw, isHonor)
    processed = process_course_shell(raw, isHonor)
  else:
    if isProgram:
      processed =  process_program_full(raw, isHonor)
    processed = process_course_full(raw, isHonor)
  
  # Write processed json data to output file
  path = get_full_filepath(schoolId, subject, isHonor)
  JSONHandler.write_to_path(processed, path)

###############################################################################
def get_all_JSON():
  """
  Get all JSON files.
  """

  get_output_file('umn_umntc_peoplesoft', 'allCourses', False, False)
  # TODO get JSON from all subjects.
  # TODO get JSON from all programs.

if __name__ == '__main__':
  get_all_JSON()