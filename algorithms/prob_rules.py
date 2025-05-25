import random

def prob_rules_algorithm(data, m=None):
    if m is None:
        m = data[0]
    
    orders = []
    x_s = []
    
    for _ in range(m):
        client_list = [(i, data[2][i], data[3][i] - data[2][i]) for i in range(data[0])]
        current_time = data[1]
        
        order = []
        x = []
        
        while client_list:
            diff = []
            
            for client in client_list:
                diff.append(abs(client[1] - current_time))
            
            rvs = [1 / (df + 1e-5) for df in diff]
            probs = [rv / sum(rvs) for rv in rvs]
            
            choosen_client = random.choices(client_list, weights=probs, k=1)[0]
            
            order.append(choosen_client[0])
            
            if current_time < choosen_client[1]:
                x.append(choosen_client[1])
                current_time = choosen_client[1] + choosen_client[2]
            else:
                x.append(current_time)
                current_time += choosen_client[2]
            
            client_list.remove(choosen_client)
        
        orders.append(order)
        x_s.append(x)
    
    y = None
    result_order = []
    result_x = []
    
    for rozklad, rozklad_x in zip(orders, x_s):
        y_temp = 0
        
        for i in range(len(rozklad)):
            y_temp += abs(rozklad_x[i] - data[2][rozklad[i]])
        
        if y is None or y_temp < y:
            y = y_temp
            result_order = rozklad
            result_x = rozklad_x
    
    return [result_order, result_x, y]
