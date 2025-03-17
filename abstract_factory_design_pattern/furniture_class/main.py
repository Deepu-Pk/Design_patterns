from furniture_factory import tableFactory,sofaFactory,chairFactory 



if(__name__ == "__main__"):
    # Chair
    chair_ob = chairFactory() 
    chair = chair_ob.createFurniture() 
    chair.create("Chair")

    # Table 
    table_ob = tableFactory() 
    table = table_ob.createFurniture() 
    table.create("Table") 

    # Sofa 
    sofa_ob = sofaFactory() 
    sofa = sofa_ob.createFurniture() 
    sofa.create("Sofa")
