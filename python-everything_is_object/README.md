# 🧠 Python3: Mutable, Immutable... Everything Is Object!

## 📌 Introduction
In Python, everything is an object—from integers to lists to functions. This project explores how Python handles object identity, mutability, and memory management. Understanding these concepts helps us write more predictable and efficient code.

---

## 🔍 `id()` and `type()`
- `type(obj)` returns the type of an object (e.g., `int`, `str`, `list`).
- `id(obj)` returns the unique identifier (memory address) of an object in CPython.

```python
x = 42
print(type(x))  # <class 'int'>
print(id(x))    # e.g., 9788736
