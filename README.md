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
            provides interface for creating objects in a superclass, but allows
            subclasses to alter the type of objects that will be created
        </td>
        <td> <a href="/src/1_creational/1_01_factory.py">/src/1_creational/1_01_factory.py</a> </td>
    </tr>
    <tr>
        <td> 1.2 </td>
        <td> Abstract Factory </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 1.3 </td>
        <td> Builder </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 1.4 </td>
        <td> Singleton </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
    </tr>
    <tr>
        <td> 1.5 </td>
        <td> Prototype </td>
        <td></td>
        <td> <a href="url">link text</a> </td>
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
        <td></td>
        <td> <a href="url">link text</a> </td>
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