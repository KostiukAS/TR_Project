def greedy_algorithm(data):
    client_list = [(i, data[2][i], data[3][i] - data[2][i]) for i in range(data[0])]
    current_time = data[1]
    
    order = []
    x = []
    
    while client_list:
        min_diff = None
        client_with_min_diff = None
        for client in client_list:
            if min_diff is None or abs(client[1] - current_time) < min_diff:
                min_diff = abs(client[1] - current_time)
                client_with_min_diff = client
        
        order.append(client_with_min_diff[0])
        
        if current_time < client_with_min_diff[1]:
            x.append(client_with_min_diff[1])
            current_time = client_with_min_diff[1] + client_with_min_diff[2]
        else:
            x.append(current_time)
            current_time += client_with_min_diff[2]
        
        client_list.remove(client_with_min_diff)
    
    y = 0
    
    for i in range(len(order)):
        y += abs(x[i] - data[2][order[i]])
    
    return [order, x, y]
