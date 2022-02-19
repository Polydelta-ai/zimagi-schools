<p align="center">
  <img width="460" height="150" src="assets/zimagi-logo.png">
</p>
<hr/>

<h1 align="center"><b>University</b> <i>and</i> <b>Educational Institution</b> <i>Data Module</i></h1>
<br/>

## Dependencies
<hr/>
<br/>

_This Zimagi module **requires** and **builds on** the following modules:_

<br/>

 * [**Organization Data Module**](https://github.com/Polydelta-ai/zimagi-organizations)

<br/>

## Overview
<hr/>
<br/>

This module provides school models that focus on program attendance and diversity data sourced and imported from the US Department of Education's College Scorecard API.

<br/>

## Components
<hr/>
<br/>

### Roles
<br/>

| _Name_ | _Description_ |
| ---- | ----------- |
| **school-admin** | _Administrative privileges over educational related data_ |
<br/>

### Data Models
<br/>

| _Name_ | _Description_ |
| ---- | ----------- |
| **school** | _Data model that extends organization with educational institution informational fields_ |
| **school_year** | _Data for an educational institution that is recorded on an annual basis_ |
<br/>

### Plugin Providers
<br/>

| _Name_ | _Type_ | _Description_ |
| ---- | ---- | ----------- |
| **college_scorecard** | **source** | _Requests educational institution data from US College Scorecard API_ |
| **college_scorecard_ownership_label** | **formatter** | _Translates an integer code into an ownership category label_ |
<br/>

### Importers and Calculations
<br/>

| _Name_ | _Type_ | _Description_ |
| ---- | ---- | ----------- |
| **college_scorecard_2019** | **import** | _Imports College Scorecard data from 2019 into internal data models_ |
| **school_year_program_enrollment_agriculture** | **calculation** | _Calculated field that finds total enrollment in agriculture programs_ |
| **school_year_program_enrollment_resources** | **calculation** | _Calculated field that finds total enrollment in resource programs (whatever those are?)_ |
| **school_year_program_enrollment_architecture** | **calculation** | _Calculated field that finds total enrollment in architecture programs_ |
| **school_year_program_enrollment_ethnic_cultural_gender** | **calculation** | _Calculated field that finds total enrollment in ethnic, cultural, and gender programs_ |
| **school_year_program_enrollment_communication** | **calculation** | _Calculated field that finds total enrollment in communications programs_ |
| **school_year_program_enrollment_communications_technology** | **calculation** | _Calculated field that finds total enrollment in communications technology programs_ |
| **school_year_program_enrollment_computer** | **calculation** | _Calculated field that finds total enrollment in computer programs_ |
| **school_year_program_enrollment_personal_culinary** | **calculation** | _Calculated field that finds total enrollment in personal culinary programs_ |
| **school_year_program_enrollment_education** | **calculation** | _Calculated field that finds total enrollment in educational programs_ |
| **school_year_program_enrollment_engineering** | **calculation** | _Calculated field that finds total enrollment in engineering programs_ |
| **school_year_program_enrollment_engineering_technology** | **calculation** | _Calculated field that finds total enrollment in engineering technology programs_ |
| **school_year_program_enrollment_language** | **calculation** | _Calculated field that finds total enrollment in language programs_ |
| **school_year_program_enrollment_family_consumer_science** | **calculation** | _Calculated field that finds total enrollment in consumer science programs_ |
| **school_year_program_enrollment_legal** | **calculation** | _Calculated field that finds total enrollment in legal programs_ |
| **school_year_program_enrollment_english** | **calculation** | _Calculated field that finds total enrollment in english programs_ |
| **school_year_program_enrollment_humanities** | **calculation** | _Calculated field that finds total enrollment in humanities programs_ |
| **school_year_program_enrollment_library** | **calculation** | _Calculated field that finds total enrollment in library programs_ |
| **school_year_program_enrollment_biological** | **calculation** | _Calculated field that finds total enrollment in biological programs_ |
| **school_year_program_enrollment_mathematics** | **calculation** | _Calculated field that finds total enrollment in mathematics programs_ |
| **school_year_program_enrollment_military** | **calculation** | _Calculated field that finds total enrollment in military programs_ |
| **school_year_program_enrollment_multidiscipline** | **calculation** | _Calculated field that finds total enrollment in multidisciplinary programs_ |
| **school_year_program_enrollment_parks_recreation_fitness** | **calculation** | _Calculated field that finds total enrollment in parks, recreation, and fitness programs_ |
| **school_year_program_enrollment_philosophy_religious** | **calculation** | _Calculated field that finds total enrollment in philosophy and religious programs_ |
| **school_year_program_enrollment_theology_religious_vocation** | **calculation** | _Calculated field that finds total enrollment in theology and religious_vocational programs_ |
| **school_year_program_enrollment_physical_science** | **calculation** | _Calculated field that finds total enrollment in physical_science programs_ |
| **school_year_program_enrollment_science_technology** | **calculation** | _Calculated field that finds total enrollment in science and technology programs_ |
| **school_year_program_enrollment_psychology** | **calculation** | _Calculated field that finds total enrollment in psychology programs_ |
| **school_year_program_enrollment_security_law_enforcement** | **calculation** | _Calculated field that finds total enrollment in security and law enforcement programs_ |
| **school_year_program_enrollment_public_administration_social_service** | **calculation** | _Calculated field that finds total enrollment in public administration and social service programs_ |
| **school_year_program_enrollment_social_science** | **calculation** | _Calculated field that finds total enrollment in social science programs_ |
| **school_year_program_enrollment_construction** | **calculation** | _Calculated field that finds total enrollment in construction programs_ |
| **school_year_program_enrollment_mechanic_repair_technology** | **calculation** | _Calculated field that finds total enrollment in mechanic and repair technology programs_ |
| **school_year_program_enrollment_precision_production** | **calculation** | _Calculated field that finds total enrollment in precision production programs_ |
| **school_year_program_enrollment_transportation** | **calculation** | _Calculated field that finds total enrollment in transportation programs_ |
| **school_year_program_enrollment_visual_performing** | **calculation** | _Calculated field that finds total enrollment in visual and performing arts programs_ |
| **school_year_program_enrollment_health** | **calculation** | _Calculated field that finds total enrollment in health programs_ |
| **school_year_program_enrollment_business_marketing** | **calculation** | _Calculated field that finds total enrollment in business marketing programs_ |
| **school_year_program_enrollment_history** | **calculation** | _Calculated field that finds total enrollment in history programs_ |
| **school_year_student_ethnicity_black** | **calculation** | _Calculated field that finds total enrollment of people classified as black_ |
| **school_year_student_ethnicity_hispanic** | **calculation** | _Calculated field that finds total enrollment of people classified as hispanic_ |
| **school_year_student_ethnicity_asian** | **calculation** | _Calculated field that finds total enrollment of people classified as asiany_ |
| **school_year_student_ethnicity_white** | **calculation** | _Calculated field that finds total enrollment of people classified as white_ |
| **school_year_student_ethnicity_aian** | **calculation** | _Calculated field that finds total enrollment of people classified as American Indian / Alaska Native_ |
| **school_year_student_ethnicity_nhpi** | **calculation** | _Calculated field that finds total enrollment of people classified as Native Hawaiian / Pacific Islander_ |
| **school_year_student_ethnicity_two_or_more** | **calculation** | _Calculated field that finds total enrollment of people classified as two or more ethnicities_ |
| **school_year_student_ethnicity_non_resident_alien** | **calculation** | _Calculated field that finds total enrollment of people classified as a non resident alien_ |
| **school_year_student_ethnicity_unknown** | **calculation** | _Calculated field that finds total enrollment of people classified as an unknown ethnicity_ |
| **school_year_student_ethnicity_white_non_hispanic** | **calculation** | _Calculated field that finds total enrollment of people classified as white and non hispanic_ |
| **school_year_student_ethnicity_black_non_hispanic** | **calculation** | _Calculated field that finds total enrollment of people classified as black and non hispanic_ |
| **school_year_student_ethnicity_asian_pacific_islander** | **calculation** | _Calculated field that finds total enrollment of people classified as asian / pacific islander_ |
<br/>

### Orchestration Profiles
<br/>

| _Name_ | _Description_ |
| ---- | ----------- |
| **build** | _Builds data centric Zimagi specifications_ |
<br/>

## How to Use
<hr/>
<br/>

_From the Linux command line interface:_

```bash
# Install the Zimagi application and remote client

pip install zimagi

# Initialize Zimagi platform and make any configuration updates

zimagi env get
#
# The first time executed the zimagi command will provide a link
# to the autogenerated configuration file for the user.  Make any
# changes to this file and run the zimagi command again to continue
# initializing the platform
#

# Install this module into the Zimagi platform

zimagi module add \
    https://github.com/Polydelta-ai/zimagi-schools.git \
    reference=main

#
# College Scorecard requires an API key
#
# Go here to register for one: https://api.data.gov/signup/
#
# Make sure the following environment variable is available
# to the Zimagi platform importing school related data
#
export ZIMAGI_COLLEGE_SCORECARD_API_KEY="{YOUR API KEY}"


# Import data and run derived calculations
zimagi import --tags=school
zimagi calculate --tags=school

# Work with the Zimagi school related data models
# (also available through the Command API)

zimagi school list --help
zimagi school get --help
zimagi school save --help
zimagi school remove --help
zimagi school clear --help

zimagi school year list --help
zimagi school year get --help
zimagi school year save --help
zimagi school year remove --help
zimagi school year clear --help

# Access school related data through the Data API

# List or search schools
curl https://localhost:5323/school
# Get JSON list of specific fields for searchable schools
curl https://localhost:5323/school/json
# Get a CSV export of specific fields for searchable schools
curl https://localhost:5323/school/csv
# Get a total count of searchable schools with field name (non NULL)
curl https://localhost:5323/school/count/{field_name}
# Get a list of unique field values for searchable schools (non NULL)
curl https://localhost:5323/school/values/{field_name}

# List or search school year information
curl https://localhost:5323/school_year
# Get JSON list of specific fields for searchable school year information
curl https://localhost:5323/school_year/json
# Get a CSV export of specific fields for searchable school year information
curl https://localhost:5323/school_year/csv
# Get a total count of searchable school year information with field name (non NULL)
curl https://localhost:5323/school_year/count/{field_name}
# Get a list of unique field values for searchable school year information (non NULL)
curl https://localhost:5323/school_year/values/{field_name}
```

_From a Python script:_

```bash
# First ensure zimagi is added to environment or requirements.txt
zimagi>=0.8.0
```

```python
# Import the zimagi package
import zimagi

# Create a message handler for streaming Command API messages
# (if you need or want)
def message_callback(message):
    message.display()

# Create API gateway (using default/development settings)
api = zimagi.Client(
    user = "admin",
    token = "uy5c8xiahf93j2pl8s00e6nb32h87dn3",
    encryption_key = "RFJwNYpqA4zihE8jVkivppZfGVDPnzcq",
    host = "localhost",
    command_port = 5123,
    data_port = 5323,
    message_callback = message_callback
)

# Add Zimagi module
#
# Make sure your script has access to the ZIMAGI_COLLEGE_SCORECARD_API_KEY
# environment variable.
#
api.extend('https://github.com/Polydelta-ai/zimagi-schools.git', 'main',
    provider = 'git'
)

# Execute any Zimagi command
#
# Can reference commands using:
#
# * space separated strings "user list" (CLI format)
# * slash separated strings "user/list" (API format)
# * dot separated strings   "user.list"
#
response = api.execute('school.list')

#
# Organization SDK interface
#

# Import and run derived calculations for schools
api.run_imports(tags = ['school'])
api.run_calculations(tags = ['school'])

# Save or update school related information
school_id = api.save('school', None, # key is autogenerated
    name = "Super School",
    city = "Washington",
    state = "DC",
    zipcode = 20024
)
api.save('school_year', None, # key is autogenerated
    school_id = school_id,
    year = 2030,
    student_size = 5000000000000
)

# List and search access schools (hyperlinked related objects)
results = api.list('school', name__endswith = "University")
results = api.list('school_year')

# Return field collections in various formats
json_results = api.json('school', fields = ['name', 'city', 'state'])
json_results = api.json('school_year', fields = ['school__name', 'year', 'student_size'])

df = api.dataframe('school', fields = ['name', 'zipcode'])
df = api.dataframe('school_year', fields = ['school__name', 'school__state', 'year', 'student_size'])

# Access school data
data = api.get('school', "{key}")
data = api.get('school_year', "{key}")

# Get school field information
results = api.values('school', 'name')
results = api.values('school_year', 'year')

count = api.count('school', 'name')
count = api.count('school_year', 'year')

# Remove schools
api.remove('school', "{key}")
api.remove('school_year', "{key}")

api.clear('school', ownership = 'Private For-Profit')
api.clear('school_year', year__lt = 2019)
```