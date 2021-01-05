def latihan_3(lists_3):
    n = len(lists_3)
    lists3_new = []
    for i in range(n):
        lists3_new.append(n * lists_3[i])
    total_lists3_new = sum(lists3_new)
    return total_lists3_new;


#case: buat module untuk 
#menghitung number of data yg ada di dalam suatu list
#kemudian jumlah data di list tsb, kita kalikan dengan masing2 data di dalam list, 
#yg kemudian angka2 tsb kita jumlah


def hitung_data_di_list(data_dalam_list):
    n = len(data_dalam_list)
    return n

def kalikan_angka_di_list(data_dalam_list,jumlah_data_di_list):
    lists3_new = []
    for i in range(jumlah_data_di_list):
        lists3_new.append(jumlah_data_di_list * data_dalam_list[i])
    return lists3_new

def jumlah_data_di_list(list_yg_baru):
    hasil_akhir = sum(list_yg_baru)
    return hasil_akhir



if __name__ == '__main__':
    import sys
    #data = sys.argv[1]
    #list_data = list(map(int, data.strip('[]').split(',')))
    #hasil = latihan_3(list_data)
    #print(hasil)
    #print('angka yang kamu ketik adalah',sys.argv[1])
    #username = input("Enter username:")
    #print("Username is: " + username)
    x=input("masukkan nilai x = ")
    print(int(x)*10)
    
    
    
    