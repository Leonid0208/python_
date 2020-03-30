n =int(input())
namespaces = {'global': []}
for i in range(0,n):
    request = input().split()
    if request[0] == 'add':
        namespaces[request[1]]+= [request[2]]
        namespaces[request[2]] = []
    elif request[0] == 'create':
        namespaces[request[2]]+= [request[1]]
        namespaces[request[1]] = []
    else:
        if request[1] not in namespaces:
            print("global")
        else:
            if request[2] in namespaces[request[1]]:
                print(request[1])
            else:
                namespace = request[1]
                while namespace!='global':
                    for key, value in namespaces.items():
                        for i in value:
                            if i == request[2]:
                                namespace=key
                                break
                        if namespace==key:
                            break
                    if namespace==key:
                        break
                if namespace ==request[1] and request[2] not in namespaces['global']:
                    print('None')
                else:
                    print(namespace)



