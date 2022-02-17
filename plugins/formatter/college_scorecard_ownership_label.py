from systems.plugins.index import BaseProvider


class Provider(BaseProvider('formatter', 'college_scorecard_ownership_label')):

    labels = {
        1: 'Public',
        2: 'Private Non-Profit',
        3: 'Private For-Profit'
    }

    def format(self, value, record):
        if value is None:
            return value
        return self.labels[value]
