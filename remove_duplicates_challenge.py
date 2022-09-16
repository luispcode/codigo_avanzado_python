def remove_duplicates(lista):
    #set_var = set(lista)
    #no_duplicates = list(set_var)
    #return no_duplicates

    return list(set(lista))

def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()