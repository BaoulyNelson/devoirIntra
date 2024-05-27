import proj2
import matplotlib.pyplot as plt
import seaborn as sns

def kesyon_1():
    print(proj2.repatisyon_depatman)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=proj2.df, x='department')
    plt.title('Repatisyon chak anplaye nn chak depatman')
    plt.xlabel('Depatman')
    plt.ylabel('Kantite anplwaye')
    plt.show()

def kesyon_2():
    print(proj2.repatisyon_seks_depatman)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=proj2.df, x='department', hue='gender')
    plt.title('Repatisyon par seks chak anplaye nn chak depatman')
    plt.xlabel('Depatman')
    plt.ylabel('Kantite anplwaye')
    plt.show()

def kesyon_3():
    print(proj2.laj_mwayen_anplaye)
    plt.figure(figsize=(10, 6))
    proj2.laj_mwayen_anplaye.plot(kind='bar')
    plt.title('Laj mwayenn anplaye pou chak depatman')
    plt.xlabel('Depatman')
    plt.ylabel('laj mwayenn')
    plt.show()
    
def kesyon_4():
    print(proj2.sale_mwayenn)
    plt.figure(figsize=(10, 6))
    proj2.sale_mwayenn.plot(kind='bar')
    plt.title('Sale mwayenn nan chak deptaman')
    plt.xlabel('Depatman')
    plt.ylabel('Sale mwayenn ')
    plt.show()

def kesyon_5():
    print(proj2.satisfaksyon_travay)
    plt.figure(figsize=(10, 6))
    proj2.satisfaksyon_travay.plot(kind='bar')
    plt.title('Satisfaskyon nan travay chak depatman')
    plt.xlabel('Depatman')
    plt.ylabel('Mwayenn satisfaksyon')
    plt.show()

    
def kesyon_6():
    print(proj2.mwayenn_tan_pwomosyon)
    plt.figure(figsize=(10, 6))
    proj2.mwayenn_tan_pwomosyon.plot(kind='bar')
    plt.title('Mwayenn ane denye pwomosyon pa depatman')
    plt.xlabel('Depatman')
    plt.ylabel('Ane depi denye pwomosyon')
    plt.show()
    
def kesyon_7():
    print(proj2.mwayenn_sale)
    plt.figure(figsize=(10, 6))
    proj2.mwayenn_sale.plot(kind='bar')
    plt.title('Sale mwayenn pa nivo edikasyon')
    plt.xlabel('Nivo Edikasyon')
    plt.ylabel('Mwayenn_sale')
    plt.show()
    
def invalid_option():
    print("Option sa envalid.")

def main():
    menu = {
        '1': kesyon_1,
        '2': kesyon_2,
        '3': kesyon_3,
        '4': kesyon_4,
        '5': kesyon_5,
        '6': kesyon_6,
        '7': kesyon_7
    }
    
    while True:
        print("\nMenu:")
        print("1. Repatisyon chak anplwaye nan chak depatman.")
        print("2. Repatisyon pa sèks nan chak depatman.")
        print("3. Mwayèn laj anplwaye yo pou chak depatman.\n\n4. Mwayèn salè nan chak depatman\n5. Satisfaksyon travay sou chak depatman\n\n6. Ki mwayèn tan ki genyen depi dènye fwa konpayi a te bay yon pwomosyon nan chak depatman?\n7. Bay mwayèn salè ki ekziste an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)." )
        print("\nQ. Quit")

        choice = input("Fe yon chwa: ").strip().upper()

        if choice == 'Q':
            print("Ou soti nan program nan. nou dezole pou sa")
            break
        else:
            
            menu.get(choice, invalid_option)()

if __name__ == "__main__":
    main()


