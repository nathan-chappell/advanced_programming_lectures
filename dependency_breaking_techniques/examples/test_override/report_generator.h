#include <string>
#include <vector>

struct Report {
    std::string name;
    double mean;
    double var;
};

class IReportSaver {
public:
    virtual void save_report(const Report &report) = 0;
};

class ReportSaver: public IReportSaver {
public:
    ReportSaver();
    virtual void save_report(const Report &report) override;
};

class ReportGenerator {
private:
    IReportSaver *report_saver;
public:
    ReportGenerator();

    virtual void analyze_data(std::string name, const std::vector<double> &data);
    virtual ~ReportGenerator();

protected:
    virtual Report make_report(std::string name, double mean, double var);

    virtual void report_data(const Report &report); 
    virtual IReportSaver *make_report_saver();
};
