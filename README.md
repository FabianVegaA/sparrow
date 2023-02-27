# Sparrow

A library with a collection of decorators and functions to functional programming. It's a library that I use in my projects and I decided to share it with the community. I hope you enjoy it.

This library solves problems and limitations that I have found programming in Python, it especially with the creation of functions and methods, adding behaviour before and after the behaviour of the functions, with first intention to be used in the composition of functions.

## Installation

Comming soon...

## Utilities

| Name      | Description                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `compose` | Composes two functions                                                                                                           |
| `currify` | Returns a function that receives a variable number of parameters and returns a function that receives the rest of the parameters |
| `reflex`  | Reflects the return of the decorated function adding side effects                                                                |
| `before`  | Executes a function before the decorated function                                                                                |
| `after`   | Executes a function after the decorated function                                                                                 |
| `when`    | Executes a function when a condition is met if not it returns the value of the decorated function                                |

## Examples

### compose

```python
@compose(add(1), add(2), add(3), add(4))
def add_10_and_mul_by_100(x):
    return x * 100
```

### currify

```python
@currify
def add(x, y):
    return x + y

add_1 = add(1) # Returns a function that receives y
add_1(2) # 3
```

### reflex

```python
@reflex(print)
def add_1(x):
    return x + 1

add_1(1)
# output: 2
# display: 2
```

### before

```python
@before(int)
def add_1(x):
    return x + 1

add_1('1') # 2
```

### after

```python
@after(lambda x: x * 100)
def add_1_and_mul_by_100(x):
    return x + 1

add_1_and_mul_by_100(1) # 200
```

### when

```python
@when(lambda x: x != 0)
def inverse(x):
    return 1 / x

inverse(0) # 0
inverse(1) # 1
```
