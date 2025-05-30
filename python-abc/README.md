# Python Object-Oriented Programming (OOP) Concepts

This repository contains exercises demonstrating key Object-Oriented Programming concepts in Python, including abstract classes, interfaces, duck typing, subclassing, and multiple inheritance.

## Tasks

### Mandatory

#### 0. Abstract Animal Class and its Subclasses
- **File**: `task_00_abc.py`
- **Concepts**: Abstract Base Classes (ABC), method overriding
- **Description**: 
  - Create an abstract `Animal` class with abstract `sound()` method
  - Implement `Dog` and `Cat` subclasses with specific sound implementations

#### 1. Shapes, Interfaces, and Duck Typing
- **File**: `task_01_shapes.py`
- **Concepts**: Duck typing, polymorphism
- **Description**:
  - Implement `Circle` and `Rectangle` classes with `area()` methods
  - Demonstrate duck typing by treating different shapes uniformly

#### 2. Extending the Python List with Notifications
- **File**: `task_02_list.py`
- **Concepts**: Subclassing built-in types
- **Description**:
  - Create `NotifyingList` that extends `list`
  - Add notifications when items are added/removed

### Advanced

#### 3. CountedIterator - Keeping Track of Iteration
- **File**: `task_03_countediterator.py`
- **Concepts**: Custom iterators
- **Description**:
  - Implement `CountedIterator` that tracks number of items iterated
  - Extend standard iteration protocol

#### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
- **File**: `task_04_flyingfish.py`
- **Concepts**: Multiple inheritance, MRO
- **Description**:
  - Create `Fish` and `Bird` classes
  - Implement `FlyingFish` that inherits from both

#### 5. The Mystical Dragon - Mastering Mixins
- **File**: `task_05_dragon.py`
- **Concepts**: Mixins, composition
- **Description**:
  - Create `FireBreathingMixin` and `FlyingMixin`
  - Combine them in `Dragon` class

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-abc.git
   cd python-abc
