#include <algorithm>
#include <exception>
#include <iterator>
#include <numeric>
#include <string>
#include <vector>

#include "report_generator.h"

using namespace std;

ReportSaver::ReportSaver() { throw exception(); }

void ReportSaver::save_report(const Report &report) { throw exception(); }

ReportGenerator::ReportGenerator() { report_saver = make_report_saver(); }

void ReportGenerator::analyze_data(string name, const vector<double> &data) {
    double mean = accumulate(data.begin(), data.end(), 0);
    vector<double> data_squared;
    transform(
        data.begin(),
        data.end(),
        back_insert_iterator<decltype(data_squared)>(data_squared),
        [](double x) { return x*x; }
    );
    double var = accumulate(data_squared.begin(), data_squared.end(), 0) - mean*mean;
    auto report = make_report(name, mean, var);
}

Report ReportGenerator::make_report(string name, double mean, double var) {
    return Report{name, mean, var};
}

void ReportGenerator::report_data(const Report &report) { report_saver->save_report(report); }

IReportSaver* ReportGenerator::make_report_saver() { return new ReportSaver(); }

ReportGenerator::~ReportGenerator() { delete report_saver; }
