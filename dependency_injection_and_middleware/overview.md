# Dependency Injection and Middleware

* Common design patterns used in server frameworks
* Middleware is used to define a Pipeline (cross cutting concern)
* Dependency Injection is used to achieve inversion of control

## Dependency Injection

* A **ServiceProvider** registers classes (**Services**) and constructs them
  for those participating in the DI (**Clients**)
* **Services** are also **Clients**
* Dependencies of a **Client** are specified *declaratively* so that they can
  be provided to the **Client** when requested (typically on construction)

### Additional Considerations

* The **ServiceProvider** typically ensures that the *Dependency Graph* is a
  DAG
* The **ServiceProvider** provides a notion of *Lifetime* to **Services**
  (Singleton, Session, Scope)
* A common technique is for **Clients** to declare their dependencies as
  constructor parameters, the **ServiceProvider** must be capable of
  *introspecting* client dependencies (reflection).

## Middleware

* In some architectures, there is an overall *pipeline* of actions that must
  be taken for all input (server responding to messages)
* This pipeline must be easily configurable
* This pipeline should offer flow-control (ability to short circuit)

### Additional Considerations

* A typical protocol is for a middleware to receive the *next* middleware,
  then return a function which receives a *message* and returns a *response*
  (it may use the *next* middleware or not)
* Another protocol is for a middleware to get passed *message* and a
  *context*, and the middleware framework decides whether to call *next* based
  on the state of *context* (e.g. if a *reponse* is not-null on the *context*)


