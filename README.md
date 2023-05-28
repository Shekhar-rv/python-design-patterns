# Design Patterns in Python
Discover the modern implementation of design patterns in Python. This is a practical course that will teach you how to use design patterns in Python to write clean, maintainable, and reusable code. The link to the course is below.

```Link
https://www.udemy.com/course/design-patterns-python/
```

## Course Content and Notes
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

   * Link to SOLID Principles video
        ```link
        https://www.youtube.com/watch?v=pTB30aXS77U
        ```
    * Link to SOLID principles article on realpython.com
        ```link
        https://realpython.com/solid-principles-python/
        ```
2. Creational Design Patterns
    * Builder
        * Separate the construction of a complex object from its representation so that the same construction process can create different representations.
        ```link
        https://refactoring.guru/design-patterns/builder
        https://refactoring.guru/design-patterns/builder/python/example
        ```

Another great reasource I found for design patterns in python is the following link:
```link
https://refactoring.guru/design-patterns/python
```

## Development Environment

To run the development environment:

1. You will need to have Docker installed on your local machine and devcontainer CLI installed on your VSCode.
    ```
    Ctrl + Shift + P -> Dev Containers:Install devcontainer CLI
    ```
2. Create and open the dev container with the following command:

    ```bash
    make open-development-environment
    ```

3. In the dev environment, you can run the `main.py` by going to the `Run and Debug` on your left panel and clicking on the `Start Debugging` green button.

4. If you make any changes to the dev environment, you can rebuild it with the following command:

    ```
    Ctrl + Shift + P -> Dev Containers:Rebuild Container Without Cache
    ``` 