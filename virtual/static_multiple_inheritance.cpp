class B {
protected:
    int x{0xbeef};
public:
    void f() { x += 0x1aab; }
};

class C {
protected:
    int x{0xbeef};
public:
    void f() { x += 0x1aac; }
};

class D : public B, public C {
public:
    // this is now ambiguous
    // void f() { x += 0xeeab; }
    void f() { B::x += 0xeeab; C::x += 0xeeac; }
};

int main(int argc, const char **argv) {
    D *dp = new D();
    B *bp = dp;
    C *cp = dp;

    dp->f();
    bp->f();
    cp->f();
}
