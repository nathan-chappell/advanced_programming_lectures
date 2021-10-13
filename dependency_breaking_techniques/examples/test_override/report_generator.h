#include <string>
#include <vector>

struct Report {
    std::string name;
    double mean;
    double var;
};

class ReportSaver {
public:
    ReportSaver();
    void save_report(const Report &report);
};

class ReportGenerator {
private:
    ReportSaver report_saver;
public:
    ReportGenerator();

    virtual void analyze_data(std::string name, const std::vector<double> &data);

protected:
    virtual Report make_report(std::string name, double mean, double var);

    virtual void report_data(const Report &report); 
};
