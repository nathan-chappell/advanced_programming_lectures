from report_generator import ReportGenerator

class DummyReportSaver:
    def save_report(self, *args, **kwargs):
        pass

class TestReportGenerator(ReportGenerator):
    def make_report_saver(self):
        return DummyReportSaver()

    def report_data(self, report):
        self.report = report

def test_analyze_data():
    data = [1,2,3,4]
    # verify:
    #  mean = 2.5, var = 1.25
    report_generator = TestReportGenerator()
    report_generator.analyze_data('test-data', data)
    mean = report_generator.report['mean']
    var = report_generator.report['var']
    assert mean == 2.5
    assert var == 1.25
    
if __name__ == '__main__':
    test_analyze_data()
