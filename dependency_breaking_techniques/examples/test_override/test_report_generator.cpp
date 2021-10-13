#include<cassert>
#include<vector>

#include "report_generator.h"

using namespace std;

class DummyReportSaver: public IReportSaver {
public:
    void save_report(const Report &) override { }
};

class TestReportGenerator: public ReportGenerator {
public:
    Report report;
protected:
    IReportSaver *make_report_saver() override { return new DummyReportSaver(); }
    void report_data(const Report &report) override { this->report = report; }
};

void test_analyze_data() {
    vector<double> data{1,2,3,4};
    auto report_generator = TestReportGenerator();
    report_generator.analyze_data("test-data", data);
    double mean = report_generator.report.mean;
    double var = report_generator.report.var;
    // verify:
    // mean = 2.5, var = 1.25
    assert(mean == 2.5);
    assert(var == 1.25);
}

int main(int argc, const char **argv) {
    test_analyze_data();
}
