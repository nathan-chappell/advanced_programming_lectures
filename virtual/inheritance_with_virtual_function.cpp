
class B {
protected:
    int x{0xbeef};
public:
    virtual void f() { x += 0x1aab; }
};

class D : public B {
public:
    virtual void f() override { x += 0xeeab; }
};

int main(int argc, const char **argv) {
    D *dp = new D();
    B *bp = dp;

    dp->f();
    bp->f();
    dp->f();
    bp->f();
}
