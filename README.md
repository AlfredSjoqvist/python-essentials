# Python Programming Essentials

This repository collects a cohesive series of Python projects progressing from programming fundamentals to algorithms, interpreters and data abstraction. The focus is on clean design, algorithmic reasoning, recursion, functional techniques, and building maintainable, testable systems.

## Skills Demonstrated

* Core Python: functions, modular structure, control flow, collections
* Iteration and recursion over flat and nested data
* Combinatorics, numeric algorithms and recursive definitions
* Pattern matching, tree search and structured data traversal
* Image processing pipelines using OpenCV
* Language implementation: ASTs, interpreters, and environment threading
* Data abstraction, invariants and layered API design
* Unit testing, error handling and defensive programming
* Git-based workflow and incremental refactoring

## Project Overview

### control-flow

Programs built around conditionals, loops and list operations. Covers digit extraction, accumulation patterns, list transformations, and basic algorithm construction using sequential computation.

### recursion-dictionaries

Introductory recursion and dictionary-based problem solving. Includes:

* Swedish personal ID validation via checksum logic
* Sparse board representation and operations on large coordinate grids
* Recursive implementations of exponentiation, summation, and binomial choose

### recursion-strings

Recursive algorithms on strings, lists and nested structures. Highlights:

* Splitting encoded strings into parallel hidden messages
* Removing vowels and searching nested collections
* A small expression evaluator using recursive descent

### recursion-trees

Binary search tree utilities using a clean tree abstraction layer. Implements:

* Search, membership, insertion, size and depth queries
* Structural validation of tree shape
* Recursion patterns on immutable tree representations

### opencv-image-processing

A lightweight image-processing toolkit built with OpenCV:

* Image loading, grayscale transforms, thresholding and color adjustments
* Functional composition of filters
* Error handling and small-scale IO testing

### pattern-matching

Sequence and nested-structure pattern matching algorithms:

* Recursive wildcard matching on lists
* Structural pattern matching across book metadata
* Basic tree traversal utilities

### calc-language

A full interpreter for a tiny language ("Calc"):

* Programs represented as explicit ASTs
* Core evaluator for arithmetic, conditionals and selections
* Extended support for variables, assignment, environments and while-loops
* Pure functional evaluation model without global state

### calendar-data-abstraction

A small personal calendar system emphasizing data abstraction and separation of concerns:

* Representations for dates, times, durations and time spans
* Booking logic with non-overlapping constraints
* Querying availability across days or months
* Separation between abstraction layer, booking logic, output formatting and UI
