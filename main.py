import Member_Transactions
import Kitap_transactions
import json
import Zaman
import modul_hata_yakala

while True:
    print("""
    ------------------------------------------------------------
    -      Halk Kutuphanesine Hosgeldiniz!                     -
    -                                                          -
    -   1- Uyelik Islemleri                                    -                    
    -   2- Kitap Islemleri                                     -                     
    -   0- Cikis                                               -                       
    -                                                          -
    ------------------------------------------------------------
    """)
    # modul_hata_yakala.hata_yakala(2)
    secim = modul_hata_yakala.hata_yakala(2)
    if secim==1:
        
        print("""
        ------------------------------------------------------------
    -                     Uyelik Islemleri                     -
    -                                                          -
    -   1- Uyeleri Listele                                     -                    
    -   2- Uye Ekleme                                          -                     
    -   3- Uye Ara                                             -                       
    -   4- Uye Sil                                             -                       
    -   5- Kitap Odunc Verme                                   -                       
    -   6- Kitap Iade                                          -                       
    -   7- Kitap Takibi                                        -                       
    -   0- Cikis                                               -                       
    -                                                          -
    ------------------------------------------------------------    
    """)
        print("Uyelik islemlerine giris yaptiniz!")
        uyelik_secimi=modul_hata_yakala.hata_yakala(7)

        if uyelik_secimi==1:
            Member_Transactions.list_member()
        
        elif uyelik_secimi==2:
            Member_Transactions.add_member()

        elif uyelik_secimi==3:
            Member_Transactions.check_member()

        elif uyelik_secimi==4:
            Member_Transactions.delete_member()

        elif uyelik_secimi==5:
            Member_Transactions.give_book()

        elif uyelik_secimi==6:
            Member_Transactions.receive_book()
        
        elif uyelik_secimi==7:
            Member_Transactions.members_book()


        



    #uyelik islemlerini def ekle

    if secim==2:
        
        print("""
        ------------------------------------------------------------
    -                     Kitap Islemleri                      -
    -                                                          -
    -   1- Kitaplari Listele                                   -                    
    -   2- Kitap Ekleme                                        -                     
    -   3- Kitap Ara                                           -                       
    -   4- Kitap Sil                                           -                                             
    -   0- Cikis                                               -                       
    -                                                          -
    ------------------------------------------------------------    
    """)
        print("Kitap islemlerine giris yaptiniz!")
        kitap_secimi=modul_hata_yakala.hata_yakala(4)
        kitap_secimi=int(input(("Lutfen yapmak istediginiz islem kodunu giriniz: ")))
    
        if kitap_secimi==0:
            print("Sistemden guvenle cikis yaptiniz! ")
            break
        elif kitap_secimi==1:
            Kitap_transactions.list_book()
        elif kitap_secimi==2:
            Kitap_transactions.add_book()

        elif kitap_secimi==3:
            Kitap_transactions.search_book()

        elif kitap_secimi==4:
            Kitap_transactions.delete_book()
        else:
            print("Yanlis giris yaptiniz tekrar deneyiniz!")
            kitap_secimi=int(input(("Lutfen yapmak istediginiz islem kodunu giriniz: ")))




            




    
    


    