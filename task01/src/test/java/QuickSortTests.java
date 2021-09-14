import edu.codeinside.coderiders.sort.QuickSort;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;

import java.util.ArrayList;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class QuickSortTests {

    private final ArrayList<Integer> random_list= new ArrayList<>();

    @BeforeEach
    void init() {
        // Getting 25 random ints to ArrayList
        IntStream.range(0, 25).forEach(n -> random_list.add(
                new Random().
                        ints(-10, 10).
                        findFirst().
                        getAsInt()));
    }

    @RepeatedTest(10)
    @DisplayName("╯°□°）╯")
    void test_quicksort_vs_default() {
        System.out.println(random_list);
        assertEquals(random_list.stream().sorted().collect(Collectors.toList()), QuickSort.quicksort(random_list));
    }
}
