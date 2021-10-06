CXX=g++ -std=c++11
CPPFLAGS=-O0 -g
EXES=$(shell find . -name "*.cpp" | sed 's/\.cpp/.exe/')

all : $(EXES)
	echo $(EXES)

%.exe : %.o
	$(CXX) $(CPPFLAGS) $< -o $(<:.o=.exe)
