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
        
def depth_first_search(node):
    x=node
    print(x["id"], end=" ")      
    if "child" in x:  
        for child in x["child"]:
            depth_first_search(child)  
    if "siblin" in x:  
        for sibling in x["siblin"]:
            depth_first_search(sibling)  
 
depth_first_search(root)

