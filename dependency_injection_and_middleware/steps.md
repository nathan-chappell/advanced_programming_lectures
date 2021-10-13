# Tagged-Code Walkthrough 

## DI 1
* Messages consist of path and content
* Responses have content
* Server handles messages (Message -> Response)
* Need to implement middleware

## DI 2
* logger demonstrates the middleware "api"

## DI 3
* use `reduce` to build middleware
* implement a few more examples

## DI 4
* Router-middleware:
    * routing done by decorator factory 
    * global instance
    * unconditional short circuit
* Service-Provider:
    * basic idea of using introspection to construct arguments
    * global instance to register services

## DI 5
* first service implemented (HelloService)

## DI 6
* notion of singleton in service provider
* DataAdapter registered as singleton
* SearchService depends on DataAdapter
* subject removed from Message

## DI 7
* removed print from demo (rely on logger)
* making use of search service

## DI 8
* Authorization middleware
* Service Provider:
    * now a notion of session-scope
    * relies on caches (dicts)
    * utilized through context-manager

## DI 9
* DataAdapter becomes session-scope
* DataStore becomes singleton
* FooService session (for demo)

## DI 10
* Basically just make everything async
* adds some docstrings / comments
* maybe some slight refactoring
