def find_missing_number(numbers_list):
    """
    Find the missing number in the given array of numbers between 1 and 10.
    """
    # Mendefinisikan variabel missing_number
    # untuk menyimpan angka yang hilang
    missing_number = 0
    # Melakukan perulangan dari angka dari 1 sampai 10
    for number in range(1, 11):
        # Memeriksa jika angka pada jangkauan diatas
        # tidak ada pada numbers_list
        # maka missing_number diisi dengan angka tersebut
        if number not in numbers_list:
            missing_number = number
    # Mengembalikan pesan serta angka yang hilang
    return f"The Missing Number is: {str(missing_number)}"

print(find_missing_number([1, 2, 3, 4, 5, 6, 8, 9, 10]))
print("\nProgram Completed!\n\n--- By L200220277 ---")