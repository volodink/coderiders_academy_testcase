package edu.codeinside.coderiders.sort;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
    Custom sorting rutines implementation.
**/

public class QuickSort {
    /**
        Return the sorted array, using simple qsort implementation.

        Args:
            array (list): Input array to sort.

        Returns:
            list: returns sorted list, using simple qsort implementation.

        Reference:
            https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python
    **/
    public static ArrayList<Integer> quicksort(ArrayList<Integer> array) {
        if (array.size() < 2) {
            return array;
        }

        ArrayList<Integer> low = new ArrayList<>();
        ArrayList<Integer> same = new ArrayList<>();
        ArrayList<Integer> high = new ArrayList<>();

        Integer pivot = array.get(new Random().ints(0, array.size() - 1).findFirst().getAsInt());

        array.forEach(item -> {
            if (item < pivot)
                low.add(item);
            else if (item == pivot)
                same.add(item);
            else if (item > pivot)
                high.add(item);
        });

        return (ArrayList<Integer>) Stream.of(quicksort(low), same, quicksort(high)).
                flatMap(Collection::stream).collect(Collectors.toList());
    }
}
