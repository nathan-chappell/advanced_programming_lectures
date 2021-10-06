# Virtual Functions in C++

1. Definitions
2. Discussion: How would you implement Virtual Functions?
3. Objdump / assembler prerequisites
4. C++: static single inheritance
5. C++: single inheritance with virtual functions
4. C++: static multiple inheritance
5. C++: multiple inheritance with virtual functions
6. C++: virtual inheritance


## Definitions

* Type
* Inheritance
* Dynamic Dispatch

## Discussion: How would you implement Virtual Functions?

* function table
* overrides

## Objdump / assembler prerequisites

* stack / registers
* push / pop
* call / ret
* mov / lea
* calling conventions

## C++: static single inheritance

### Main Takeaway
* static methods are just like functions

## C++: single inheritance with virtual functions

### Main Takeaway:
* vtable is stored at object, can easily be dereferenced

## C++: static multiple inheritance

### Main Takeaway:
* pointer-to-base now is given by an offset (function still called by name)

## C++: multiple inheritance with virtual functions
### Main Takeaway:
## C++: virtual inheritance
### Main Takeaway:
