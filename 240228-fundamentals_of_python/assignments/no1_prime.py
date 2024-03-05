def check_prime(number):
    """
    Author : L200220277 (Mhd. Farhan Lubis)
    Date : 28/02/2024

    Check if the given number is prime or not.
    Parameters:
        number (int): The number to be checked for prime.
    Returns:
        str: "Prime" if the number is prime, "Not Prime" otherwise.
    """
    # Mengecek apakah number pada argumen lebih besar dari 1.
    if number > 1:
        # Melakukan iterasi dari 2 sampai number pada argumen
        for i in range(2, number):
            # Jika number pada argumen habis dibagi oleh i maka number pada argumen bukan bilangan prima
            if number % i == 0:
                return "Not Prime"
        # Jika kondisi sebelumnya tidak terpenuhi maka number argumen tersebut adalah bilangan prima
        return "Prime"
    # Jika lebih kecil dari 1, number tersebut bukan bilangan prima.
    return "Not Prime"

print(check_prime(int(input("Enter a number: "))))
print("\nProgram Completed!\n\n--- By L200220277 ---")
