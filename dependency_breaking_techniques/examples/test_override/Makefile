CXX = g++ -std=c++11
CPPFLAGS = -O0 -g
OBJS = $(shell find . -name "*.cpp" | sed 's/\.cpp/.o/')

all: $(OBJS)
	$(CXX) $(CPPFLAGS) $^ -o test_report_generator.exe


.PHONY: clean
clean:
	rm *.o
