package edu.codeinside.coderiders;

/**
 *
 */
public class Task02Application {

    /**
     * Main application method.
     * @param args command line arguments.
     */
    public static void main(String[] args) {
        System.out.println("The answer is:\n" +
                "    SELECT b.name, p.name\n" +
                "    FROM books AS b\n" +
                "    JOIN publishers AS p on p.id = b.publisher_id\n" +
                "    WHERE\n" +
                "        (b.year >= 2009 AND b.year <= 2018)\n" +
                "        AND\n" +
                "        (b.genre = 'tech' OR b.genre = 'cyberpunk');");

        System.out.println("\nSorry guys, no Hibernate or JDBC :( Hibernate is HARD, plain JDBC is so wrong.");
    }
}
