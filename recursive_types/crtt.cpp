#include<iostream>
using namespace std;

/*
 * CRTT is enabled by the following from **the standard**
 * http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2014/n4296.pdf
 *
 * Chapter 9: Classes
 * (note 2)
 *     A class-name is inserted into the scope in which it is declared
 *     immediately after the class-name is seen.
 */

template<typename T>
class B {
public:
    // returning B& doesn't work right, see line 33
    // virtual B& f() {
    virtual T& f() { 
        cout << "B.f" << endl;
        return *(T*)this; 
    }
};

class D: public B<D> {
public:
    /*
    virtual D& f() override { 
        cout << "D.f" << endl;
        return *this;
    };
    */

    D& g() {
        cout << "D.g" << endl;
        return *this;
    };

};

int main(int argc, const char **argv) {
    D d{};
    d.f().g();
}
