// Using file system
let fs = require("fs");

/** Export JSON file from Course Dogs API */
function exportDogs(PROGRAM) {
  const schoolId = "umn_umntc_peoplesoft";
  let fileName = (PROGRAM == "")? "allPrograms.json" : PROGRAM + ".json";
  let filePath = "../../data/Test/UMNTC/Program/";
  let programGroupId = "programGroupIds=" + PROGRAM;
  let active = "&isActive=true&includePending=false"; // include only active program
  let returnFields = 
    "&returnFields=" +
    "";
  let limit = "&limit=infinity";

  let url =
    "https://app.coursedog.com/api/v1/cm/" +
    schoolId +
    "/programs/search/$filters?" +
    programGroupId +
    returnFields +
    active +
    limit;

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      let programs =
        data.data.map((program) => {
          return {
            code: program.code || "",
            name: program.catalogDisplayName || "",
            status: program.status || "",
            type: program.type || "",
            degreeGranter: program.customFields.cdDegreeGrantingCollege || "",
            classification: program.nscClassification || "",
            diploma: program.diplomaDescription || "",
            info: program.customFields.cdProgramDescr || "",
            level: program.customFields.cdProgramCareer || "",
            accredited: program.customFields.cdProgramAccredited || "",
            minProgramCredit: program.customFields.cdProgramCreditsProgramMin || "",
            maxProgramCredit: program.customFields.cdProgramCreditsProgramMax || "",
            minDegreeCredit: program.customFields.cdProgramCreditsDegreeMin || "",
            maxDegreeCredit: program.customFields.cdProgramCreditsDegreeMax || "",
            requirements: {
              admission: {
                tests: {
                  TOEFL: program.customFields.cdProgramAdmissionTOEFL || "",
                  IELTS: program.customFields.cdProgramAdmissionIELTS || "",
                  GRE: program.customFields.cdProgramAdmissionGRE || "",
                  GMAT: program.customFields.cdProgramAdmissionGMAT || "",
                  MCAT: program.customFields.cdProgramAdmissionMCAT || "",
                  LSAT: program.customFields.cdProgramAdmissionLSAT || "",
                  Other: program.customFields.cdProgramAdmissionOtherTest || "",
                },
                minCredits: program.customFields.cdProgramAdmissionCourseCreditMin || "",
                preMajorStatus: program.customFields.cdProgramAdmissionPreMajorStatus || "",
                GPA: {
                  min: program.customFields.cdProgramAdmissionGPACollAdmitMin || "",
                  minTransIUT: program.customFields.cdProgramAdmissionGPATransIUTMin || "",
                  minTrans: program.customFields.cdProgramAdmissionGPATransMin || "",
                  rationale: program.customFields.cdProgramAdmissionGPARationale || ""
                },
                info: program.requirementLevels
              },
              language: {
                sem: program.customFields.cdProgramReqLanguageSemesters,
                undergrad: program.customFields.cdProgramReqLanguageUgrd,
                graduate: program.customFields.cdProgramReqLanguageGrad
              }
            },
            requisites: program.requisites.map(
              (req) => {
                let subreq = req.subRules || req.values;
                return {
                  id: req.id,
                  name: req.name,
                  condition: req.type,
                  rules: subreq
                }
              }
            )
          }
        })

      let i = 0;
      while (i < programs.length) {
        if (programs[i] == null) {
          programs.splice(i, 1)
        } else {
          i++;
        }
      }

      fs.writeFile(filePath + fileName, JSON.stringify(programs, null, 2), (error) => {
        if (error) {
          console.error(
            "Error exporting data to JSON file" + fileName + ":",
            error,
          );
        } else {  
          console.log("Data exported to", fileName);
        }
      });
    });
}

exportDogs("");