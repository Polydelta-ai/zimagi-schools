from django.conf import settings

from systems.plugins.index import BaseProvider

import requests


class Provider(BaseProvider('source', 'college_scorecard')):

    base_url = 'https://api.data.gov/ed/collegescorecard/v1/schools'

    school_fields = [
        'school.name',
        'school.city',
        'school.state',
        'school.zip',
        'school.school_url',
        'school.main_campus',
        'school.ownership'
    ]
    year_fields = [
        'admissions.admission_rate.overall',
        'student.size',
        'academics.program_percentage.agriculture',
        'academics.program_percentage.resources',
        'academics.program_percentage.architecture',
        'academics.program_percentage.ethnic_cultural_gender',
        'academics.program_percentage.communication',
        'academics.program_percentage.communications_technology',
        'academics.program_percentage.computer',
        'academics.program_percentage.personal_culinary',
        'academics.program_percentage.education',
        'academics.program_percentage.engineering',
        'academics.program_percentage.engineering_technology',
        'academics.program_percentage.language',
        'academics.program_percentage.family_consumer_science',
        'academics.program_percentage.legal',
        'academics.program_percentage.english',
        'academics.program_percentage.humanities',
        'academics.program_percentage.library',
        'academics.program_percentage.biological',
        'academics.program_percentage.mathematics',
        'academics.program_percentage.military',
        'academics.program_percentage.multidiscipline',
        'academics.program_percentage.parks_recreation_fitness',
        'academics.program_percentage.philosophy_religious',
        'academics.program_percentage.theology_religious_vocation',
        'academics.program_percentage.physical_science',
        'academics.program_percentage.science_technology',
        'academics.program_percentage.psychology',
        'academics.program_percentage.security_law_enforcement',
        'academics.program_percentage.public_administration_social_service',
        'academics.program_percentage.social_science',
        'academics.program_percentage.construction',
        'academics.program_percentage.mechanic_repair_technology',
        'academics.program_percentage.precision_production',
        'academics.program_percentage.transportation',
        'academics.program_percentage.visual_performing',
        'academics.program_percentage.health',
        'academics.program_percentage.business_marketing',
        'academics.program_percentage.history',
        'student.demographics.race_ethnicity.white',
        'student.demographics.race_ethnicity.black',
        'student.demographics.race_ethnicity.hispanic',
        'student.demographics.race_ethnicity.asian',
        'student.demographics.race_ethnicity.aian',
        'student.demographics.race_ethnicity.nhpi',
        'student.demographics.race_ethnicity.two_or_more',
        'student.demographics.race_ethnicity.non_resident_alien',
        'student.demographics.race_ethnicity.unknown',
        'student.demographics.race_ethnicity.white_non_hispanic',
        'student.demographics.race_ethnicity.black_non_hispanic',
        'student.demographics.race_ethnicity.asian_pacific_islander'
    ]


    def item_columns(self):
        return self.school_fields + [ 'year' ] + self.year_fields


    def load_items(self, context):
        year_fields = [ "{}.{}".format(self.field_year, field) for field in self.year_fields ]
        query_options = [
            "api_key={}".format(settings.COLLEGE_SCORECARD_API_KEY),
            "fields={}".format(",".join(self.school_fields + year_fields)),
            'school.degrees_awarded.highest=3,4'
        ]
        page = self.command.get_state('college_scorecard_page', 1)

        while True:
            request_params = "&".join(query_options + [ "page={}".format(page) ])

            response = requests.get("{}?{}".format(self.base_url, request_params))
            results = response.json()

            if results['metadata']['page'] > results['metadata']['total']:
                break

            for record in results['results']:
                processed_record = {}
                for field, value in record.items():
                    processed_record[field.removeprefix("{}.".format(self.field_year))] = value

                yield processed_record

            page += 1
            self.command.set_state('college_scorecard_page', page)
            self.command.sleep(1)

        self.command.delete_state('college_scorecard_page')

    def load_item(self, school, context):
        school_fields = []
        for field in self.school_fields:
            school_fields.append(school[field])

        year_fields = [ self.field_year ]
        for field in self.year_fields:
            year_fields.append(school[field])

        return school_fields + year_fields
