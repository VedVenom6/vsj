// Unit 3: main thread, Runnable, multiple threads, synchronized
class Counter {
    int count = 0;
    synchronized void inc() { count++; }        // only one thread at a time
}

class Task implements Runnable {                // Runnable = preferred way (class can still extend another)
    private Counter counter;
    Task(Counter counter) { this.counter = counter; }

    public void run() {
        for (int i = 0; i < 1000; i++) counter.inc();
        System.out.println(Thread.currentThread().getName() + " finished");
    }
}

public class ThreadBasics {
    public static void main(String[] args) throws InterruptedException {
        Thread main = Thread.currentThread();
        System.out.println("Main thread: " + main.getName() + ", priority " + main.getPriority());

        Counter c = new Counter();
        Thread t1 = new Thread(new Task(c), "Worker-1");
        Thread t2 = new Thread(new Task(c), "Worker-2");
        Thread t3 = new Thread(new Task(c), "Worker-3");

        t1.start(); t2.start(); t3.start();     // start() -> new thread -> run()
        t1.join(); t2.join(); t3.join();

        System.out.println("Final count = " + c.count + " (always 3000 thanks to synchronized)");
    }
}
