# OOPCG Java – Lab & Concept Code

Java programs for SPPU SE Computer (2024 Pattern) **Object Oriented Programming & Computer Graphics Lab** (PCC-205-COM), organised by syllabus unit. Every file is self-contained: one public class, its own `main`, no packages.

## Run any program
```bash
cd unit3-oop
javac ATM.java
java ATM
```
Graphics programs (unit4, unit5 `Transform2D`) open a Swing window, so they need a desktop (not a headless terminal).

## Contents

| Folder | File | What it covers |
|---|---|---|
| unit1-basics | `Basics.java` | Data types, casting, operators, if/else, switch, all loops, break/continue |
| | `Calculator.java` | **Lab A1** – menu-driven calculator (do-while + switch) |
| | `ArrayStats.java` | Array input, sum / largest / even count |
| unit2-classes | `StudentDemo.java` | Class, constructors (default/param/copy), `this`, `static`, getters/setters, overloading, array of objects |
| | `Order.java` | **Lab A2** – e-commerce order, overloaded constructors, discount, invoice |
| | `Hotel.java` | **Lab A3** – hotel booking with a 2D array |
| | `ArgsAndIO.java` | Passing arrays, varargs, command-line args, BufferedReader, PrintWriter |
| unit3-oop | `SingleInheritance.java` | **Lab A4** – single + multilevel inheritance, `super`, overriding |
| | `MultipleInterface.java` | **Lab A5** – multiple inheritance via interfaces, polymorphism |
| | `ShapesAbstract.java` | Abstract class, dynamic binding, `final`, `toString` |
| | `ATM.java` | **Lab A6** – ATM with try / multiple catch / finally / throw |
| | `ExceptionDemo.java` | Built-in exceptions, nested try, throws, custom exception |
| | `Chat.java` | **Lab A7** – multithreaded chat: isAlive, join, priorities, pause/resume/stop |
| | `ThreadBasics.java` | Main thread, Runnable, multiple threads, synchronized |
| unit4-graphics | `Lines.java` | **Lab B1** – DDA (dotted/thick rectangles) + Bresenham (dashed/solid diamond) |
| | `Circles.java` | **Lab B2** – DDA / Bresenham / Midpoint circles, solid/dotted/dashed |
| | `PolygonFill.java` | **Lab B3** – concave polygon: scan-line, flood, seed/boundary fill |
| | `SutherlandHodgeman.java` | **Lab B4** – polygon clipping, vertices entered interactively |
| | `CohenSutherland.java` | **Lab B5** – line clipping with outcodes |
| unit5-transforms | `Transform2D.java` | **Labs B6, B7, B8** – translate/scale/rotate/shear/reflect, triangle & rhombus, rotation about arbitrary point |
| | `Transform3D.java` | 3D translate / scale / rotate about X, Y, Z (4×4 matrices) |
| specific | – | Programs for specific problem statements, added later |

## Quick theory reminders
- **Bresenham vs DDA:** Bresenham uses only integer add/subtract; DDA uses floating point + rounding.
- **Cohen–Sutherland:** both outcodes 0000 → accept; `code1 & code2 != 0` → reject; else clip and repeat.
- **Sutherland–Hodgeman cases:** in→in: V2 · in→out: intersection · out→out: nothing · out→in: intersection + V2.
- **Rotation about a point:** `T(xr,yr) · R(θ) · T(−xr,−yr)`.
- **suspend/resume/stop** are deprecated (deadlock / inconsistent state) → use flags.
