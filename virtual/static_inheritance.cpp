class B {
public:
    void f() {}
};

class D : public B {
public:
    void f() {}
};

int main(int argc, const char **argv) {
    D *dp = new D();
    B *bp = dp;

    dp->f();
    bp->f();
}
