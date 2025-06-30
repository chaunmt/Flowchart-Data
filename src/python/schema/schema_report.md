## Schema format:
- Empty value is represented by null.

### Only use on data side:
```json
    "CourseShell": {
        "key": "CourseShell.id",
        "local": {  // Stored locally
            "id": "number",         // PeopleSoft course ID
            "code": "string",       // Code
            "subject": "string",    // Course subject code
            "number": "number",     // Course number
            "honors": "bool"        // Determined from Code
        }
    }
```

### Use on client side:
```json
    "Course": {
        "key": "Course.id",
        "local": {  // Stored locally
            "id": "number",              // PeopleSoft course ID
            "code": "string",           // Code
            "subject": "string",        // Course subject code
            "number": "number",         // Course number
            "honors": "bool",           // Determined from Code
            "writing": "bool",          // Twin Cities: This course is approved as Writing Intensive        
            "fullname": "string",       // Course name
            "prereq": "PrereqFormat"    // Determined from info
        },
        "additional" {  // Might need to add
            "target_courses": "list[id]",
            "target_programs": "list[id]",
            "attributes": "list[string]",   // tags
            "alternatives": "list[id]",     // alternative courses
        }
    }
```


```json
    "PrereqFormat.prereq" : "string (id) or dict (with 'and', 'or' for keys)"        
```

```json
    "Program": {
    }
```