# 📖 Introduction
This repository includes all classes and methods that are used to fetch, process, write, and publish data on to the data server for [Course Flowchart](https://github.com/chaunmt/Interactive-Prerequisite-Flowchart).

__Table of Contents__
- [📖 Introduction](#-introduction)
- [📈 Data](#-data)
  - [1. Where are they from?](#1-where-are-they-from)
  - [2. What are they like?](#2-what-are-they-like)
  - [3. How to access them?](#3-how-to-access-them)
  - [4. Python UML](#4-python-uml)
- [🐍 Python](#-python)
- [🔍 Test](#-test)
- [🔖 Archive](#-archive)
  
# 📈 Data
## 1. Where are they from?
- The data is fetched from [Coursedog Curriculum API](https://coursedogcurriculum.docs.apiary.io/#reference/courses). This is the data sources used by the University of Minnesota's [ASR](https://asr-custom.umn.edu/) (Academic Support Resources Application Development) and [Gopher Grade](https://umn.lol/).
## 2. What are they like?
- Necessary data are read as JSON from Coursedog API. They are then processed based on the project's usages. Prerequisites data are heavily processed from a natural language format into a logical structure that increases readability and allows ease of access for [Course Flowchart](https://github.com/chaunmt/Interactive-Prerequisite-Flowchart) graphbuilders. 
## 3. How to access them?
- Data are saved in the data folder.
- Processed data will also be added into the main repository ([Course Flowchart](https://github.com/chaunmt/Interactive-Prerequisite-Flowchart)). They can then be access by the Access (.ts or .js) file in the data folder.
- Attempts were made to add the data into a PostgreSQL on Vercel. However, Vercel's low limits for free tier and the complicated nature of the nested logical structure of prerequisites hinders our progress to transfer to this format. Some data (Subject's code and name etc.) are already availlable on this server and can be accessed if desired. Please contact the [project lead](mailto:truon417@umn.edu) if you want to access these data.
## 4. Python UML
<img src="https://github.com/chaunmt/Flowchart-Data/blob/main/img/CourseFlowchart-coursesys_uml_light.drawio.png"></img>

# 🐍 Python
- Currently, our system involves a Course System ([Course Flowchart](https://github.com/chaunmt/Interactive-Prerequisite-Flowchart)) and a Program System (to be implemented as a collaboration result with [Gopher Major Planner](https://gophermajorplanner-steven-tams-projects.vercel.app/)).
- This is a sketch describes how client communicate with our project:
<img src="https://github.com/chaunmt/Flowchart-Data/blob/main/img/CourseFlowchart-client.drawio.png"></img>
- To run the project from src directory:
  ```
  python3 -m python.client
  ```
- The Python project involes 7 majors packages, each associate with a certain task. Each packages can include multiple packages or modules associated with a specific task or system.
- The first 3 packages are low level tools:
  + Checker
    - Check whether something is true or false.
  + Splitter
    - Split an object into a list of something.
  + Converter
    - Convert an object from one type (or form) to another.

- The next 2 packages are used to extract and sanitize a course's prerequisites.
  + Extractor
    - An interface calling to pre-process, extract, and post-process a course's prerequisites.
  + Filter
    - A tool used to remove unnecessary parts from an object.

- The last 2 packages are other tools more related to our API and main project ([Course Flowchart](https://github.com/chaunmt/Interactive-Prerequisite-Flowchart)):
  + Schema
    - These schemas are used mostly as a reference point to the schemas used in [Course Flowchart](https://github.com/chaunmt/Interactive-Prerequisite-Flowchart).
    - They are also used to post-process and test our data.
  + Sources
    - This packages contains all handlers to the file systems and API requests.

# 🔍 Test
- The test directory contains all test modules for our project.
- To run all tests:
  ```
  pytest -q
  ```
- To run a module test:
  ```
  pytest -q [file_path]/[test_module_name].py
  ```

# 🔖 Archive
  - Obsolete codes that are used for references.
