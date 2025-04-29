# Bubble Sort and Insert Sort

This repository aims to provide a comprehensive starting point for understanding and implementing two fundamental sorting algorithms: Bubble Sort and Insertion Sort. These algorithms are implemented in Python and serve as a great introduction to sorting techniques for beginners and intermediate programmers.

<hr><br>

## Purpose of This Repository

### Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted. Although it is not the most efficient sorting algorithm for large datasets, it is easy to understand and implement.

### Insertion Sort

Insertion Sort is another simple sorting algorithm that builds the final sorted array one item at a time. It is much more efficient than Bubble Sort for small or nearly sorted datasets. It works by taking elements from the unsorted part of the array and inserting them into their correct position in the sorted part.

<hr><br>

## Demonstration

Here is a quick demo of the sorting algorithms in action:

### Bubble Sort Example

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
```

### Insertion Sort Example

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array is:", sorted_arr)
```

<hr><br>

## Features

- Easy-to-understand implementations of Bubble Sort and Insertion Sort
- Well-commented code for better understanding
- Suitable for beginners and intermediate programmers

<hr><br>

## Technologies Used

- Python

<hr><br>

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/n4vrl0s3/Bubble-Sort-and-Insert-Sort.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Bubble-Sort-and-Insert-Sort
   ```

<hr><br>

## Steps to Run

1. Ensure you have Python installed on your system.
2. Run the Python scripts:
   ```bash
   python program.py
   ```

<hr><br>

## License

This project is licensed under the GNU General Public v3.0 License. See the [LICENSE](LICENSE) file for details.

<hr><br>

<div align="center">
  <a href="https://www.x.com/n4vrl0s3/">
    <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=100:49108B,20:F3F8FF&section=footer&reversal=false&textBg=false&fontAlignY=50&descAlign=48&descAlignY=59"/>
  </a>
</div>
