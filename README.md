# Design Patterns with Python

Design Patterns is the most essential part of Software Engineering, as they provide the general repeatable solution to a commonly occurring problem in software design.

These design patterns can be used as templates, describing how to solve particular software development problems with greater efficiency. Thereby, they offer reusable solutions for software design. While the patterns are generally programming language agnostic, this repository uses Python for demonstration purposes. Picking the correct design pattern for a problem often is difficult, understanding all patterns and their purpose is highly recommended to help with the decision.

<br>

----------------
----------------

<br>

## Types of Design Patterns

Design patterns can generally be divided into thee categories:

<br>

**1️⃣ Creational**

- focus on class instantiation or object creation
- class-creational patterns: use inheritance for effective instantiation process
- object-creational patterns: use delegation for effective instantiation process

<table>
    <tr>
        <th> ID </th>
        <th> Pattern </th>
        <th> Description </th>
        <th> Implementation </th>
    </tr>
    <tr>
        <td> 1.1 </td>
        <td> Factory </td>
        <td>
            provides interface for creating objects in a base class, but allows
            subclasses to alter the type of objects that will be created
        </td>
        <td> <a href="/src/1_creational/1_01_factory.py">/src/1_creational/1_01_factory.py</a> </td>
    </tr>
    <tr>
        <td> 1.2 </td>
        <td> Abstract Factory </td>
        <td>
            allows to produce families of related objects without specifying
            their concrete classes -> easy way to produce similar type of many
            objects
        </td>
        <td> <a href="/src/1_creational/1_02_abstract_factory.py">/src/1_creational/1_02_abstract_factory.py</a> </td>
    </tr>
    <tr>
        <td> 1.3 </td>
        <td> Builder </td>
        <td>
            separates the construction of a complex object from its
            representation, allowing the same construction process to create
            different representations -> construct complex objects step by step
            by providing flexibility to various object creation problems
        </td>
        <td> <a href="/src/1_creational/1_03_builder.py">/src/1_creational/1_03_builder.py</a> </td>
    </tr>
    <tr>
        <td> 1.4 </td>
        <td> Prototype </td>
        <td>
            aims to reduce number of classes used for an application by allowing
            to copy existing objects independent of the concrete implementation
            of their class at run-time (important e.g., when object creation is
            expensive)
        </td>
        <td> <a href="/src/1_creational/1_04_prototype.py">/src/1_creational/1_04_prototype.py</a> </td>
    </tr>
    <tr>
        <td> 1.5 </td>
        <td> Singleton </td>
        <td>
            provides one and only one instance of a particular class or object type
        </td>
        <td> <a href="/src/1_creational/1_05_singleton.py">/src/1_creational/1_05_singleton.py</a> </td>
    </tr>
</table>

<br>

**2️⃣ Structural**

- focus on organizing different classes and objects to from larger structures
- can provide new functionality through combinations

<table>
    <tr>
        <th>ID</th>
        <th>Pattern</th>
        <th>Description</th>
        <th>Link</th>
    </tr>
    <tr>
        <td> 2.1 </td>
        <td> Adapter </td>
        <td>
            helps to make two incompatible interfaces work together by creating
            a bridge between them -> allows to use existing classes with new
            interfaces
        </td>
        <td> <a href="/src/1_structural/1_06_adapter.py">/src/1_structural/1_06_adapter.py</a> </td>
    </tr>
    <tr>
        <td> 2.2 </td>
        <td> Bridge </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 2.3 </td>
        <td> Composite </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 2.4 </td>
        <td> Decorator </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 2.5 </td>
        <td> Facade </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 2.6 </td>
        <td> Flyweight </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 2.7 </td>
        <td> Proxy </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
</table>

<br>

**3️⃣ Behavioral**

- focus on identifying and realizing common communication patterns between objects

<table>
    <tr>
        <th>ID</th>
        <th>Pattern</th>
        <th>Description</th>
        <th>Link</th>
    </tr>
    <tr>
        <td> 3.1 </td>
        <td> Chain of Responsibility </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.2 </td>
        <td> Command </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.3 </td>
        <td> Iterator </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.4 </td>
        <td> Mediator </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.5 </td>
        <td> Memento </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.6 </td>
        <td> Observer </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.7 </td>
        <td> State </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.8 </td>
        <td> Strategy </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.9 </td>
        <td> Template </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 3.10 </td>
        <td> Visitor </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    
</table>

<br>

----------------
----------------

<br>

## Setup

The project uses [Poetry](https://python-poetry.org) to manage the project dependencies. Install dependencies via:

    `poetry install`

<br>

----------------
----------------

<br>

## Source

For more information about the patterns, check out:
- [Python Wife - Design Patterns in Python](https://pythonwife.com/design-patterns-in-python/)
- [StackAbuse - Design Patterns in Python](https://stackabuse.com/design-patterns-in-python/)
- [Geeks for Geeks - Python Design Patterns](https://www.geeksforgeeks.org/python-design-patterns/)