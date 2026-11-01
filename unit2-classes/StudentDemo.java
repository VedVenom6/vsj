// Unit 2: class, fields, constructors (default/parameterized/copy), this, static,
// getters/setters, object as parameter, returning object, overloading, array of objects
class Student {
    private int roll;
    private String name;
    private double marks;
    static int count = 0;              // shared by all objects

    Student() {                        // default constructor
        this(0, "Unknown", 0);         // constructor chaining, must be first line
    }

    Student(int roll, String name, double marks) {   // parameterized
        this.roll = roll;
        this.name = name;
        this.marks = marks;
        count++;
    }

    Student(Student s) {               // copy constructor (written by hand in Java)
        this(s.roll, s.name, s.marks);
    }

    public String getName() { return name; }
    public double getMarks() { return marks; }
    public void setMarks(double m) {
        if (m >= 0 && m <= 100) marks = m;
        else System.out.println("Invalid marks");
    }

    Student topper(Student other) {    // object as parameter + returning object
        return (this.marks >= other.marks) ? this : other;
    }

    void show() { System.out.println(roll + " " + name + " " + marks); }       // overloading
    void show(String prefix) { System.out.println(prefix + ": " + name); }

    static int getCount() { return count; }
}

public class StudentDemo {
    public static void main(String[] args) {
        Student s1 = new Student(1, "Ved", 88);
        Student s2 = new Student(2, "Amit", 92);
        Student s3 = new Student(s1);
        Student s4 = new Student();

        s1.topper(s2).show("Topper");
        s3.setMarks(150);                      // Invalid marks
        s4.show();
        System.out.println("Objects: " + Student.getCount());

        Student[] list = { s1, s2, s3 };       // array of objects
        for (Student s : list) s.show();

        Student r = s1;                        // same object, two references
        r.setMarks(50);
        System.out.println("s1 marks now: " + s1.getMarks());   // 50.0
    }
}
