## Schema format:
- Empty value is represented by null.
- `cdog` means the relative object (course/program) fetched from coursedog.

### Only use on data side:
```json
    "CourseShell": {
        "key": "CourseShell.id",
        "local": {  // Stored locally
            "id": "string",
            "code": "string",
            "subject": "string",
            "number": "number",
            "honors": "bool"
        },
        "online": {  // Fetch on run time
        }
    }
```

### Use on client side:
```json
    "Course": {
        "key": "Course.id",
        "local": {  // Stored locally
            "id": "string",             // cdog._id
            "subject": "string",        // cdog.subjectCode
            "number": "number",         // cdog.courseNumber (without suffix)
            "honors": "bool",           // Determined from suffix of cdog.courseNumber
            "writing": "boolean",       // Determined from suffix of cdog.courseNumber        
            "fullname": "string",       // cdog.longname
            "prereq": "PrereqFormat"    // Extracted from info
        },
        "additional" {  // Might need to add
            "target_courses": "list[id]",
            "target_programs": "list[id]",
            "attributes": "list[string]",   // tags
            "alternatives": "list[id]",     // alternative courses
        },
        "online": {  // Fetch on run time
            "name": "string",   // cdog.name
            "info": "string",   // cdog.description
            // more tbd
        }
    }
```


```json
    "PrereqFormat.prereq" : "string (id) or dict (with 'and', 'or' for keys)"        
```

```json
    "Program": {
        "key": "Program.id",
        "local": {
            "id": "string"  // cdog.courseGroupId
        },
        "online": {
            "num_req_required": "number",   // cdog.number
        }
    }
```