package edu.codeinside.coderiders;

import edu.codeinside.coderiders.sort.QuickSort;

import java.util.ArrayList;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


public class Task01Application {
    public static void main(String[] args) {
        ArrayList<Integer> random_list = new ArrayList<>();

        // Fix seed to debug algorithm
        Random rnd_number_src = new Random();
        rnd_number_src.setSeed(123);

        // Pushing 25 random ints to ArrayList
        IntStream.range(0, 25).forEach(n -> random_list.add(
                rnd_number_src.
                        ints(0, 10).
                        findFirst().
                        getAsInt()));

        // Output results
        System.out.println("Random list => " + random_list);
        System.out.println("Sorted random list => " + random_list.stream().sorted().collect(Collectors.toList()));
        System.out.println("Quick sort implementation => " + QuickSort.quicksort(random_list));
    }
}
