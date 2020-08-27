#program masih ada kekurangan, pada bagian rajut utk purwadhika
#program membaca terdaoat dua 'a' jdi salah satu a terhapus, jdinya cuma dpt purwadhik

def urai(data):
    hasil = ''                  #variabel utk menampung tiap pengolahan looping
    for i in range(len(data)):  #membuat loop utk mengambil index tiap string
        hasil += data[:i+1]     #nilai hasil ditambahkan dimana tiap penambahan dihitung dri index pertama
    return hasil                #menyimpan nilai hasil

def rajut(data):
    hasil = ''                  #variabel utk menampung tiap pengolahan looping
    for i in data:              #membuat loop utk mengambil tiap string
        if i not in hasil:      #jika tiap i tidak ada dalam nilai dari variabel hasil,
            hasil += i          #maka hasil ditambahkan i
    return hasil                #menyimpan nilai hasil

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))
print('')
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))