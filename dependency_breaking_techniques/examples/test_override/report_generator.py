class ReportSaver:
    def __init__(self):
        raise NotImplementedError()
    
    def save_report(self, report):
        raise NotImplementedError()
    
class ReportGenerator:
    def __init__(self):
        # self.report_saver = ReportSaver()
        self.report_saver = self.make_report_saver()

    def make_report_saver(self):
        return ReportSaver()

    def make_report(self, name, mean, var):
        report = {'name': name, 'mean': mean, 'var': var}
        return report

    def analyze_data(self, name, data):
        mean = sum(data) / len(data)
        var = sum([x**2 for x in data]) - mean**2
        report = self.make_report(name, mean, var)
        self.report_data(report)

    def report_data(self, report):
        self.report_saver.save_report(report)

