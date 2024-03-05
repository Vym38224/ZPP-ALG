import lin_dat_str as lds

root = {"id":1, 
    "child":[{"id":2, 
        "child":[{"id":5, 
            "child":[],
            "siblin":[{"id":6, 
                "child":[{"id":10, 
                    "child":[],
                    "siblin":[{"id":11,
                        "child":[],
                        "siblin":[{"id":12,
                            "child":[], 
                            "siblin":[]}]}]}],
                "siblin":[{"id":7,"child":[],"siblin":[]}]}]}], 
        "siblin":[{"id":3,
            "child":[],
            "siblin":[{"id":4,
                "child":[{"id":8,
                    "child":[],
                    "siblin":[{"id":9,
                        "child":[],
                        "siblin":[]}]}], 
                "siblin":[]}]}]}],
    "siblin":[]}
        

      
"""def depth_first_search_iter(node):
    x=node
    S=lds.init_stack(20)
    lds.push(S,x)
    while lds.empty_s(S)!=True:
        y=lds.pop(S)
        print(y["id"],end=" ")
        for i in range(y["n"]):
            lds.push(S,y["children"][i])

print("")
depth_first_search_iter(root)"""