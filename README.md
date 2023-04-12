# python-design-patterns
Modern implementation of design patterns in Python

## Table of Contents

1. SOLID Principles
   * Single Responsibility
       Make things (classes, functions, etc.) responsible for fulfilling one type of role.
       e.g. Refactor code responsibilities into separate classes.

   * Open/Closed
       Be able to add new functionality to existing code easily without modifying existing code.
       e.g. Use abstract classes. These can define what subclasses will require and strengthen Principle 1. by separating code duties.

   * Liskov Substitution
       When a class inherits from another class, the program shouldn't break and you shouldn't need to hack anything to use the subclass.
       e.g. Define constructor arguments to keep inheritance flexible.

   * Interface Segregation
        Make interfaces (parent abstract classes) more specific, rather than generic.
        e.g. Create more interfaces (classes) if needed and/or provide objects to constructors.

   * Dependency Inversion
       Make classes depend on abstract classes rather than non-abstract classes.
       e.g. Make classes inherit from abstract classes.