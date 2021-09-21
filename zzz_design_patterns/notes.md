# pattern
solution that has worked repeatedly
dont use unnecessarily

# abstraction levels
- idioms - low level - language specific 
  eg: chained comparison operators, top level script env, conditional expressions, indexing during iteration
- design patterns - mid level - design part of system - language independent
  - singleton
  - template method
  - adapter
  - observer
- architectural patterns - high level - components and relationships
  eg: MVC, microservices, pipes, filters
  
# design patterns
- creational - create, instantiate objects
- structural - classes and objects and communication
- behavioral - responsibilities at run time

# design principles
- separate static and dynamic things
- program an interface not implementation
- prefer composition over inheritance?
- delegation?

# anatomy of design pattern
- intent
- motivation
- structure
- implementation

# singleton design pattern (creational)
class has only one instance
eg: printer manager, payroll

# template method (behavioral)
skeleton of algorithm whose steps can be overridden without changing structure

# adapter (structural)
convert one interface into another that the client expects