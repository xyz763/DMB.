import java.util.Random;

public class RandomizedQuickSort {

    public static void QuickSort(int[] seq, int left, int right) {
        if (left < right) {
            int pivotIndex = left + new Random().nextInt(right - left + 1);
            swap(seq, pivotIndex, right);
            int pivot = seq[right];
            int partition = partitionIt(seq, left, right, pivot);
            QuickSort(seq, left, partition - 1);
            QuickSort(seq, partition + 1, right);
        }
    }

    public static int partitionIt(int[] seq, int left, int right, int pivot) {
        int leftPtr = left - 1;
        int rightPtr = right;
        while (true) {
            while (seq[++leftPtr] < pivot);
            while (rightPtr > 0 && seq[--rightPtr] > pivot);
            if (leftPtr >= rightPtr) break;
            swap(seq, leftPtr, rightPtr);
        }
        swap(seq, leftPtr, right);
        return leftPtr;
    }

    public static void swap(int[] seq, int a, int b) {
        int temp = seq[a];
        seq[a] = seq[b];
        seq[b] = temp;
    }

    public static void main(String[] args) {
        int[] seq = new Random().ints(10, 0, 100).toArray();
        System.out.println("Original Sequence:\n" + printSequence(seq));
        QuickSort(seq, 0, seq.length - 1);
        System.out.println("Sorted Sequence:\n" + printSequence(seq));
    }

    public static String printSequence(int[] seq) {
        StringBuilder sb = new StringBuilder();
        for (int num : seq) sb.append(num).append(" ");
        return sb.toString().trim();
    }
}
