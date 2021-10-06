# Dependency Breaking Techniques

## Overview

## Techniques by Category

* Test-Override
* Parameter Modification
* Hierarchy Modification
* Globals
* Statics / Misc

### Test-Override
1. Subclass and Override Method - most fundamental technique.  Override
   behavior you wish to "ignore" in test-class
2. Extract and Override Call - factor out troublesome behavior into new
   method, override in test-class
3. Extract and Override Factory Method - delegate construction of objects in
   constructor to Factory Method (NOTE: may not apply to some C++ cases due to
   virtual calls not being honored in base class constructors)
4. Extract and Override Getter - delegate retrieval of required objects to
   getter

### Parameter Modification
1. Adapt Parameter - generalize a parameter so you can call the method with a
   simple implmentor
2. Parameterize Constructor - allow "injection" of implementors instead of
   constructing it directly (can maintain signatures)
3. Parameterize Method - same story, but for methods
4. Primitivize Parameter - expose inner-details to simplify testing (implies
   further refactorization)

### Hierarchy Modification
1. Pull-Up Feature - move the functionality you with to test into a
   super-class (make new abstract)
2. Push-Down Dependency - move code related to dependency into sub-class (make
   current class abstract)
3. Extract Interface - inversion of control

### Globals
1. Encapsulate Global Ref - move global dependencies behind some object (good
   use for singleton)
2. Introduce Static Setter - allow setting Singleton instance in testing
3. Replace Global Ref with Getter - have class get access to global through
   getter so it can be overridden in subclass

### Statics / Misc
1. Expose Static Method - if some method does not have any (too many)
   references to `this`, then make it static
2. Introduce Instance Delegator - if some static method is proving troubling,
   use indirection through instance method
3. Break-Out Method Object - if some complex method in a complex class needs
   to be tested, move all logic into its own object (then test the method on
   this object)


## Examples
