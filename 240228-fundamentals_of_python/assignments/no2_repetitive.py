def remove_repetitive(number_list):
    """
    Author : L200220277 (Mhd. Farhan Lubis)
    Date : 28/02/2024

    Remove repetitive items from the list.
    Parameters:
        number_list (list): The list to remove repetitive items from.
    Returns:
        list: The list with repetitive items removed.
    """
    # Menginialisasi variabel unique_list yang bernilai list kosong
    unique_list = []
    # Mengecek apakah argumen number_list berupa list kosong atau tidak
    if len(number_list) != 0:
        # Melakukan iterasi pada argumen number_list
        for item in number_list:
            # Jika item pada argumen number_list tidak ada pada variabel unique_list
            # Maka item tersebut ditambahkan ke variabel unique_list
            if item not in unique_list:
                unique_list.append(item)
        # Jika panjang dari variabel unique_list sama dengan panjang dari argumen number_list`
        # Maka mengembalikan pesan bahwa list tersebut sudah unik
        if len(unique_list) == len(number_list):
            return "List is already unique"
        # Jika kondisi di atas tidak terpenuhi
        # maka mengembalikan unique_list yang sudah diproses
        return unique_list
    # Jika panjang unique_list yang diinisialisasi berupa list kosong
    # Maka mengembalikan pesan bahwa list tersebut kosong
    return "List is empty"

print(remove_repetitive([]))
print(remove_repetitive([2,2,3,4,4,4,5,5,6,7]))
print(remove_repetitive([2,3,4,5,6,7]))
print("\nProgram Completed!\n\n--- By L200220277 ---")