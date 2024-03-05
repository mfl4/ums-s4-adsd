def sum_all_numbers(number):
    """
    Author : L200220277 (Mhd. Farhan Lubis)
    Date : 28/02/2024

    Calculate the sum of all numbers from 1 to the given number.
    Args:
        number (int): The input number for calculating the sum.
    Returns:
        int: The sum of all numbers from 1 to the given number.
    """
    # Mengecek apakah number sama dengan 1
    # maka mengembalikan 1
    if number == 1:
        return 1
    # Jika kondisi diatas tidak terpenuhi maka akan dicek apakah number kurang dari sama dengan 0
    # Jika kondisi ini terpenuhi maka akan mengembalikan pesan bahwa number harus lebih dari 0
    if number <= 0:
        return "number must be greater than 0"
    # Jika kondisi diatas tidak terpenuhi
    # maka akan mengembalikan jumlah dari number ditambah fungsi rekursif yang memiliki parameter dikurangi 1
    return number + sum_all_numbers(number - 1)

print(sum_all_numbers(int(input("Enter a number: "))))
print("\nProgram Completed!\n\n--- By L200220277 ---")