def weight_rules_algorithm(data, w_gap=1.0, w_dur=0.5):

    n = data[0]
    t = data[1]
    s = data[2]
    f = data[3]
    
   
    d = [f[i] - s[i] for i in range(n)]
    
  
    client_list = [(i, s[i], d[i]) for i in range(n)]
    
  
    current_time = t
    
   
    order = []
    x = []
    
   
    while client_list:
        min_score = None
        selected_client = None
        
       
        for client in client_list:
            i, s_i, d_i = client
            
      
            gap = abs(s_i - current_time)
            
         
            score = w_gap * gap + w_dur * d_i
            
         
            if min_score is None or score < min_score:
                min_score = score
                selected_client = client
        
    
        client_index = selected_client[0]
        order.append(client_index)
        
     
        if current_time < s[client_index]:
            x_k = s[client_index]
        else:
            x_k = current_time
        
        x.append(x_k)
        
        
        current_time = x_k + d[client_index]
        
     
        client_list.remove(selected_client)
    
   
    y = sum(abs(x[k] - s[order[k]]) for k in range(n))
    
    return [order, x, y]