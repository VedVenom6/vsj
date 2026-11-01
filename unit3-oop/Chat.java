// Lab A7: Multithreaded chat - isAlive(), join(), priorities, suspend/resume/stop.
// suspend()/resume()/stop() are deprecated (and throw UnsupportedOperationException in
// recent Java), so pausing and stopping are done safely with volatile flags.
class User extends Thread {
    private String[] msgs;
    private volatile boolean paused = false;
    private volatile boolean stopped = false;

    User(String name, String[] msgs) {
        super(name);
        this.msgs = msgs;
    }

    void pauseUser()  { paused = true; }
    void resumeUser() { paused = false; }
    void stopUser()   { stopped = true; }

    public void run() {
        for (String m : msgs) {
            if (stopped) break;
            while (paused && !stopped) {                 // "suspended"
                try { Thread.sleep(100); } catch (InterruptedException e) { }
            }
            if (stopped) break;
            System.out.println(getName() + " [P" + getPriority() + "]: " + m);
            try { Thread.sleep(500); } catch (InterruptedException e) { }
        }
        System.out.println(getName() + " left the chat");
    }
}

public class Chat {
    public static void main(String[] args) throws InterruptedException {
        User a = new User("Ved",   new String[]{"Hi", "How are you?", "What's up?", "Bye"});
        User b = new User("Amit",  new String[]{"Hello", "Good", "Studying", "See ya"});
        User c = new User("Admin", new String[]{"URGENT: server restart", "Done"});

        c.setPriority(Thread.MAX_PRIORITY);    // 10 - high-priority messages
        a.setPriority(Thread.NORM_PRIORITY);   // 5
        b.setPriority(Thread.MIN_PRIORITY);    // 1

        System.out.println("Ved alive before start? " + a.isAlive());   // false
        a.start(); b.start(); c.start();
        System.out.println("Ved alive after start?  " + a.isAlive());   // true

        Thread.sleep(600);
        b.pauseUser();   System.out.println(">> Amit suspended");
        Thread.sleep(1000);
        b.resumeUser();  System.out.println(">> Amit resumed");
        a.stopUser();    System.out.println(">> Ved stopped");

        a.join(); b.join(); c.join();          // main waits for all threads
        System.out.println("Ved alive after join?   " + a.isAlive());   // false
        System.out.println("Chat ended");
    }
}
